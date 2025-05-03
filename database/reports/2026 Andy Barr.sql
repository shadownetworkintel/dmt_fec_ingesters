-- what candidates are running for us senate in kentucky in 2026?
select candidate_id, name, district, office_full, party from candidates 
where election_years @> '[2026]' 
and state = 'KY' 
AND UPPER(name) like '%BARR%'; -- S6KY00286 and H0KY06104
--and office = 'S' -- senate races only

-- what committees are named after the candidate
select * from committees 
where cycles @> '[2026]' 
AND UPPER(name) like '%ANDY BARR%' --C00467571, C00618777, C00633792

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
WHERE committee_id IN ('C00467571', 'C00618777', 'C00633792')
AND contribution_receipt_amount > 5000
ORDER BY
  contribution_receipt_amount DESC, contribution_receipt_date DESC; -- no contributions for andy barr for senate, only house

-- schedule b - disbursements
SELECT 
    committee_id,
    recipient_name,
    expenditure_description,
    disbursement_date,
    disbursement_amount
FROM schedule_b_disbursements
WHERE committee_id IN ('C00467571', 'C00618777', 'C00633792')
ORDER BY disbursement_date DESC;
-- This grabs every payment those committees have made.

-- schedule e - expenditures
SELECT
  candidate_id,
  candidate_name,
  committee_name,
  expenditure_date,
  expenditure_amount,
  payee_name,
  expenditure_description,
  support_oppose_indicator,
  pdf_url
FROM
  schedule_e_expenditures
WHERE
  candidate_id IN ('S6KY00286', 'H0KY06104')
ORDER BY
  expenditure_date DESC;
  
------------------ 
-- DIGGING DEEPER
------------------
-- 1 Identify PACs/Committees
SELECT DISTINCT committee_id, name, candidate_ids, committee_type, first_file_date, treasurer_name, city, state, sponsor_name, sponsor_state, sponsor_zip
FROM committees
WHERE committee_id in ('C00467571', 'C00618777', 'C00633792')
--and committee_type = 'O' -- these are super pacs;

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

---------------------------------------
-- Detect Bundled Donations to JFCs
---------------------------------------

WITH jfc_donations AS (
    SELECT
        contributor_name,
        contributor_employer,
        contributor_occupation,
        contributor_state,
        contributor_zip,
        committee_id,
        contribution_receipt_amount,
        contribution_receipt_date
    FROM
        schedule_a_contributions
    WHERE
        committee_id IN ('C00618777', 'C00633792')
        AND contribution_receipt_amount > 0
),
bundled_donors AS (
    SELECT
        contributor_name,
        contributor_employer,
        contributor_occupation,
        contributor_state,
        contributor_zip,
        COUNT(*) AS num_donations,
        SUM(contribution_receipt_amount) AS total_contributed,
        MAX(contribution_receipt_amount) AS largest_single_donation
    FROM
        jfc_donations
    GROUP BY
        contributor_name,
        contributor_employer,
        contributor_occupation,
        contributor_state,
        contributor_zip
    HAVING
        SUM(contribution_receipt_amount) >= 100000  -- Flag if total given ≥ $100k
        OR MAX(contribution_receipt_amount) >= 50000  -- Or any single gift ≥ $50k
)

SELECT
    *
FROM
    bundled_donors
ORDER BY
    total_contributed DESC;

----------------------------------
-- Track Where the JFC Money Flows
----------------------------------
WITH jfc_spending AS (
    SELECT
        recipient_committee_id,
        recipient_committee_name,
        committee_id AS source_committee_id,
        disbursement_amount,
        disbursement_date
    FROM
        schedule_b_disbursements
    WHERE
        committee_id IN ('C00618777', 'C00633792')
        AND disbursement_amount > 0
)

SELECT
    recipient_committee_id,
    recipient_committee_name,
    SUM(disbursement_amount) AS total_transferred,
    COUNT(*) AS num_transfers,
    ROUND(100.0 * SUM(disbursement_amount) / (SELECT SUM(disbursement_amount) FROM jfc_spending), 2) AS pct_of_total_disbursed
FROM
    jfc_spending
GROUP BY
    recipient_committee_id, recipient_committee_name
ORDER BY
    total_transferred DESC;

-------------------------------------------------
-- Check for Unusual Recipients (Dark Money Risk)
-------------------------------------------------
WITH jfc_spending AS (
    SELECT
        recipient_committee_id,
        recipient_committee_name,
        committee_id AS source_committee_id,
        disbursement_amount,
        disbursement_date
    FROM
        schedule_b_disbursements
    WHERE
        committee_id IN ('C00618777', 'C00633792')
        AND disbursement_amount > 0
)

