CREATE TABLE schedule_e (
    id TEXT PRIMARY KEY,
    committee_id VARCHAR(9),
    committee_name TEXT,
    candidate_id VARCHAR(9),
    candidate_name TEXT,
    support_oppose_indicator CHAR(1),  -- 'S' or 'O'
    expenditure_amount NUMERIC(14, 2),
    expenditure_date DATE,
    filing_form VARCHAR(8),
    image_number TEXT,
    report_type VARCHAR(10),
    report_year SMALLINT,
    memo_code CHAR(1),
    memo_text TEXT,
    office CHAR(1),           -- 'H', 'S', or 'P'
    state CHAR(2),
    district VARCHAR(3),
    payee_name TEXT,
    payee_street_1 TEXT,
    payee_street_2 TEXT,
    payee_city TEXT,
    payee_state CHAR(2),
    payee_zip VARCHAR(10),
    disbursement_description TEXT,
    purpose TEXT,
    is_notice BOOLEAN,
    notary_sign_date DATE,
    pdf_url TEXT,
    line_number TEXT,
    file_number INTEGER,
    transaction_id TEXT,
    action_code TEXT,
    schedule_type VARCHAR(10),
    schedule_type_full TEXT,
    transaction_date DATE,
    election_type VARCHAR(5),
    election_type_full TEXT,
    is_foreign BOOLEAN,
    timestamp TIMESTAMPTZ DEFAULT now()
);

-- Fast lookup by committee
CREATE INDEX idx_schedule_e_committee ON schedule_e (committee_id);

-- Fast lookup by candidate and support/oppose
CREATE INDEX idx_schedule_e_candidate_support ON schedule_e (candidate_id, support_oppose_indicator);

-- Fast filtering by report year and election type
CREATE INDEX idx_schedule_e_year_election_type ON schedule_e (report_year, election_type);

-- For time-based queries
CREATE INDEX idx_schedule_e_expenditure_date ON schedule_e (expenditure_date);
CREATE INDEX idx_schedule_e_transaction_date ON schedule_e (transaction_date);

-- For geographic analysis
CREATE INDEX idx_schedule_e_state_district ON schedule_e (state, district);

-- Optional: Aggregate by payee
CREATE INDEX idx_schedule_e_payee ON schedule_e (payee_name);

-- Optional: Purpose aggregation
CREATE INDEX idx_schedule_e_purpose ON schedule_e (purpose);
