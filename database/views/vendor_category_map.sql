CREATE OR REPLACE VIEW vendor_category_map AS
WITH all_vendors AS (
    SELECT DISTINCT recipient_name
    FROM   schedule_b_disbursements               -- source of truth
)
SELECT
    av.recipient_name,

    /* ---- Priority: manual → fuzzy → 'Other' ---- */
    COALESCE(
        vcm_manual.category,           -- 1️⃣ hand-tagged
        CASE                           -- 2️⃣ fuzzy rules
            WHEN av.recipient_name ILIKE ANY (ARRAY[
                 '%media%', '%communication%', '%digital%', '%advert%'])
                 THEN 'Media & Digital'

            WHEN av.recipient_name ILIKE ANY (ARRAY[
                 '%consult%', '%strateg%', '%advisor%', '%lobby%'])
                 THEN 'Consulting'

            WHEN av.recipient_name ILIKE ANY (ARRAY[
                 '%print%', '%mailer%', '%mailing%', '%litho%'])
                 THEN 'Printing & Mail'

            WHEN av.recipient_name ILIKE ANY (ARRAY[
                 '%payroll%', '%salary%', '%wage%', '%benefit%'])
                 THEN 'Payroll'

            WHEN av.recipient_name ILIKE ANY (ARRAY[
                 '%legal%', '%law%', '%compliance%'])
                 THEN 'Legal'

            WHEN av.recipient_name ILIKE ANY (ARRAY[
                 '%poll%', '%research%', '%survey%'])
                 THEN 'Polling & Research'

            WHEN av.recipient_name ILIKE ANY (ARRAY[
                 '%travel%', '%air%', '%hotel%', '%transport%'])
                 THEN 'Travel'

            ELSE 'Other'
        END
    ) AS category
FROM all_vendors            av
LEFT JOIN vendor_category_manual vcm_manual
       ON av.recipient_name = vcm_manual.recipient_name;


CREATE INDEX IF NOT EXISTS idx_schedule_b_recipient_name_trgm
ON schedule_b_disbursements
USING gin (recipient_name gin_trgm_ops);