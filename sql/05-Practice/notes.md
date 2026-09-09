### Practice
- `With ...  as` clause in sql is used to define a commone table expression (CTE)


- Now find the most networked senator from each state.
If multiple senators tie for top, show both. Return columns corresponding to state, senator and mutual cosponsorship count.
```sql
with mutual_counts as (
	select senator, state, count(*)
  as mutual_count
  from (
  	select distinct c1.sponsor_name as senator,
	c1.sponsor_state as state,
	c2.sponsor_name as senator2
	from cosponsors c1 
	join cosponsors c2
	on c1.sponsor_name = c2.cosponsor_name
	and c1.cosponsor_name = c2.sponsor_name
  )
  group by senator, state
),
state_max as (
	select state, max(mutual_count) as max_mutual_count
  from mutual_counts
  group by state
)
select 
  mutual_counts.state,
  mutual_counts.senator,
  mutual_counts.mutual_count
from mutual_counts
join state_max 
on mutual_counts.state = state_max.state
and mutual_counts.mutual_count = state_max.max_mutual_count
```
- Find the senators who cosponsored but didn't sponsor bills
```sql
SELECT DISTINCT c1.cosponsor_name
FROM cosponsors c1
LEFT JOIN cosponsors c2
 ON c1.cosponsor_name = c2.sponsor_name
 -- This join identifies cosponsors
 -- who have sponsored bills
WHERE c2.sponsor_name IS NULL
-- LEFT JOIN + NULL is a standard trick for excluding
-- rows. It's more efficient than WHERE ... NOT IN.
```