CREATE TABLE operating_expenditures (
	cmte_id           VARCHAR(9),    -- filer identification number
	amndt_ind         varchar(1),    -- amendment indicator
	rpt_yr            numeric(4,0),  -- report year
	rpt_tp            varchar(3),    -- report type
	image_num         varchar(18),   -- image number
	line_num          varchar(8),    -- fec form line number
	form_tp_cd        varchar(8),    -- image number
	sched_tp_cd       varchar(8),    -- image number
	name              varchar(200),  -- image number
	city              varchar(30),   -- image number
	state             varchar(2),    -- image number
	zip_code          varchar(9),    -- image number
	transaction_dt    date,          -- transaction date
	transaction_amt   numeric(14,2), -- transaction amount
	transaction_pgi   varchar(5),    -- primary/general indicator
	purpose           varchar(100),  -- purpose
	category          varchar(3),    -- disbursement category code
	category_desc     varchar(40),   -- disbursement category code description
	memo_cd           varchar(1),    -- memo code
	memo_text         varchar(100),  -- memo text
	entity_tp         varchar(3),    -- entity type
	sub_id            numeric(19,0), -- fec record number
	file_num          numeric(7,0),  -- file number/report id
	tran_id           varchar(32) PRIMARY KEY,   -- transaction id
	back_ref_tran_id  varchar(32),   -- back reference transaction id
	dummy_column      varchar(5),    -- extra (blank) column in the file. who knows!
	election_cycle    integer        -- election cycle (year)
);
