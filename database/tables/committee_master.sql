-- Description: This SQL script creates a table for storing information about political committees for 2025/2026 elections
CREATE TABLE committee_master (
    cmte_id                 VARCHAR(9) PRIMARY KEY, -- Unique identifier for the committee
    cmte_nm                 VARCHAR(200) NOT NULL,  -- Committee's full name
    tres_nm                 VARCHAR(200),           -- Treasurer's name
    cmte_st1                TEXT,                   -- Committee's mailing address
    cmte_st2                TEXT,                   -- Committee's mailing address
    cmte_city               VARCHAR(100),
    cmte_st                 CHAR(2),
    cmte_zip                VARCHAR(10),
    cmte_dsgn               CHAR(1),                -- 'A', 'B', 'D', 'J', 'P', 'U' -- Designation codes
    cmte_tp                 CHAR(1),                -- 'C', 'D', 'E', 'H', 'I', 'N', 'O', 'P', 'Q', 'S', 'U', 'V', 'W', 'X', 'Y', 'Z' -- Committee type codes
    cmte_pty_affiliation    VARCHAR(3),             -- Three-character party code
    cmte_filing_freq        CHAR(1),                -- 'A', 'M', 'Q', 'T', 'W', 'X', 'Y' Filing frequency codes
    org_tp                  VARCHAR(1),             -- Interest group category (if applicable)
    connected_org_nm        VARCHAR(200),           -- Name of connected organization (if applicable)
    cand_id                 VARCHAR(9),              -- Associated candidate (if applicable)
    election_cycle          INTEGER
);
CREATE UNIQUE INDEX idx_committee_master_cmte_id
ON committee_master (cmte_id);

-- The committee master file contains basic information for each committee 
-- registered with the Federal Election Commission, including:
-- Federal political action committees and party committees
-- Campaign committees for presidential, house, and senate candidates
-- Groups or organizations spending money for or against candidates for federal office
-- The file has one record per committee and shows the committee identification number, 
-- committee name, sponsor (when appropriate), treasurer name, committee address, 
-- information about the type of committee, and the candidate identification number 
-- (for campaign committees). 
-- The end-of-line (EOL) marker is line feed '\n' (LF, 0x0A, 10 in decimal).