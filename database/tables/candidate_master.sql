-- FEC Candidate Master Table
-- This table contains information about candidates running for federal office in the United States.
CREATE TABLE candidate_master (
    cand_id                 VARCHAR(9) PRIMARY KEY, -- Unique identifier for candidates
    cand_name               VARCHAR(200),           -- Candidate’s full name
    cand_pty_affiliation    VARCHAR(3),             -- Three-character party code see below
    cand_election_yr        INTEGER,                -- Year of election
    cand_office_st          CHAR(2),                -- Two-character state abbreviation House = state of race, President = US, Senate = state of race
    cand_office             CHAR(1),                -- House (H), Senate (S), President (P)
    cand_office_district    VARCHAR(2),             -- Congressional district (House races only, "00" for Senate)
    cand_ici                CHAR(1),                -- Incumbent (I), Challenger (C), Open (O)
    cand_status             CHAR(1),                -- Current (C), Future (F), Not running (N), Prior (P)
    cand_pcc                VARCHAR(9),             -- Linked principal campaign committee ID
    cand_st1                TEXT,                   -- Candidate’s mailing address
    cand_st2                TEXT,                   -- Candidate’s mailing address
    cand_city               VARCHAR(100), 
    cand_st                 CHAR(2),
    cand_zip                VARCHAR(10),
    election_cycle          INTEGER
);
CREATE UNIQUE INDEX idx_candidate_master_cand_id
ON candidate_master (cand_id);

-- The candidate master file contains basic information for each candidate, including:
-- Candidates who have filed a Statement of Candidacy (Form 2) for the upcoming election
-- Candidates who have active campaign committees without regard to election year
-- Candidates who are referenced as a part of a draft committee or a nonconnected committee 
-- that registers as supporting or opposing a particular candidate
-- The file shows the candidate's identification number, candidate’s name, party affiliation, 
-- election year, office state, office sought, district, incumbent/challenger status, status 
-- as a candidate, name of the candidate’s principal campaign committee, and address. 
-- The end-of-line (EOL) marker is line feed '\n' (LF, 0x0A, 10 in decimal).

-- Party code descriptions
-- Party code	Party code description	Notes
-- ACE	Ace Party	
-- AKI	Alaskan Independence Party	
-- AIC	American Independent Conservative	
-- AIP	American Independent Party	
-- AMP	American Party	
-- APF	American People's Freedom Party	
-- AE	Americans Elect	
-- CIT	Citizens' Party	
-- CMD	Commandments Party	
-- CMP	Commonwealth Party of the U.S.	
-- COM	Communist Party	
-- CNC	Concerned Citizens Party Of Connecticut	
-- CRV	Conservative Party	
-- CON	Constitution Party	
-- CST	Constitutional	
-- COU	Country	
-- DCG	D.C. Statehood Green Party	
-- DNL	Democratic -Nonpartisan League	
-- DEM	Democratic Party	
-- D/C	Democratic/Conservative	
-- DFL	Democratic-Farmer-Labor	
-- DGR	Desert Green Party	
-- FED	Federalist	
-- FLP	Freedom Labor Party	
-- FRE	Freedom Party	
-- GWP	George Wallace Party	
-- GRT	Grassroots	
-- GRE	Green Party	
-- GR	Green-Rainbow	
-- HRP	Human Rights Party	
-- IDP	Independence Party	
-- IND	Independent	
-- IAP	Independent American Party	
-- ICD	Independent Conservative Democratic	
-- IGR	Independent Green	
-- IP	Independent Party	
-- IDE	Independent Party of Delaware	
-- IGD	Industrial Government Party	
-- JCN	Jewish/Christian National	
-- JUS	Justice Party	
-- LRU	La Raza Unida	Also see RUP
-- LBR	Labor Party	Also see LAB
-- LFT	Less Federal Taxes	
-- LBL	Liberal Party	
-- LIB	Libertarian Party	
-- LBU	Liberty Union Party	
-- MTP	Mountain Party	
-- NDP	National Democratic Party	
-- NLP	Natural Law Party	
-- NA	New Alliance	
-- NJC	New Jersey Conservative Party	
-- NPP	New Progressive Party	
-- NPA	No Party Affiliation	
-- NOP	No Party Preference	Commonly used in CA & WA
-- NNE	None	
-- N	Nonpartisan	
-- NON	Non-Party	
-- OE	One Earth Party	
-- OTH	Other	
-- PG	Pacific Green	
-- PSL	Party for Socialism and Liberation	
-- PAF	Peace And Freedom	Also see PFP
-- PFP	Peace And Freedom Party	Also see PAF
-- PFD	Peace Freedom Party	
-- POP	People Over Politics	
-- PPY	People's Party	
-- PCH	Personal Choice Party	
-- PPD	Popular Democratic Party	
-- PRO	Progressive Party	
-- NAP	Prohibition Party	
-- PRI	Puerto Rican Independence Party	
-- RUP	Raza Unida Party	Also see LRU
-- REF	Reform Party	
-- REP	Republican Party	
-- RES	Resource Party	
-- RTL	Right To Life	
-- SEP	Socialist Equality Party	
-- SLP	Socialist Labor Party	
-- SUS	Socialist Party	
-- SOC	Socialist Party U.S.A.	
-- SWP	Socialist Workers Party	
-- TX	Taxpayers	
-- TWR	Taxpayers Without Representation	
-- TEA	Tea Party	
-- THD	Theo-Democratic	
-- LAB	U.S. Labor Party	Also see LBR
-- USP	U.S. People's Party	
-- UST	U.S. Taxpayers Party	
-- UN	Unaffiliated	
-- UC	United Citizen	
-- UNI	United Party	
-- UNK	Unknown	
-- VET	Veterans Party	
-- WTP	We the People	
-- W	Write-In