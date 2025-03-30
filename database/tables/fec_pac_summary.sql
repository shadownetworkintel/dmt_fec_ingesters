CREATE TABLE fec_pac_summary (
    cmte_id                 VARCHAR(9) PRIMARY KEY, -- Unique identifier for the committee
    cmte_nm                 VARCHAR(200) NOT NULL, -- Name of the PAC or party committee
    cmte_tp                 CHAR(1),       -- PAC or party committee type codes
    cmte_dsgn               CHAR(1),       -- Designation codes
    cmte_filing_freq        char(1),       -- committee filing frequency
	ttl_receipts            NUMERIC(12,2), -- Total receipts
  	trans_from_aff          NUMERIC(14,2), -- transfers from affiliates
	indv_contrib            NUMERIC(14,2), -- contributions from individuals
	other_pol_cmte_contrib  NUMERIC(14,2), -- contributions from other political committees
	cand_contrib            NUMERIC(14,2), -- contributions from candidate
	cand_loans              NUMERIC(14,2), -- candidate loans
	ttl_loans_received      NUMERIC(14,2), -- total loans received
	ttl_disb                NUMERIC(14,2), -- total disbursements
	tranf_to_aff            NUMERIC(14,2), -- transfers to affiliates
	indv_refunds            NUMERIC(14,2), -- refunds to individuals
	other_pol_cmte_refunds  NUMERIC(14,2), -- refunds to other political committees
	cand_loan_repay         NUMERIC(14,2), -- candidate loan repayments
	loan_repay              NUMERIC(14,2), -- loan repayments
	coh_bop                 NUMERIC(14,2), -- cash beginning of period
	coh_cop                 NUMERIC(14,2), -- cash close of period
	depts_owed_by           NUMERIC(14,2), -- debts owed by
	nonfed_trans_received   NUMERIC(14,2), -- nonfederal transfers received
	contrib_to_other_cmte   NUMERIC(14,2), -- contributions to other committees
	ind_exp                 NUMERIC(14,2), -- independent expenditures
	pty_coord_exp           NUMERIC(14,2), -- party coordinated expenditures
	nonfed_share_exp        NUMERIC(14,2), -- nonfederal share expenditures
	cvg_end_dt              VARCHAR(14)    -- through date
);
