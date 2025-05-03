select committee_id
, contributor_employer
, contributor_occupation
, contributor_state
, contributor_zip
, contribution_receipt_amount
, contribution_receipt_date
from schedule_a_contributions
WHERE
    UPPER(contributor_name) = 'WINRED'
    AND memo_text ILIKE '%EARMARKED%'
-------------------------------------------------------------------------------
-- Report date: 2025-05-02
-- Summary of unattributed contributions where WINRED is the named contributor
-- but no individual donor information is disclosed
SELECT
    committee_id,
    COUNT(*) AS winred_contribution_count,
    SUM(contribution_receipt_amount) AS total_amount,
    MIN(contribution_receipt_date) AS first_date,
    MAX(contribution_receipt_date) AS last_date
FROM
    schedule_a_contributions
WHERE
    UPPER(contributor_name) = 'WINRED'
    AND memo_text ILIKE '%EARMARKED%'
    -- AND (
    --     contributor_employer IS NULL OR contributor_employer = ''
    -- )
    -- AND (
    --     contributor_occupation IS NULL OR contributor_occupation = ''
    -- )
    -- AND (
    --     contributor_state IS NULL OR contributor_state = ''
    -- )
    -- AND (
    --     contributor_zip IS NULL OR contributor_zip = ''
    -- )
GROUP BY
    committee_id
ORDER BY
    total_amount DESC;
-- This gives you a by-committee summary of contributions reported as coming from WINRED without donor details.

-- 📄 2. Example Rows Lacking Donor Information
-- Optional: See the first few individual records with missing donor info

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
    UPPER(contributor_name) = 'WINRED'
    AND memo_text ILIKE '%EARMARKED%'
    AND (
        contributor_employer IS NULL OR contributor_employer = ''
    )
    AND (
        contributor_occupation IS NULL OR contributor_occupation = ''
    )
    AND (
        contributor_state IS NULL OR contributor_state = ''
    )
    AND (
        contributor_zip IS NULL OR contributor_zip = ''
    )
ORDER BY
    contribution_receipt_date DESC
LIMIT 100;