SELECT
    recipient_committee_id,
    recipient_committee_name,
    SUM(disbursement_amount) AS total_disbursed
FROM
    jfc_spending
WHERE
    recipient_committee_name IS NULL
    OR recipient_committee_name ILIKE '%advocacy%'
    OR recipient_committee_name ILIKE '%association%'
    OR recipient_committee_name ILIKE '%alliance%'
    OR recipient_committee_name ILIKE '%coalition%'
    OR recipient_committee_name ILIKE '%action%'
GROUP BY
    recipient_committee_id, recipient_committee_name
ORDER BY
    total_disbursed DESC;

---------------------------------------
-- Dig into WINRED-related transactions:
---------------------------------------
-- Run this query to expand and see individual contributions via WINRED.
SELECT
    contributor_name,
    contributor_employer,
    contributor_occupation,
    contributor_state,
    contributor_zip,
    committee_id,
    contribution_receipt_amount,
    contribution_receipt_date,
    memo_text
FROM
    schedule_a_contributions
WHERE
    committee_id IN ('C00618777', 'C00633792','C00467571')
    AND contributor_name ILIKE '%WINRED%'
ORDER BY
    contribution_receipt_date DESC;
-- Look at:
-- memo_text field — this sometimes lists the true original donor in FEC filings.
-- Patterns — are there lots of $2,900 donations? Are they anonymous? Are they in huge clumps?

select count(*) 
from schedule_a_contributions 
where UPPER(contributor_name) ILIKE '%WINRED%'
-- this gives scale

-- Specifically, see if Schedule A for those JFCs includes 
-- individual names and earmarks to committees like Barr’s.
SELECT DISTINCT committee_id
FROM schedule_a_contributions
WHERE UPPER(memo_text) LIKE '%WINRED%'
-- Then investigate those committee_ids to see if they're 
-- JFCs (name includes 'Victory', 'Joint', etc.).

select * from committees where committee_id in ('C00003418','C00027466','C00074450','C00075820','C00116632','C00158402','C00162339','C00369033','C00371203','C00376939','C00394957','C00441014','C00444620','C00454074','C00458828','C00459255','C00461806','C00473371','C00476317','C00483487','C00491357','C00492785','C00494617','C00496075','C00498121','C00499392','C00499988','C00510164','C00539825','C00543983','C00545749','C00546788','C00547893','C00551275','C00551374','C00561597','C00568162','C00570945','C00571596','C00573444','C00608695','C00620518','C00632257','C00632828','C00652727','C00652743','C00658484','C00662767','C00665638','C00677286','C00678854','C00690891','C00692327','C00692343','C00696088','C00697789','C00701003','C00701672','C00706267','C00706614','C00708289','C00714865','C00718221','C00718627','C00725853','C00726042','C00730895','C00742007','C00748673','C00750521','C00758532','C00764829','C00766774','C00770180','C00770214','C00771246','C00773101','C00776120','C00779223','C00781112','C00783142','C00784934','C00791293','C00791574','C00798322','C00799288','C00801985','C00806307','C00806612','C00808279','C00815415','C00817072','C00817122','C00821231','C00822767','C00829705','C00830679','C00831222','C00834994','C00836403','C00837484','C00837492','C00839100','C00844159','C00845826','C00850321','C00851980','C00852889','C00855288','C00855528','C00856401','C00856773','C00858373','C00859058','C00865956','C00869016','C00870139','C00871152','C00872473','C00873828','C00877225','C00893594','C00895821','C00897918','C00898189')
-- 2. Check Schedule B:
-- Did the Victory Committees pay fees to WINRED?
-- If they paid huge fees (like 10-15% of donations collected), 
-- that's another bundling red flag.
-- You can run:

SELECT
    recipient_name,
    recipient_committee_id,
    disbursement_amount,
    disbursement_date,
    disbursement_description,
	memo_text
FROM
    schedule_b_disbursements
WHERE
    committee_id IN ('C00618777', 'C00633792')
    AND recipient_name ILIKE '%WINRED%'
ORDER BY
    disbursement_date ASC;
	
----------------------------------------------------------------
-- Here's a simple query you can use to auto-flag suspicious bundling:
----------------------------------------------------------------
SELECT
    contributor_name,
    contribution_receipt_amount,
    contribution_receipt_date,
    memo_text
FROM
    schedule_a_contributions
