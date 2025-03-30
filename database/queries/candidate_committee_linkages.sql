select committee_name, purpose, transaction_dt, transaction_amt from fec_operating_expenditures oe
join fec_committee_master cm on oe.cmte_id = cm.committee_id
where state = 'KY' 
order by transaction_dt desc
--group by committee_name, purpose

select cm.committee_name, cam.candidate_name, cm.connected_organization_name
from fec_candidate_committee_linkages ccl
join fec_committee_master cm on ccl.cmte_id = cm.committee_id
join fec_candidate_master cam on ccl.cand_id = cam.candidate_id
where cam.state = 'KY'