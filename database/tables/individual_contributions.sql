CREATE TABLE individual_contributions (
	cmte_id                VARCHAR(9),    -- filer identification number
	amndt_ind              VARCHAR(1),    -- Indicates if the report being filed is new (N), an amendment (A) to a previous report or a termination (T) report.
    rpt_tp                 VARCHAR(3),    -- report type see below
	transaction_pgi        VARCHAR(5),    -- primary-general indicator This code indicates the election for which the contribution was made. EYYYY (election plus election year) P = Primary, G = General, O = Other, C = Convention, R = Runoff, S = Special, E = Recount
	image_num              VARCHAR(18),   -- image number
	transaction_tp         VARCHAR(3),    -- Transaction types 10, 11, 15, 15C, 15E, 15I, 15T, 19, 22Y, 24I, 24T, 20Y and 21Y are included in the INDIV file. Beginning with 2016 transaction types 30, 30T, 31, 31T, 32, 32T, 40T, 40Y, 41T, 41Y, 42T and 42Y are included in the INDIV file. Beginning with 2020 transaction types 30E, 31E and 32E are also included in the INDIV file.
	entity_tp              VARCHAR(3),    -- entity type ("CAN" - candidate, "com" = committee, "IND" = individual, "ORG" = organization, "PAC" = political action committee, "PTY" = party organization)
	name                   VARCHAR(200),  -- contributor/lender/transfer name
    city                   VARCHAR(30),   -- Contributor’s city
    state                  CHAR(2),       -- Contributor’s state
    zip_code               VARCHAR(9),    -- Contributor’s ZIP code
    employer               VARCHAR(38),   -- Contributor’s employer
    occupation             VARCHAR(38),   -- Contributor’s occupation
    transaction_dt         DATE,          -- Date of the contribution
    transaction_amt        NUMERIC(14,2), -- Contribution amount
	other_id               VARCHAR(9),    -- other identification numberFor contributions from individuals this column is null. For contributions from candidates or other committees this column will contain that contributor's FEC ID.
    tran_id                VARCHAR(20),   -- Unique transaction identifier
    file_num               INTEGER,       -- unique report id
    memo_code              CHAR(1),       -- Memo code indicator
    memo_text              VARCHAR(100),  -- Additional memo text (if applicable)
	sub_id                 NUMERIC(19,0) PRIMARY KEY, -- FEC record number *unique row id
    election_cycle         INTEGER        -- Election cycle (YYYY) for which the contribution was made
);
CREATE INDEX idx_individual_contributions_tran_id
ON individual_contributions (tran_id);
CREATE INDEX idx_individual_contributions_cmte_id
ON individual_contributions (cmte_id);

-- The contributions by individuals file contains information for contributions given by individuals. 
-- The method used to include contributions in this file has changed over time.
-- 2015 - present: greater than $200
--    A contribution will be included if:
--    The contribution’s election cycle-to-date amount is over $200 for contributions to candidate committees
--    The contribution’s calendar year-to-date amount is over $200 for contributions to political action committees (PACs) and party committees.
-- 1989 - 2014: $200 and above
--    A contribution will be included if the reporting period amount is $200 or more.
-- 1975 - 1988: $500 and above
--    A contribution will be included if the reporting period amount is $500 or more.
-- The file contains information about the committee receiving the contribution, the report 
-- where the contribution is disclosed, the individual giving the contribution, the contribution’s 
-- date, amount, and additional information about the contribution (if provided).
-- The end-of-line (EOL) marker is line feed '\n' (LF, 0x0A, 10 in decimal).



