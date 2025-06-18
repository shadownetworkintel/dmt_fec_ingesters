-- show recipients and related disbursement_descriptions, where they are fuzzy-filtered as "Other"
SELECT recipient_name, recipient_state, 
string_agg(disbursement_description, ', '),
sum(disbursement_amount) as total_spent
FROM   schedule_b_disbursements sb
JOIN   vendor_category_map vcm USING (recipient_name)
WHERE  sb.committee_id = 'C00893271'
AND  sb.two_year_transaction_period = 2026
AND vcm.category = 'Other'
GROUP  BY recipient_name, recipient_state
having sum(disbursement_amount) > 10000
ORDER  BY total_spent DESC;

-- categorize a recipient (aka "vendor")
INSERT INTO vendor_category_manual (recipient_name, category)
VALUES ('BASE ENGAGER, LLC', 'Media & Digital')
ON CONFLICT (recipient_name) DO UPDATE SET category = EXCLUDED.category;