import csv
import psycopg2
import argparse
import os
from zipfile import ZipFile
from datetime import datetime

DB_CONFIG = {
    'dbname': 'political_finance_data',
    'user': 'postgres',
    'password': 'EMvAYOrD#BYU8y',
    'host': 'localhost',
    'port': 5432
}

DATA_DIR = r'C:\Users\rasho\Campaign Finance\Data Sources'  # where your .zip files are located

def unzip_file(zip_filename, extracted_filename):
    zip_path = os.path.join(DATA_DIR, zip_filename)
    with ZipFile(zip_path, 'r') as zipf:
        zipf.extract(extracted_filename, path=DATA_DIR)
    return os.path.join(DATA_DIR, extracted_filename)

def parse_date(mmddyyyy):
    if mmddyyyy == '':
        return None
    try:
        return datetime.strptime(mmddyyyy, '%m%d%Y').date()
    except (ValueError, TypeError):
        return None

def load_candidate_master(conn, election_cycle):
    txt_file = unzip_file(f'cn{election_cycle % 100}.zip', 'cn.txt')
    with open(txt_file, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter='|')
        with conn.cursor() as cur:
            for row in reader:
                if not row or len(row) < 15:
                    continue
                cur.execute("""
                    INSERT INTO candidate_master (
                        cand_id, cand_name, cand_pty_affiliation, cand_election_yr,
                        cand_office_st, cand_office, cand_office_district, cand_ici,
                        cand_status, cand_pcc, cand_st1, cand_st2, cand_city,
                        cand_st, cand_zip, election_cycle
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (cand_id) DO NOTHING;
                """, row + [election_cycle])
        conn.commit()
        
def load_committee_master(conn, election_cycle):
    txt_file = unzip_file(f'cm{election_cycle % 100}.zip', 'cm.txt')
    with open(txt_file, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter='|')
        with conn.cursor() as cur:
            for row in reader:
                if not row or len(row) < 15:
                    continue
                cur.execute("""
                    INSERT INTO committee_master (
                        cmte_id, cmte_nm, tres_nm, cmte_st1, cmte_st2, 
                        cmte_city, cmte_st, cmte_zip, cmte_dsgn,
                        cmte_tp, cmte_pty_affiliation, cmte_filing_freq,
                        org_tp, connected_org_nm, cand_id, election_cycle
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (cmte_id) DO NOTHING;
                """, row + [election_cycle])
        conn.commit()
        
def load_candidate_committee_linkage (conn, election_cycle):
    txt_file = unzip_file(f'ccl{election_cycle % 100}.zip', 'ccl.txt')
    with open(txt_file, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter='|')
        with conn.cursor() as cur:
            for row in reader:
                if not row or len(row) < 5:
                    continue
                cur.execute("""
                    INSERT INTO candidate_committee_linkage  (
                        cand_id, cand_election_year, fec_election_year, 
                        cmte_id, cmte_tp, cmte_dsgn, linkage_id, 
                        election_cycle
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (linkage_id) DO NOTHING;
                """, row + [election_cycle])
        conn.commit()
        
def load_individual_contributions (conn, election_cycle):
    txt_file = unzip_file(f'indiv{election_cycle % 100}.zip', 'itcont.txt')
    with open(txt_file, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter='|')
        with conn.cursor() as cur:
            batch_size = 500  # Commit every 500 rows
            row_count = 0
            for row in reader:
                if not row or len(row) < 21:
                    continue
                parsed_date = parse_date(row[13])
                row[13] = parsed_date

                cur.execute("""
                    INSERT INTO individual_contributions  (
                        cmte_id, amndt_ind, rpt_tp, 
                        transaction_pgi, image_num, transaction_tp, entity_tp, 
                        name, city, state, zip_code, employer, occupation, 
                        transaction_dt, transaction_amt, other_id,
                        tran_id, file_num, memo_code, memo_text, sub_id,
                        election_cycle    
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (tran_id) DO NOTHING;
                """, row + [election_cycle])
                row_count += 1

                if row_count % batch_size == 0:
                    conn.commit()
                    print(f'Inserted {row_count} rows...')

        #final commit for any remaining rows            
        conn.commit()
        print(f'Inserted {row_count} rows in total.')  

def load_committee_to_candidate_cont_and_ind_exp (conn, election_cycle):
    txt_file = unzip_file(f'pas2{election_cycle % 100}.zip', 'itpas2.txt')
    with open(txt_file, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter='|')
        with conn.cursor() as cur:
            batch_size = 500  # Commit every 500 rows
            row_count = 0
            for row in reader:
                if not row or len(row) < 22:
                    continue
                parsed_date = parse_date(row[13])
                row[13] = parsed_date

                cur.execute("""
                    INSERT INTO committee_to_candidate_cont_and_ind_exp  (
                        cmte_id, amndt_ind, rpt_tp, 
                        transaction_pgi, image_num, transaction_tp, entity_tp, 
                        name, city, state, zip_code, employer, occupation, 
                        transaction_dt, transaction_amt, other_id, cand_id,
                        tran_id, file_num, memo_cd, memo_text, sub_id,
                        election_cycle    
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (tran_id) DO NOTHING;
                """, row + [election_cycle])
                row_count += 1

                if row_count % batch_size == 0:
                    conn.commit()
                    print(f'Inserted {row_count} rows...')

        #final commit for any remaining rows            
        conn.commit()
        print(f'Inserted {row_count} rows in total.')
        
