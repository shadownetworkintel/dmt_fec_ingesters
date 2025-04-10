select sum(transaction_amt) from candidate_master cn
join committee_to_candidate_cont_and_ind_exp ie 
on cn.cand_id = ie.cand_id
join committee_master cm on cm.cmte_id = ie.cmte_id
where cn.cand_id = 'S8GA00180';

select * from candidate_committee_linkage
where cand_id = 'S8GA00180';

select sum(transaction_amt) from individual_contributions 
where cmte_id = 'C00886291';

select sum(transaction_amt) from committee_to_committee_trans
where cmte_id = 'C00886291';