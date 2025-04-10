CREATE TABLE individual_contributions (
	cmte_id                VARCHAR(9), -- filer identification number
	amndt_ind              VARCHAR(1), -- amendment indicator
    rpt_tp                 VARCHAR(3), -- report type
	transaction_pgi        VARCHAR(5), -- primary-general indicator
	image_num              VARCHAR(18), -- image number
	transaction_tp         VARCHAR(3), -- transaction type
	entity_tp              VARCHAR(3), -- entity type ("CAN" - candidate, "com" = committee, "IND" = individual, "ORG" = organization, "PAC" = political action committee, "PTY" = party organization)
	name                   VARCHAR(200), -- contributor/lender/transfer name
    city                   VARCHAR(30), -- Contributor’s city
    state                  CHAR(2), -- Contributor’s state
    zip_code               VARCHAR(9), -- Contributor’s ZIP code
    employer               VARCHAR(38), -- Contributor’s employer
    occupation             VARCHAR(38), -- Contributor’s occupation
    transaction_dt         DATE, -- Date of the contribution
    transaction_amt        NUMERIC(14,2), -- Contribution amount
	other_id               VARCHAR(9), -- other identification numberFor contributions from individuals this column is null. For contributions from candidates or other committees this column will contain that contributor's FEC ID.
    tran_id                VARCHAR(20) PRIMARY KEY, -- Unique transaction identifier
    file_num               INTEGER, -- unique report id
    memo_code              CHAR(1), -- Memo code indicator
    memo_text              VARCHAR(100), -- Additional memo text (if applicable)
	sub_id                 NUMERIC(19,0), -- FEC record number *unique row id
    election_cycle         INTEGER -- Election cycle (YYYY) for which the contribution was made
);
CREATE UNIQUE INDEX idx_individual_contributions_tran_id
ON individual_contributions (tran_id);