-- candidate committee linkages
CREATE TABLE fec_ccl26 (
    cand_id              VARCHAR(9) NOT NULL, -- Unique candidate identifier
    cand_election_year   INTEGER NOT NULL, -- Election year
    fec_election_year    INTEGER, -- FEC election cycle year
    cmte_id              VARCHAR(9) NOT NULL, -- Unique committee identifier
    cmte_tp          	 CHAR(1) CHECK (cmte_tp IN ('C', 'D', 'E', 'H', 'I', 'N', 'O', 'P', 'Q', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z')), -- Committee type codes
    cmte_dsgn			 CHAR(1) CHECK (cmte_dsgn IN ('A', 'B', 'D', 'J', 'P', 'U')), -- Committee designation codes
    linkage_id			 INTEGER, 
    PRIMARY KEY (cand_id, cmte_id, cand_election_year)
);
