CREATE TABLE operating_expenditures (
	cmte_id           VARCHAR(9),    -- filer identification number
	amndt_ind         varchar(1),    -- Indicates if the report being filed is new (N), an amendment (A) to a previous report, or a termination (T) report.
	rpt_yr            numeric(4,0),  -- report year
	rpt_tp            varchar(3),    -- report type see below
	image_num         varchar(18),   -- image number
	line_num          varchar(8),    -- fec form line number
	form_tp_cd        varchar(8),    -- Indicates FEC Form
	sched_tp_cd       varchar(8),    -- Schedule B - Itemized disbursements
	name              varchar(200),  
	city              varchar(30),   
	state             varchar(2),    
	zip_code          varchar(9),    
	transaction_dt    date,          -- transaction date
	transaction_amt   numeric(14,2), -- transaction amount
	transaction_pgi   varchar(5),    -- primary/general indicator
	purpose           varchar(100),  -- purpose
	category          varchar(3),    -- disbursement category code 001-012 and 101-107
	category_desc     varchar(40),   -- disbursement category code description see below
	memo_cd           varchar(1),    -- X' indicates that the amount of the transaction is not incorporated into the total figure disclosed on the detailed summary page of the committee’s report. 'X' may also indicate that the amount was received as part of a joint fundraising transfer or other lump sum contribution required to be attributed to individual contributors. Memo items may be used to denote that a transaction was previously reported or in the case of an independent expenditure, that the amount represents activity that has occurred but has not yet been paid by the committee. When using the bulk data file these memo items should be included in your analysis.
	memo_text         varchar(100),  -- memo text
	entity_tp         varchar(3),    -- entity type ONLY VALID FOR ELECTRONIC FILINGS received after April 2002. CAN = CandidateCCM = Candidate committee, COM = Committee, IND = Individual (a person), ORG = Organization (not a committee and not a person), PAC = Political action committee, PTY = Party organization
	sub_id            numeric(19,0) PRIMARY KEY, -- fec record number
	file_num          numeric(7,0),  -- unique report id 
	tran_id           varchar(32),   -- transaction id ONLY VALID FOR ELECTRONIC FILINGS. A unique identifier associated with each itemization or transaction appearing in an FEC electronic file. A transaction ID is unique for a specific committee for a specific report. In other words, if committee, C1, files a Q3 New with transaction SA123 and then files 3 amendments to the Q3 transaction SA123 will be identified by transaction ID SA123 in all 4 filings.
	back_ref_tran_id  varchar(32),   -- back reference transaction id ONLY VALID FOR ELECTRONIC FILINGS. Used to associate one transaction with another transaction in the same report (using file number, transaction ID and back reference transaction ID). For example, a credit card payment and the subitemization of specific purchases. The back reference transaction ID of the specific purchases will equal the transaction ID of the payment to the credit card company.
	dummy_column      varchar(5),    -- extra (blank) column in the file. who knows!
	election_cycle    integer        -- election cycle (year)
);
CREATE INDEX idx_operating_expenditures_tran_id
ON operating_expenditures (tran_id);
CREATE INDEX idx_operating_expenditures_cmte_id
ON operating_expenditures (cmte_id);

-- The operating expenditures file contains information about disbursements disclosed on FEC reports, 
-- including operating expenditures reported on:
-- Form 3, Line 17 for House and Senate committees
-- Form 3P, Line 23 for Presidential committees
-- Form 3X, Lines 21(a)(i), 21(a)(ii), and 21(b) for PAC and Party committees
-- For electronic filing committees, operating expenditures are available from the 2004 election cycle
-- to the present.
-- For paper filing committees, operating expenditures are available starting October 2005 through 
-- the present.
-- The file contains information about the committee making the disbursement, the report where 
-- the operating expenditure is disclosed, the entity receiving the disbursement, the disbursement’s 
-- date, amount, purpose, and additional information about the operating expenditure (if provided).
-- The end-of-line (EOL) marker is line feed '\n' (LF, 0x0A, 10 in decimal).

