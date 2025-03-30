select distinct recipient
, first_name || ' ' || last_name as candidate
, donor, party
, office
, district
, d.city
, d.state
, d.zip_code
, amount
, date 
from ky_candidates c
full outer join kref_donations d on c.first_name || ' ' || c.last_name = d.recipient
group by recipient