CREATE TABLE candidates (
    candidate_id TEXT PRIMARY KEY,
    name TEXT,
    candidate_status TEXT,
    candidate_status_full TEXT,
    cycle INTEGER,
    district TEXT,
    district_number INTEGER,
    election_years JSONB,
    federal_funds_flag BOOLEAN,
    first_file_date DATE,
    incumbent_challenge TEXT,
    incumbent_challenge_full TEXT,
    last_file_date DATE,
    load_date DATE,
    office TEXT,
    office_full TEXT,
    office_sought TEXT,
    party TEXT,
    party_full TEXT,
    state TEXT,
    state_full TEXT,
    active_through INTEGER,
    candidate_inactive BOOLEAN,
    candidate_election_years JSONB,
    committee_ids JSONB,
    has_raised_funds BOOLEAN,
    principal_campaign_committee_id TEXT,
    principal_campaign_committee_name TEXT,
    ingestion_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_updated TIMESTAMP
);
CREATE INDEX idx_candidates_candidate_id ON candidates (candidate_id);
CREATE INDEX idx_candidates_name ON candidates (name);
CREATE INDEX idx_candidates_state ON candidates (state);
CREATE INDEX idx_candidates_party ON candidates (party);
CREATE INDEX idx_candidates_office ON candidates (office);
CREATE INDEX idx_candidates_cycle ON candidates (cycle);
CREATE INDEX idx_candidates_committee_ids ON candidates USING GIN (committee_ids);
CREATE INDEX idx_candidates_election_years ON candidates USING GIN (election_years);