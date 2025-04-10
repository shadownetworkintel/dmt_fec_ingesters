CREATE TABLE committee_contributions (
    id                      SERIAL PRIMARY KEY, -- Unique row identifier
    committee_id            VARCHAR(9) NOT NULL, -- The ID of the contributing committee
    contributor_name        VARCHAR(200), -- Name of the contributing committee
    contributor_type        CHAR(1) CHECK (contributor_type IN ('C', 'P', 'S', 'O')), -- Committee type (C=Candidate, P=Party, S=PAC, O=Other)
    recipient_committee_id  VARCHAR(9) NOT NULL, -- Receiving candidate or committee ID
    recipient_committee_name VARCHAR(200), -- Name of the recipient committee
    transaction_date        DATE, -- Date of the contribution
    transaction_amount      NUMERIC(12,2) NOT NULL, -- Contribution amount
    election_year           INTEGER, -- Election year of the recipient
    fec_election_year       INTEGER, -- FEC election cycle year
    receipt_type           VARCHAR(3), -- Type of receipt (e.g., "15E", "15J")
    memo_code              CHAR(1), -- Memo code indicator
    memo_text              TEXT, -- Additional memo text (if applicable)
    file_number            INTEGER, -- FEC file number for the contribution
    election_cycle         INTEGER, -- Election cycle for the contribution
    FOREIGN KEY (committee_id) REFERENCES committee_master(cmte_id) ON DELETE CASCADE,
    FOREIGN KEY (recipient_committee_id) REFERENCES committee_master(cmte_id) ON DELETE CASCADE
);