-- Transaction type	Transaction type description
-- 10	Contribution to Independent Expenditure-Only Committees (Super PACs), Political Committees with non-contribution accounts (Hybrid PACs) and nonfederal party "soft money" accounts (1991-2002) from a person (individual, partnership, limited liability company, corporation, labor organization, or any other organization or group of persons)
-- 10J	Memo - Recipient committee's percentage of nonfederal receipt from a person (individual, partnership, limited liability company, corporation, labor organization, or any other organization or group of persons)
-- 11	Native American Tribe contribution
-- 11J	Memo - Recipient committee's percentage of contribution from Native American Tribe given to joint fundraising committee
-- 12	Nonfederal other receipt - Levin Account (Line 2)
-- 13	Inaugural donation accepted
-- 15	Contribution to political committees (other than Super PACs and Hybrid PACs) from an individual, partnership or limited liability company
-- 15C	Contribution from candidate
-- 15E	Earmarked contributions to political committees (other than Super PACs and Hybrid PACs) from an individual, partnership or limited liability company
-- 15F	Loans forgiven by candidate
-- 15I	Earmarked contribution from an individual, partnership or limited liability company received by intermediary committee and passed on in the form of contributor's check (intermediary in)
-- 15J	Memo - Recipient committee's percentage of contribution from an individual, partnership or limited liability company given to joint fundraising committee
-- 15K	Contribution received from registered filer disclosed on authorized committee report
-- 15T	Earmarked contribution from an individual, partnership or limited liability company received by intermediary committee and entered into intermediary's treasury (intermediary treasury in)
-- 15Z	In-kind contribution received from registered filer
-- 16C	Loan received from the candidate
-- 16F	Loan received from bank
-- 16G	Loan from individual
-- 16H	Loan from registered filers
-- 16J	Loan repayment from individual
-- 16K	Loan repayment from from registered filer
-- 16L	Loan repayment received from unregistered entity
-- 16R	Loan received from registered filers
-- 16U	Loan received from unregistered entity
-- 17R	Contribution refund received from registered entity
-- 17U	Refund/Rebate/Return received from unregistered entity
-- 17Y	Refund/Rebate/Return from individual or corporation
-- 17Z	Refund/Rebate/Return from candidate or committee
-- 18G	Transfer in from affiliated committee
-- 18H	Honorarium received
-- 18J	Memo - Recipient committee's percentage of contribution from a registered committee given to joint fundraising committee
-- 18K	Contribution received from registered filer
-- 18L	Bundled contribution
-- 18U	Contribution received from unregistered committee
-- 19	Electioneering communication donation received
-- 19J	Memo - Recipient committee's percentage of Electioneering Communication donation given to joint fundraising committee
-- 20	Nonfederal disbursement - nonfederal party "soft money" accounts (1991-2002)
-- 20A	Nonfederal disbursement - Levin Account (Line 4A) Voter Registration
-- 20B	Nonfederal Disbursement - Levin Account (Line 4B) Voter Identification
-- 20C	Loan repayment made to candidate
-- 20D	Nonfederal disbursement - Levin Account (Line 4D) Generic Campaign
-- 20F	Loan repayment made to banks
-- 20G	Loan repayment made to individual
-- 20R	Loan repayment made to registered filer
-- 20V	Nonfederal disbursement - Levin Account (Line 4C) Get Out The Vote
-- 20Y	Nonfederal refund
-- 21Y	Native American Tribe refund
-- 22G	Loan to individual
-- 22H	Loan to candidate or committee
-- 22J	Loan repayment to individual
-- 22K	Loan repayment to candidate or committee
-- 22L	Loan repayment to bank
-- 22R	Contribution refund to unregistered entity
-- 22U	Loan repaid to unregistered entity
-- 22X	Loan made to unregistered entity
-- 22Y	Contribution refund to an individual, partnership or limited liability company
-- 22Z	Contribution refund to candidate or committee
-- 23Y	Inaugural donation refund
-- 24A	Independent expenditure opposing election of candidate
-- 24C	Coordinated party expenditure
-- 24E	Independent expenditure advocating election of candidate
-- 24F	Communication cost for candidate (only for Form 7 filer)
-- 24G	Transfer out to affiliated committee
-- 24H	Honorarium to candidate
-- 24I	Earmarked contributor's check passed on by intermediary committee to intended recipient (intermediary out)
-- 24K	Contribution made to nonaffiliated committee
-- 24N	Communication cost against candidate (only for Form 7 filer)
-- 24P	Contribution made to possible federal candidate including in-kind contributions
-- 24R	Election recount disbursement
-- 24T	Earmarked contribution passed to intended recipient from intermediary's treasury (treasury out)
-- 24U	Contribution made to unregistered entity
-- 24Z	In-kind contribution made to registered filer
-- 28L	Refund of bundled contribution
-- 29	Electioneering Communication disbursement or obligation
-- 30	Convention Account receipt from an individual, partnership or limited liability company
-- 30E	Convention Account - Earmarked receipt
-- 30F	Convention Account - Memo - Recipient committee's percentage of contributions from a registered committee given to joint fundraising committee
-- 30G	Convention Account - transfer in from affiliated committee
-- 30J	Convention Account - Memo - Recipient committee's percentage of contributions from an individual, partnership or limited liability company given to joint fundraising committee
-- 30K	Convention Account receipt from registered filer
-- 30T	Convention Account receipt from Native American Tribe
-- 31	Headquarters Account receipt from an individual, partnership or limited liability company
-- 31E	Headquarters Account - Earmarked receipt
-- 31F	Headquarters Account - Memo - Recipient committee's percentage of contributions from a registered committee given to joint fundraising committee
-- 31G	Headquarters Account - transfer in from affiliated committee
-- 31J	Headquarters Account - Memo - Recipient committee's percentage of contributions from an individual, partnership or limited liability company given to joint fundraising committee
-- 31K	Headquarters Account receipt from registered filer
-- 31T	Headquarters Account receipt from Native American Tribe
-- 32	Recount Account receipt from an individual, partnership or limited liability company
-- 32E	Recount Account - Earmarked receipt
-- 32F	Recount Account - Memo - Recipient committee's percentage of contributions from a registered committee given to joint fundraising committee
-- 32G	Recount Account - transfer in from affiliated committee
-- 32J	Recount Account - Memo - Recipient committee's percentage of contributions from an individual, partnership or limited liability company given to joint fundraising committee
-- 32K	Recount Account receipt from registered filer
-- 32T	Recount Account receipt from Native American Tribe
-- 40	Convention Account disbursement
-- 40Y	Convention Account refund to an individual, partnership or limited liability company
-- 40T	Convention Account refund to Native American Tribe
-- 40Z	Convention Account refund to registered filer
-- 41	Headquarters Account disbursement
-- 41Y	Headquarters Account refund to an individual, partnership or limited liability company
-- 41T	Headquarters Account refund to Native American Tribe
-- 41Z	Headquarters Account refund to registered filer
-- 42	Recount Account disbursement
-- 42Y	Recount Account refund to an individual, partnership or limited liability company
-- 42T	Recount Account refund to Native American Tribe
-- 42Z	Recount Account refund to registered filer

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