WHERE
    committee_id = 'C00633792'
    AND contributor_name ILIKE '%WINRED%'
    AND (memo_text ILIKE '%EARMARK NON-DIRECTED%' OR memo_text IS NULL)
    AND contribution_receipt_amount > 200
ORDER BY
    contribution_receipt_date ASC;


	-- Here's how to cross-check WINRED's filings to trace whether they properly disclosed the original donors behind those “EARMARK NON-DIRECTED” transactions.

-- 🔎 Goal:
-- You want to check WINRED’s Schedule A (itemized receipts) to match up donations earmarked for C00633792 (Andy Barr Victory Committee), and verify if donors were disclosed.

-- ✅ Step-by-step:
-- 1. Find WINRED’s committee ID:
-- WINRED’s main FEC committee ID is:
-- (This is their national-level fundraising platform.)
-- COMMITTEE_ID = 'C00694323'
select * from committees 
where  
UPPER(name) like '%WINRED%'
-- result: 'C00694323'

https://www.fec.gov/data/committee/C00618389/?tab=raising


-- 2. Query WINRED’s Schedule A for Andy Barr Victory Committee:
SELECT
    contributor_name,
    contributor_city,
    contributor_state,
    contribution_receipt_date,
    contribution_receipt_amount,
    committee_id,
    memo_text
FROM
    schedule_a_contributions
WHERE
    conduit_committee_id in ('C00618389','C00694323')  -- WINRED
    AND committee_id = 'C00633792'  -- Andy Barr Victory
    AND contribution_receipt_date BETWEEN '2025-01-01' AND '2025-03-31'
ORDER BY
    contribution_receipt_date;
-- 🎯 This will return all itemized receipts from donors who gave through WINRED to Andy Barr’s Victory Committee.

--> returned no results - chatgpt says: 
-- In FEC bulk data (and sometimes in the API), the conduit_committee_id field is often not populated, 
-- even when a contribution clearly flows through a conduit like WINRED.
-- Instead, WINRED appears as the reporting committee (committee_id) — 
-- and the actual recipient is listed in the memo_text or via earmark notation, 
-- NOT as recipient_committee_id (which only exists in Schedule B).


-- ✅ How to Get Contributions FUNNELED Through WINRED to Andy Barr’s Committee
-- Try this alternative query, which finds contributions reported by WINRED but 
-- earmarked for Andy Barr’s committee:

SELECT
    contributor_name,
    contributor_city,
    contributor_state,
    contribution_receipt_date,
    contribution_receipt_amount,
    committee_id AS reporting_committee,
    memo_text
select *
FROM
    schedule_a_contributions
WHERE
    --committee_id = 'C00618389'  -- WINRED is the reporting committee
    --AND 
	memo_text ILIKE '%ANDY BARR%'
	
-- 🔍 Why This Works:
-- WINRED files the transaction as if they received the donation.
-- The earmark for Andy Barr (or his committee, e.g. “C00633792”) will show up in memo_text.
-- The recipient's actual committee ID isn’t consistently recorded as a dedicated field (sadly), 
-- so you need to pattern match it.



-- 🧠 Bonus Tip:
-- You can also check:
-- Total earmarked transfers from WINRED to Andy Barr
SELECT
    SUM(contribution_receipt_amount)
FROM
    schedule_a_contributions
WHERE
    committee_id = 'C00618389'
    AND recipient_committee_id = 'C00633792'
    AND memo_text ILIKE '%EARMARK%'
-- If this amount roughly equals what Andy Barr reports getting from WINRED — but no donors are disclosed — it’s further proof of wrongdoing.

-- 📂 Optional: Match Against Schedule B
-- To dig deeper, match this against Schedule B (disbursements) from WINRED:


SELECT
    recipient_committee_id,
    disbursement_amount,
    disbursement_date,
    memo_text
FROM
    schedule_b_disbursements
WHERE
    committee_id = 'C00618389'
    AND recipient_committee_id = 'C00633792'
    AND disbursement_date BETWEEN '2025-01-01' AND '2025-03-31'
-- You’ll likely find the same dates and amounts as the contributions 
-- reported by Andy Barr, which confirms that WINRED was acting as a passthrough without disclosing the upstream donor.
-- 🔥 If confirmed:
-- You’ve identified:
-- A potential illegal bundling operation
-- Involving a national fundraising platform (WINRED)
-- Being used to fund a specific candidate (Andy Barr)
-- With large amounts of money and no donor traceability
-- This could be a major campaign finance violation — and possibly part of a wider pattern.
-- Would you like a report template or SQL-to-CSV export code for documenting your findings?





