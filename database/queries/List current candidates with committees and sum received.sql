SELECT cm.committee_id,
  cn.candidate_id, 
  cn.name, 
  cn.state, 
  cn.office_full, 
  cn.district, 
  cn.incumbent_challenge_full, 
  cn.party_full as party,
  sum(contribution_receipt_amount)
FROM candidates cn
JOIN committees cm 
  ON cm.candidate_ids @> to_jsonb(json_build_array(cn.candidate_id))
  JOIN schedule_a_contributions sa
  ON sa.committee_id = cm.committee_id
WHERE cn.election_years @> '2026' AND sa.two_year_transaction_period = 2026
GROUP BY cm.committee_id,
  cn.candidate_id, 
  cn.name, 
  cn.state, 
  cn.office_full, 
  cn.district, 
  cn.incumbent_challenge_full, 
  cn.party;