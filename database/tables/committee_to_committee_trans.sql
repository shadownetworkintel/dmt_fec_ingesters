CREATE TABLE committee_to_committee_trans (
    cmte_id          varchar(9),    -- Unique row identifier
	amndt_ind        char(1),       -- Amendment indicator
	rpt_tp           varchar(3),    -- report type
	transaction_pgi  varchar(5),    -- Primary/general indicator
	image_num        varchar(18),   -- image number
	transaction_tp   varchar(3),    -- transaction type
	entity_tp        varchar(3),    -- entity type
	name             varchar(200),  -- contributor/lender/transfer name
	city             varchar(30),   -- city
	state            varchar(2),    -- state
	zip_code         varchar(9),    -- zip code
	employer         varchar(38),   -- employer
	occupation       varchar(38),   -- occupation
	transaction_dt   date,          -- transaction date (MMDDYYYY)
	transaction_amt  numeric(14,2), -- transaction amount  
	other_id         varchar(9),    -- other identification number
	tran_id          varchar(32) PRIMARY KEY,   -- transaction id
	file_num         numeric(22,0), -- file number / report id
	memo_cd          varchar(1),    -- memo code
	memo_text        varchar(100),  -- memo text
	sub_id           numeric(19),   -- fec record number
	election_cycle   integer        -- election cycle
  );
