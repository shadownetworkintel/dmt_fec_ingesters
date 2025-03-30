--individual contributions
select 
cm.candidate_name
,cm.state
, sum(transaction_amt)
from fec_individual_contributions ic
join fec_committee_master ctm on ic.cmte_id = ctm.committee_id
join fec_candidate_master cm on ctm.candidate_id = cm.candidate_id
where office_sought = 'S'
group by 
cm.candidate_name
,cm.state
order by sum(transaction_amt) desc






--committee to candidate--
select 
cm.candidate_name
,cm.state
, sum(transaction_amt)
from fec_committee_to_candidate_contributions cc
join fec_committee_master ctm on cc.cmte_id = ctm.committee_id
join fec_candidate_master cm on cc.cand_id = cm.candidate_id
where office_sought = 'S'
group by 
cm.candidate_name
,cm.state
order by sum(transaction_amt) desc
;

select * from fec_house_senate_current_campaigns order by ttl_receipts desc