def load_committee_to_committee_trans (conn, election_cycle):
    txt_file = unzip_file(f'oth{election_cycle % 100}.zip', 'itoth.txt')
    with open(txt_file, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter='|')
        with conn.cursor() as cur:
            batch_size = 500  # Commit every 500 rows
            row_count = 0
            for row in reader:
                if not row or len(row) < 21:
                    continue
                parsed_date = parse_date(row[13])
                row[13] = parsed_date

                cur.execute("""
                    INSERT INTO committee_to_committee_trans  (
                        cmte_id, amndt_ind, rpt_tp, 
                        transaction_pgi, image_num, transaction_tp, entity_tp, 
                        name, city, state, zip_code, employer, occupation, 
                        transaction_dt, transaction_amt, other_id,
                        tran_id, file_num, memo_cd, memo_text, sub_id,
                        election_cycle    
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (tran_id) DO NOTHING;
                """, row + [election_cycle])
                row_count += 1

                if row_count % batch_size == 0:
                    conn.commit()
                    print(f'Inserted {row_count} rows...')

        #final commit for any remaining rows            
        conn.commit()
        print(f'Inserted {row_count} rows in total.')
        
def load_operating_expenditures (conn, election_cycle):
    txt_file = unzip_file(f'oppexp{election_cycle % 100}.zip', 'oppexp.txt')
    with open(txt_file, 'r', encoding='latin-1') as f:
        reader = csv.reader(f, delimiter='|')
        with conn.cursor() as cur:
            batch_size = 500  # Commit every 500 rows
            row_count = 0
            for row in reader:
                if not row or len(row) < 21:
                    continue
                parsed_date = parse_date(row[12])
                row[12] = parsed_date

                cur.execute("""
                    INSERT INTO operating_expenditures  (
                        cmte_id, amndt_ind, rpt_yr, rpt_tp, 
                        image_num, line_num, form_tp_cd, sched_tp_cd,
                        name, city, state, zip_code, transaction_dt, 
                        transaction_amt, transaction_pgi, purpose, 
                        category, category_desc, memo_cd, memo_text,
                        entity_tp, sub_id, file_num, tran_id, 
                        back_ref_tran_id, dummy_column, election_cycle    
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                    ON CONFLICT (tran_id) DO NOTHING;
                """, row + [election_cycle])
                row_count += 1

                if row_count % batch_size == 0:
                    conn.commit()
                    print(f'Inserted {row_count} rows...')

        #final commit for any remaining rows            
        conn.commit()
        print(f'Inserted {row_count} rows in total.')

def main():
    parser = argparse.ArgumentParser(description='Load FEC bulk data into PostgreSQL')
    parser.add_argument('dataset', choices=[
        'candidate_master', 'committee_master',
        'candidate_committee_linkage', 'individual_contributions',
        'committee_to_candidate', 'committee_to_committee', 
        'operating_expenditures', 'all'
    ])    
    parser.add_argument('--year', type=int, required=True, help='Election cycle year (e.g., 2024)')
    args = parser.parse_args()

    election_cycle = args.year
    conn = psycopg2.connect(**DB_CONFIG)
    if args.dataset == 'candidate_master' or args.dataset == 'all':
        print(f'Loading candidate master for {election_cycle}...')
        load_candidate_master(conn, election_cycle)
    if args.dataset == 'committee_master' or args.dataset == 'all':
        print(f'Loading committee master for {election_cycle}...')
        load_committee_master(conn, election_cycle)
    if args.dataset == 'candidate_committee_linkage' or args.dataset == 'all':
        print(f'Loading candidate committee linkage for {election_cycle}...')
        load_candidate_committee_linkage(conn, election_cycle)
    if args.dataset == 'individual_contributions' or args.dataset == 'all':
        print(f'Loading individual contributions for {election_cycle}...')
        load_individual_contributions(conn, election_cycle)
    if args.dataset == 'committee_to_candidate' or args.dataset == 'all':
        print(f'Loading committee to candidate contributions and independent expenditures for {election_cycle}...')
        load_committee_to_candidate_cont_and_ind_exp(conn, election_cycle)
    if args.dataset == 'committee_to_committee' or args.dataset == 'all':
        print(f'Loading committee to committee transactions for {election_cycle}...')
        load_committee_to_committee_trans(conn, election_cycle)
    if args.dataset == 'operating_expenditures' or args.dataset == 'all':
        print(f'Loading operating expenditures for {election_cycle}...')
        load_operating_expenditures(conn, election_cycle)

    conn.close()

if __name__ == '__main__':
    main()
