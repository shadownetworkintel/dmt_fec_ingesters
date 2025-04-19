SELECT MAX(contribution_receipt_date) FROM schedule_a_contributions; -- returns future dates!

SELECT MAX(contribution_receipt_date)
FROM schedule_a_contributions
WHERE contribution_receipt_date <= CURRENT_DATE;-- returns latest non-future date

SELECT *
FROM schedule_a_contributions
WHERE contribution_receipt_date >= CURRENT_DATE; -- shows future-dated records

SELECT MAX(load_date) FROM schedule_a_contributions; -- 

-- 1. Opaque Entity Types (Not Individual Donors)
-- contributions not from individuals, 
-- which are more likely to be less transparent.
SELECT
  contributor_name,
  contributor_employer,
  contributor_occupation,
  entity_type,
  committee_id,
  committee_name,
  contribution_receipt_amount,
  contribution_receipt_date
FROM schedule_a_contributions
WHERE entity_type NOT IN ('IND', 'CAN')  -- Exclude individual and candidate self-funding
  AND contribution_receipt_amount >= 1000
ORDER BY contribution_receipt_date DESC;

-- 2. PAC-to-PAC Transfers (Harder to Trace Original Source)
-- PACs can funnel money to other PACs, obscuring the source.
SELECT
  contributor_name,
  entity_type,
  committee_id,
  committee_name,
  contribution_receipt_amount,
  contribution_receipt_date
FROM schedule_a_contributions
WHERE entity_type = 'PAC'
  AND contributor_name ILIKE '%PAC%'
ORDER BY contribution_receipt_amount DESC;

-- 3. Contributions with Minimal Employer/Occupation Info
-- These are often flagged as less transparent.
SELECT
  contributor_name,
  contributor_employer,
  contributor_occupation,
  entity_type,
  committee_id,
  contribution_receipt_amount,
  contribution_receipt_date
FROM schedule_a_contributions
WHERE (contributor_employer ILIKE '%retired%'
       OR contributor_employer IS NULL
       OR contributor_employer = '')
  AND (contributor_occupation IS NULL
       OR contributor_occupation = ''
       OR contributor_occupation ILIKE '%not provided%')
  AND contribution_receipt_amount > 500
ORDER BY contribution_receipt_date DESC;

-- 4. Filter by Committee Type (Like Super PACs)
-- To focus on Super PACs or other big players, 
-- join with the committee_master table:
SELECT a.contributor_name, a.contribution_receipt_amount, c.cmte_nm, c.cmte_tp
FROM schedule_a_contributions a
JOIN committee_master c ON a.committee_id = c.cmte_id
WHERE c.cmte_tp IN ('I', 'O')  -- I = Independent Expenditure-Only (Super PAC), O = Single Candidate Independent
ORDER BY a.contribution_receipt_amount DESC;


select distinct cmte_tp, count(*) from committee_master
group by distinct cmte_tp;

select * from committee_master where cmte_id = 'C00540302'