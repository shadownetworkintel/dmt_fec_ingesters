CREATE OR REPLACE VIEW vendor_category_map AS
WITH all_vendors AS (
    SELECT DISTINCT recipient_name
    FROM   schedule_b_disbursements
),

/* auto from vendor name */
name_cat AS (
    SELECT av.recipient_name,
           MIN(vnk.category) AS name_category
    FROM   all_vendors av
    JOIN   vendor_name_keywords vnk
      ON   LOWER(av.recipient_name) LIKE '%'||vnk.kw||'%'
    GROUP  BY av.recipient_name
),

/* auto from disbursement description */
purpose_cat AS (
    SELECT sb.recipient_name,
           MIN(pk.category) AS purpose_category
    FROM   schedule_b_disbursements sb
    JOIN   purpose_keywords pk
      ON   LOWER(sb.disbursement_description) LIKE '%'||pk.kw||'%'
    GROUP  BY sb.recipient_name
)

SELECT
    av.recipient_name,
    COALESCE(
        vcm_manual.category,   -- 1️⃣ manual overrides
        pc.purpose_category,   -- 2️⃣ description match
        nc.name_category,      -- 3️⃣ vendor-name match
        'Other'                -- 4️⃣ fallback
    ) AS category
FROM   all_vendors                av
LEFT   JOIN vendor_category_manual vcm_manual USING (recipient_name)
LEFT   JOIN name_cat              nc          USING (recipient_name)
LEFT   JOIN purpose_cat           pc          USING (recipient_name);


-- Fuzzy text search accelerators
CREATE EXTENSION IF NOT EXISTS pg_trgm;

CREATE INDEX IF NOT EXISTS idx_schedb_recipient_trgm
ON schedule_b_disbursements
USING gin (recipient_name gin_trgm_ops);

CREATE INDEX IF NOT EXISTS idx_schedb_disbursement_description_trgm
ON schedule_b_disbursements
USING gin (disbursement_description gin_trgm_ops);