-- Which committees supported the greatest number of candidates?
-- The dataset contains information about both candidates and campaigns,
-- as well as linkages between the two in the ccl (Committee Campaign 
-- Linkage) table. This query counts the number of candidates that each 
-- committee is associated with and JOINS with the candidate table to 
-- list the candidates each committee supports in addition to an 
-- aggregated count. 

SELECT
  cmte_nm as Committee_Name
  ,COUNT(DISTINCT(linkage_id)) as Number_of_Candidates
  ,STRING_AGG(distinct cand_name, ' | ') as Candidates_Supported
FROM (
  SELECT
    linkage_id
    ,cand_id
    ,cmte_id
  FROM
    fec_ccl26) link
INNER JOIN
  fec_cn26 cand ON cand.cand_id=link.cand_id
INNER JOIN
  fec_cm26 cmte ON cmte.cmte_id=link.cmte_id
GROUP BY
  cmte.cmte_nm
ORDER BY
  2 desc
--LIMIT
--  10