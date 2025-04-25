-- what candidates are running for us senate in kentucky in 2026?
select * from candidate_master 
where election_cycle = 2026 
and cand_office_st = 'KY' 
and cand_office = 'S'
AND UPPER(cand_name) like '%BARR';

-- schedule a - contributions
SELECT
  contributor_name,
  contributor_city,
  contributor_state,
  contribution_receipt_date,
  contribution_receipt_amount,
  committee_id,
  candidate_id
FROM
  schedule_a_contributions
WHERE
  candidate_id IN (
    'S6KY00211',  -- Pamela Stevenson
    'S6KY00229',  -- Wende Carol Kennedy
    'S6KY00237',  -- Daniel Cameron
    'S6KY00252',  -- Jared Randall
    'S6KY00260'   -- Michael James Faris
    'S6KY00278'   -- Michael James Faris
  )
  AND contribution_receipt_date >= '2023-01-01'
ORDER BY
  contribution_receipt_date DESC;


-- schedule e - expenditures
  SELECT
  spender_committee_name,
  payee_name,
  expenditure_date,
  expenditure_amount,
  support_oppose_indicator,
  candidate_id
  
select *
FROM
  schedule_e_expenditures
WHERE
  candidate_id IN (
    'S6KY00211',  -- Pamela Stevenson
    'S6KY00229',  -- Wende Carol Kennedy
    'S6KY00237',  -- Daniel Cameron
    'S6KY00252',  -- Jared Randall
    'S6KY00260'   -- Michael James Faris
    'S6KY00278'   -- Michael James Faris
  )
  AND expenditure_date >= '2023-01-01'
ORDER BY
  expenditure_date DESC;
------------------ 
-- DIGGING DEEPER
------------------
-- 1 Identify PACs/Committees Based in Kentucky
SELECT DISTINCT cmte_id, cmte_nm, cand_id, cmte_tp, tres_nm, cmte_city, cmte_st
FROM committee_master
WHERE cmte_st = 'KY' 
and cmte_id in ('C00467571', 'C00633792')
--and cmte_tp = 'O' -- these are super pacs;
--look for familiar political figures (McConnell, Cameron, Barr)

-- 2 Trace Contributions from Kentucky Donors (Schedule A)
SELECT contributor_name --,contributor_city, contributor_state  
	, committee_id, cmte_nm, tres_nm, cmte_st1, cmte_st2, cmte_city, cmte_st --, committee_name, candidate_name
	, cand_id, contribution_receipt_amount, contribution_receipt_date
--select sum(contribution_receipt_amount) 
FROM schedule_a_contributions sa
JOIN committee_master cm on sa.committee_id = cm.cmte_id
WHERE contributor_state = 'KY'
  --AND contribution_receipt_amount >= 200
  AND contribution_receipt_date >= '2021-01-01'
ORDER BY cmte_nm, contribution_receipt_amount DESC;
-- Which KY-based donors are giving big money? 
--    Humana, National Thoroughbred Racing Assoc, Dischinger Chris, Schaefer Katherine
-- Which PACs or candidates are they funding?
-- Any surprising out-of-state PACs receiving KY money?

-- 3. Trace PAC-to-PAC Transfers & Shell PACs
-- If you’ve loaded Schedule B (expenditures), look for:
SELECT recipient_committee_name, recipient_committee_id, committee_id AS sender_committee_id, disbursement_amount, disbursement_date
FROM schedule_b
WHERE recipient_committee_id IN (
  SELECT committee_id FROM committee_master WHERE committee_state = 'KY'
)
AND disbursement_amount > 1000
ORDER BY disbursement_date DESC;
-- PACs funneling money to KY-based PACs (or vice versa)
-- Reused or recycled entities
-- Out-of-state coordination

-- 4. Map Shared Vendors or Repeated Addresses
SELECT payee_name, payee_city, payee_state, committee_type_full, COUNT(*) AS num_txns, SUM(expenditure_amount) AS total_paid
FROM schedule_e_expenditures
WHERE payee_state = 'KY'
--AND expenditure_amount >= 200
GROUP BY payee_name, payee_city, payee_state, committee_type_full
ORDER BY total_paid DESC;
--Shared vendors between “independent” PACs and candidate campaigns
--Possible straw vendors (shell firms, legal or digital firms)


SELECT committee_name, contribution_receipt_amount, entity_type, fec_election_year, contributor_name, contributor_state, contributor_city, contributor_street_1
FROM schedule_a_contributions
WHERE committee_id in ('C00467571', 'C00633792')
ORDER BY contribution_receipt_amount DESC;

SELECT *
FROM schedule_e_expenditures
WHERE committee_id in ('C00467571', 'C00633792')
ORDER BY expenditure_date DESC;