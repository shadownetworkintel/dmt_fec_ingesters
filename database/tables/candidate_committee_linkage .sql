-- candidate committee linkages
CREATE TABLE candidate_committee_linkage (
    cand_id              VARCHAR(9) NOT NULL, -- Unique candidate identifier
    cand_election_year   INTEGER NOT NULL,    -- Election year
    fec_election_year    INTEGER,             -- FEC election cycle year
    cmte_id              VARCHAR(9) NOT NULL, -- Unique committee identifier
    cmte_tp          	 CHAR(1),             --'C', 'D', 'E', 'H', 'I', 'N', 'O', 'P', 'Q', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z' -- Committee type codes
    cmte_dsgn			 CHAR(1),             --'A', 'B', 'D', 'J', 'P', 'U' -- Committee designation codes
    linkage_id			 SERIAL PRIMARY KEY,
    election_cycle       INTEGER
    );
