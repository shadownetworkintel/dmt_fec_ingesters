--1. Who is spending the most via independent expenditures (Schedule E)?
--This shows top outside spenders.
SELECT 
    committee_name, candidate_name,
    support_oppose_indicator,
    SUM(expenditure_amount) AS total_spent
FROM 
    schedule_e_expenditures
WHERE 
    expenditure_date >= '2023-01-01'
GROUP BY 
    committee_name, candidate_name,
    support_oppose_indicator
ORDER BY 
    total_spent DESC
LIMIT 20;


--2. Who received the most support from independent expenditures?
--Find candidates being promoted or attacked.
SELECT 
    candidate_id, cand_name, cand_pty_affiliation,
    support_oppose_indicator,
    SUM(expenditure_amount) AS total_independent_expenditures
FROM 
    schedule_e_expenditures e
JOIN candidate_master cn on e.candidate_id = cn.cand_id
WHERE 
    --expenditure_date >= '2024-01-01'
GROUP BY 
    candidate_id, cand_name, cand_pty_affiliation, support_oppose_indicator
ORDER BY 
    total_independent_expenditures DESC
LIMIT 20;

--3. Which committees are contributing to the top independent spenders?
--This connects Schedule A (incoming funds) with Schedule E spenders.
--🕵️ This helps surface possible "pop-up" committees or conduits for dark money:
--when a committee gives lots of money to an outside spender that spends it right away.
SELECT 
    sa.contributor_committee_id,
    se.spender_committee_id,
    SUM(sa.contribution_amount) AS total_contributed
FROM 
    schedule_a_contributions sa
JOIN 
    schedule_e_expenditures se ON sa.recipient_committee_id = se.spender_committee_id
WHERE 
    sa.contribution_receipt_date >= '2023-01-01'
GROUP BY 
    sa.contributor_committee_id, se.spender_committee_id
ORDER BY 
    total_contributed DESC
LIMIT 20;

--4. Unitemized donors powering large independent spenders
--Large spenders funded mostly by small or unitemized contributions may be red flags.
SELECT 
    sa.recipient_committee_id,
    COUNT(*) FILTER (WHERE sa.contribution_amount < 200) AS small_donors,
    COUNT(*) AS total_donors,
    SUM(sa.contribution_amount) AS total_contributions
FROM 
    schedule_a_contributions sa
JOIN 
    schedule_e_expenditures se ON sa.recipient_committee_id = se.spender_committee_id
GROUP BY 
    sa.recipient_committee_id
HAVING 
    SUM(sa.contribution_amount) > 1000000
ORDER BY 
    small_donors::float / total_donors DESC
LIMIT 10;


--5. Rapid money-in, money-out behavior ("pop-up" PACs)
--Committees receiving money and quickly spending it are often vehicles for dark money.
SELECT 
    se.spender_committee_id,
    MIN(sa.contribution_receipt_date) AS first_donation,
    MIN(se.expenditure_date) AS first_expenditure,
    SUM(sa.contribution_amount) AS total_raised,
    SUM(se.expenditure_amount) AS total_spent
FROM 
    schedule_a_contributions sa
JOIN 
    schedule_e_expenditures se ON sa.recipient_committee_id = se.spender_committee_id
GROUP BY 
    se.spender_committee_id
HAVING 
    MIN(se.expenditure_date) <= MIN(sa.contribution_receipt_date) + INTERVAL '14 days'
ORDER BY 
    total_spent DESC
LIMIT 20;

