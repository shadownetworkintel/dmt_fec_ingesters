CREATE TABLE fec_house_senate_current_campaigns (
    cand_id                VARCHAR(9) PRIMARY KEY, -- candidate identifier
    cand_name              VARCHAR(200), -- Candidate’s full name
	cand_ici               CHAR(1), -- incumbent challenger status
	pty_cd                 CHAR(1), -- party code
	cand_pty_affiliation   VARCHAR(3), -- party affiliation
	ttl_receipts           NUMERIC(14,2), -- total receipts
	trans_from_auth        NUMERIC(14,2), -- transfers from authorized committees
	ttl_disb               NUMERIC(14,2), -- total disbursements
	trans_to_auth          NUMERIC(14,2), -- transfers to authorized committees
	coh_bop                NUMERIC(14,2), -- beginning cash
	coh_cop                NUMERIC(14,2), -- ending cash
	cand_contrib           NUMERIC(14,2), -- contributions from candidate
	cand_loans             NUMERIC(14,2), -- loans from candidate
	other_loans            NUMERIC(14,2), -- other loans
	cand_loan_repay        NUMERIC(14,2), -- candidate loan repayments
	other_loan_repay       NUMERIC(14,2), -- other loan repayments
	debts_owed_by          NUMERIC(14,2), -- debts owed by
	ttl_indiv_contrib      NUMERIC(14,2), -- total individual contributions
	cand_office_st         VARCHAR(2), -- candidate state
	cand_office_district   VARCHAR(2), -- candidate district
	spec_election          VARCHAR(1), -- special election status
	prim_election          VARCHAR(1), -- primary election status
	run_election           VARCHAR(1), -- runoff election status
	gen_election           VARCHAR(1), -- general election status
	gen_election_percent   NUMERIC(7,2), -- general election percentage
	other_pol_cmte_contrib NUMERIC(14,2), -- contributions from other political committees
	pol_pty_contrib        NUMERIC(14,2), -- contributions from party committees
	cvg_end_dt             VARCHAR(10), -- coverage end date
	indiv_refunds          NUMERIC(14,2), -- refunds to individuals
	cmte_refunds           NUMERIC(14,2) -- refunds to committees
);
