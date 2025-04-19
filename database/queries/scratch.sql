select * from candidate_master
where cand_id = 'S4NJ00185';

select * from committee_master
where cmte_id = 'C00540500';

select * from candidate_committee_linkage
where cand_id = 'S4NJ00185';

select * from candidate_committee_linkage
where cmte_id = 'C00540500';

select sum(transaction_amt) 
from committee_to_candidate_cont_and_ind_exp
where cand_id = 'S4NJ00185';

select sum(transaction_amt) 
from committee_to_candidate_cont_and_ind_exp 
where cmte_id = 'C00540500';

select sum(transaction_amt) 
from committee_to_committee_trans
where cmte_id = 'C00540500';

select * --name, cm.cmte_nm, transaction_pgi, transaction_dt, transaction_amt, sub_id 
from individual_contributions ic
--join committee_master cm on ic.cmte_id = cm.cmte_id
--join candidate_master cn on cm.cand_id = cn.cand_id
WHERE 
  trim(ic.cmte_id) = 'C00540500'
  AND transaction_dt = '2024-01-01'
  --AND transaction_tp = '15E'
  --AND data_type = 'processed'
order by transaction_amt desc;

select sum(transaction_amt) 
from operating_expenditures oe
join committee_master cm on oe.cmte_id = cm.cmte_id
join candidate_master cn on cm.cand_id = cn.cand_id
where oe.cmte_id = 'C00540500' and cand_election_yr = 2026 ;


select sum(transaction_amt) 
from committee_to_candidate_cont_and_ind_exp ie
join candidate_master cn on ie.cand_id = cn.cand_id
join committee_master cm on ie.cmte_id = cm.cmte_id
where cn.cand_id = 'S4NJ00185' and cand_election_yr = 2026 ;

SELECT *
FROM individual_contributions
WHERE transaction_amt >= 1000
  --AND is_individual = TRUE
  --AND committee_type = 'I'
  AND memo_code <> 'X'
  AND transaction_tp IN ('15', '15E', '15J')
  AND name IS NOT NULL;

SELECT distinct entity_tp, count(*)
FROM individual_contributions a
group by distinct entity_tp

JOIN committee_master cm
  ON a.cmte_id = cm.cmte_id
WHERE cm.cmte_tp IN ('I', 'O')  -- Super PACs
