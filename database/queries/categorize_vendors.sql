-- show recipients and related disbursement_descriptions, where they are fuzzy-filtered as "Other"
SELECT recipient_name, recipient_state, entity_type_desc, category,
string_agg(disbursement_description, ', '),
sum(disbursement_amount) as total_spent
FROM   schedule_b_disbursements sb
JOIN   vendor_category_map vcm USING (recipient_name)
WHERE  sb.committee_id = 'C00763045'
AND category = 'Other'
AND  sb.two_year_transaction_period = 2026
GROUP  BY recipient_name, recipient_state, entity_type_desc, category
having sum(disbursement_amount) > 5000
ORDER  BY total_spent DESC;

-- categorize a recipient (aka "vendor") by vendor name
INSERT INTO vendor_category_manual (recipient_name, category)
VALUES ('GUSTO', 'Payroll & Staff')
ON CONFLICT (recipient_name) DO UPDATE SET category = EXCLUDED.category;

-- categorize a recipient (aka "vendor") by purpose keyword
INSERT INTO purpose_keywords (kw, category)
VALUES ('salary', 'Payroll & Staff')
ON CONFLICT (kw) DO UPDATE SET category = EXCLUDED.category;

select * from vendor_category_manual

select * from purpose_keywords

select * from vendor_name_keywords