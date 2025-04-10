-- FEC Candidate Master Table
-- This table contains information about candidates running for federal office in the United States.
CREATE TABLE candidate_master (
    cand_id                 VARCHAR(9) PRIMARY KEY, -- Unique identifier for candidates
    cand_name               VARCHAR(200) NOT NULL,  -- Candidate’s full name
    cand_pty_affiliation    VARCHAR(3),             -- Three-character party code
    cand_election_yr        INTEGER NOT NULL,       -- Year of election
    cand_office_st          CHAR(2),                -- Two-character state abbreviation
    cand_office             CHAR(1),                -- House (H), Senate (S), President (P)
    cand_office_district    VARCHAR(2),             -- Congressional district (House races only, "00" for Senate)
    cand_ici                CHAR(1),                -- Incumbent (I), Challenger (C), Open (O)
    cand_status             CHAR(1),                -- Current (C), Future (F), Not running (N), Prior (P)
    cand_pcc                VARCHAR(9),             -- Linked principal campaign committee ID
    cand_st1                TEXT,                   -- Candidate’s mailing address
    cand_st2                TEXT,                   -- Candidate’s mailing address
    cand_city               VARCHAR(100), 
    cand_st                 CHAR(2),
    cand_zip                VARCHAR(10),
    election_cycle          INTEGER
);
CREATE UNIQUE INDEX idx_candidate_master_cand_id
ON candidate_master (cand_id);
