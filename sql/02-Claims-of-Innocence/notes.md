# Select Star SQL - Claims of Innocence

## Goal
Learning `Aggregrate Functions` and 
`COUNT ... CASE ...`

## Main ideas
- To aggregate means to combine multiple elements into a whole.
- `Aggregate functions` take multiple rows of data and combine them into one number.
- `COUNT(<column>)` returns the number of `non-null` rows in the column.
- `NULL` is the value of an empty entry and is different from empty string `''` and the integer `0`.
- To check if an entry is `NULL`, use `IS` and `IS NOT`.
- `CASE WHEN` block which acts as a big if-else statement.
``` sql
CASE
  WHEN <clause> THEN <result>
  WHEN <clause> THEN <result>
  ...
  ELSE <result>
END
```

## Fun things to know
- `COUNT(*)` counts rows as long as any one of their columns is non-null. 
``` sql
SELECT COUNT(*) FROM executions WHERE last_statement IS NULL
SELECT COUNT(CASE WHEN last_statement IS NULL THEN 1 ELSE NULL END) FROM executions
SELECT COUNT(*) - COUNT(last_statement) FROM executions
```
- The `WHERE` version had it filter down to a small table first before aggregating while in the other two, it had to look through the full table. In the `COUNT + CASE WHEN` version, it only had to go through once, while the `double COUNT` version made it go through twice.

## Examples
```sql
SELECT
  COUNT(CASE WHEN county='Harris' THEN 1
    ELSE NULL END),
  COUNT(CASE WHEN county='Bexar' THEN 1
    ELSE NULL END)
FROM executions