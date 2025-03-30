-- Which committees raised the most money through "small dollar" donations in 2016?
-- Small dollar donations, defined as donations from an individual of less than $200, 
-- were a popular topic during the 2016 election. This query uses the information 
-- from the indiv (individual donations) table to sum the small dollar donations made 
-- to each committee. It produces a list of the 20 committees that raised the most 
-- money and the total amount contributed by small dollar donations in millions of 
-- dollars.

SELECT
  cmte_nm AS Committee_Name,
  SUM(transaction_amt)/1000000 AS Total_Small_Dollar_Donations_in_Millions
FROM (
  SELECT
    cmte_id
    ,transaction_amt
  FROM
    fec_indiv26
  WHERE
    transaction_amt>0
    --AND transaction_amt<200
   ) indiv
INNER JOIN
  fec_cm26 cmte
ON
  cmte.cmte_id=indiv.cmte_id
GROUP BY
  cmte_nm
ORDER BY
  2 desc
--LIMIT
--  20