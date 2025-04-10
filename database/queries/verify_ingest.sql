select distinct election_cycle, count(*)
from candidate_committee_linkage
group by election_cycle;

select distinct election_cycle, count(*)
from candidate_master
group by election_cycle;

select distinct election_cycle, count(*)
from committee_master
group by election_cycle;

select distinct election_cycle, count(*)
from committee_to_candidate_cont_and_ind_exp
group by election_cycle;

select distinct election_cycle, count(*)
from committee_to_committee_trans
group by election_cycle;

select distinct election_cycle, count(*)
from individual_contributions
group by election_cycle;

select distinct election_cycle, count(*)
from operating_expenditures
group by election_cycle;
