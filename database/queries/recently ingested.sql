SELECT 
    cn.name,
    cn.candidate_id,
	s.committee_id,
    cn.state,
    cn.election_years,
    COUNT(*) 
FROM 
    schedule_a_contributions s
JOIN 
    committees cm ON s.committee_id = cm.committee_id
JOIN 
    candidates cn ON cn.candidate_id = ANY(
        SELECT jsonb_array_elements_text(cm.candidate_ids)
    )
WHERE 
    (
        s.ingestion_date >= CURRENT_DATE - INTERVAL '7 days' 
        OR s.last_updated >= CURRENT_DATE - INTERVAL '7 days'
    )
    AND EXISTS (
        SELECT 1 FROM jsonb_array_elements_text(cn.election_years) AS year
        WHERE year::int >= 2025 AND year::int <= 2026
    )
GROUP BY 
    s.committee_id, cn.election_years, cn.candidate_id, cn.name, cn.state
ORDER BY 
    COUNT(*) DESC;