-- The list of report type codes contains the following information:
-- Report type code	Report type	explanation
-- 12C	Pre-convention	For states using conventions to select candidates. Report covers through 20 days before the convention
-- 12G	Pre-general	Report covers through 20 days before the general election - due 12 days before the election
-- 12P	Pre-primary	Report covers through 20 days before the primary- due 12 days before the election
-- 12R	Pre-Runoff	Report covers through 20 days before the run-off- due 12 days before the election
-- 12S	Pre-special	Report covers through 20 days before the special election - due 12 days before the election
-- 30D	Post-Election	Report covers from 19 days before the election through 20 days after - due 30 days after the election
-- 30G	Post-general	Report covers from 19 days before the election through 20 days after. - due 30 days after the election
-- 30P	Post-primary	Report covers from 19 days before the election through 20 days after. - due 30 days after the election
-- 30R	Post-runoff	Report covers from 19 days before the election through 20 days after. - due 30 days after the election
-- 30S	Post-special	Report covers from 19 days before the election through 20 days after. - due 30 days after the election
-- 60D	Post-convention	Report filed by national party convention and host committees disclosing their convention expenses, due 60 days after the convention
-- ADJ	Comprehensive adjusted amendment	Adjustment of a comprehensive amendment - coverage is variable
-- CA	Comprehensive amendment	Amendment modifying information from two or more original reports - coverage is variable
-- M10	October monthly	Covers September - due October 20
-- M11	November monthly	Covers October - due November 20
-- M12	December monthly	Covers November - due December 20
-- M2	February monthly	Covers January - due February 20
-- M3	March monthly	Covers February - due March 20
-- M4	April monthly	Covers March - due April 20
-- M5	May monthly	Covers April - due May 20
-- M6	June monthly	Covers May - due June 20
-- M7	July monthly	Covers June - due July 20
-- M8	August monthly	Covers July - due August 20
-- M9	September monthly	Covers August - due September 20
-- MY	Mid-year	Covers January 1 through June 30 - due July 31 Permissible in non-election years for PACs and party committees normally filing Quarterly reports. (Note that since 2003 campaign committees must file quarterly in all years.)
-- Q1	April quarterly	Covers January 1 through March 31 - due April 15
-- Q2	July quarterly	Covers April 1 through June 30 - due July 15
-- Q3	October quarterly	Covers July 1 through September 30 - due October 15
-- TER	Termination	Final report submitted by a committee - coverage is variable
-- YE	Year end	Covers from the end of the last quarterly or mid-year report through December 31 - due January 31
-- 90S	Post inaugural supplement	 
-- 90D	Post inaugural	Filing of Presidential inaugural committee - due 90 days after the Inauguration
-- 48H	48-hour	Report of specific contribution of $1,000 or more made to a campaign within 20 days of an election. Alternatively, once a PAC or party or other person has made independent expenditures exceeding $10,000 in a race these and future independent expenditures must be reported. Due within 48 hours of receiving the contribution or public distribution of the independent expenditure. 48 hour timing for independent expenditures applies prior to 20 days before the election.
-- 24H	24-hour	Within 20 days of an election once a PAC or party or other person has made independent expenditures exceeding $1,000 in a race these and future independent expenditures must be reported. Due within 24 hours of the public distribution of the independent expenditure.

-- The list of disbursement category codes contains the following information:
-- Disbursment category code	Code description
-- Disbursement category codes for non-presidential filers
-- 001	Administrative/salary/overhead expenses (e.g., rent, staff salaries, postage, office supplies, equipment, furniture, ballot access fees, petition drives, party fees and legal and accounting expenses)
-- 002	Travel expenses - including travel reimbursement expenses (e.g., costs of commercial carrier tickets; reimbursements for use of private vehicles, advance payments for use of corporate aircraft; lodging and meal expenses incurred during travel)
-- 003	Solicitation and fundraising expenses (e.g., costs for direct mail solicitations and fundraising events including printing, mailing lists, consultant fees, call lists, invitations, catering costs and room rental)
-- 004	Advertising expenses -including general public political advertising (e.g., purchases of radio/television broadcast/cable time, print advertisements and related production costs)
-- 005	Polling expenses
-- 006	Campaign materials (e.g., buttons, bumper stickers, brochures, mass mailings, pens, posters, balloons)
-- 007	Campaign event expenses (e.g., costs associated with candidate appearances, campaign rallies, town meetings, phone banks, including catering costs, door to door get-out-the-vote efforts and driving voters to the polls)
-- 008	Transfers (e.g., to other authorized committees of the same candidate)
-- 009	Loan repayments (e.g., repayments of loans made/guaranteed by the candidate or other person)
-- 010	Refunds of contributions (e.g., contribution refunds to individuals/ persons, political party committees or other political committees)
-- 011	Political contributions (e.g., contributions to other federal candidates and committees, donations to nonfederal candidates and committees)
-- 012	Donations (e.g., donations to charitable or civic organizations
-- Disbursement category codes for presidential filers
-- 101	Expenses that are not allocable
-- 102	Media expenditures
-- 103	Expenditures for mass mailings and other campaign materials (e.g., buttons, bumper stickers, brochures, mass mailings, pens, posters, balloons)
-- 104	Overhead expenditures of state offices and their facilities (e.g., rent, staff salaries, postage, office supplies, equipment, furniture, ballot access fees, petition drives, party fees and legal and accounting expenses)
-- 105	Expenditures for special telephone programs
-- 106	Public opinion poll expenditures
-- 107	Fundraising expenditures (e.g., costs for direct mail solicitations & fundraising events including printing, mailing lists, consultant fees, call lists, invitations, catering costs and room rental)