CREATE TABLE fec_all_candidates (
    image_link             TEXT, -- URL to candidate's image
    candidate_name         VARCHAR(200) NOT NULL, -- Candidate’s name
    candidate_id           VARCHAR(9) PRIMARY KEY, -- Unique identifier for candidates
    office_sought          CHAR(1) CHECK (office_sought IN ('H', 'S', 'P')), -- House, Senate, or Presidential
    candidate_office_state CHAR(2), -- State abbreviation
    candidate_office_district     VARCHAR(2), -- Congressional district (00 for Senate, 98 for at-large, 99 for unknown)
    candidate_party_affiliation   VARCHAR(3), -- Three-letter party code
    incumbent_challenger   CHAR(10) CHECK (incumbent_challenger IN ('INCUMBENT', 'CHALLENGER', 'OPEN')), -- Incumbent, Challenger, Open
    total_receipt     		NUMERIC(15, 2),
    total_disbursement     NUMERIC(15, 2), -- Total receipts and disbursements
    cash_on_hand_cop       NUMERIC(15, 2), -- Cash on hand
    debt_owed_by_committee NUMERIC(15, 2), -- Debt owed by candidate
    coverage_end_date      VARCHAR(10), -- Coverage end date    
    mailing_address_1      TEXT, -- Candidate mailing address
    mailing_address_2      TEXT, -- Candidate mailing address
    mailing_city           VARCHAR(100),
    mailing_state          CHAR(2),
    mailing_zip            VARCHAR(10),
    Individual_Itemized_Contribution	     NUMERIC(15, 2),
    Individual_Unitemized_Contribution	     NUMERIC(15, 2),
    Individual_Contribution	     NUMERIC(15, 2),
    Other_Committee_Contribution	     NUMERIC(15, 2),
    Party_Committee_Contribution	     NUMERIC(15, 2),
    Cand_Contribution	     NUMERIC(15, 2),
    Total_Contribution	     NUMERIC(15, 2),
    Transfer_From_Other_Auth_Committee	     NUMERIC(15, 2),
    Cand_Loan	     NUMERIC(15, 2),
    Other_Loan	     NUMERIC(15, 2),
    Total_Loan	     NUMERIC(15, 2),
    Offsets_To_Operating_Expenditure	     NUMERIC(15, 2),
    Offsets_To_Fundraising	     NUMERIC(15, 2),
    Offsets_To_Leagal_Accounting	     NUMERIC(15, 2),
    Other_Receipts	     NUMERIC(15, 2),
    Operating_Expenditure	     NUMERIC(15, 2),
    Exempt_Legal_Accounting_Disbursement	     NUMERIC(15, 2),
    Fundraising_Disbursement	     NUMERIC(15, 2),
    Transfer_To_Other_Auth_Committee	     NUMERIC(15, 2),
    Cand_Loan_Repayment	     NUMERIC(15, 2),
    Other_Loan_Repayment	     NUMERIC(15, 2),
    Total_Loan_Repayment	     NUMERIC(15, 2),
    Individual_Refund	     NUMERIC(15, 2),
    Party_Committee_Refund	     NUMERIC(15, 2),
    Other_Committee_Refund	     NUMERIC(15, 2),
    Total_Contribution_Refund	     NUMERIC(15, 2),
    Other_Disbursements	     NUMERIC(15, 2),
    Net_Contribution	     NUMERIC(15, 2),
    Net_Operating_Expenditure	     NUMERIC(15, 2),
    Cash_On_Hand_BOP	     NUMERIC(15, 2),
    Debt_Owe_To_Committee	     NUMERIC(15, 2),   
    Coverage_Start_Date     VARCHAR(10)
);
