# Select Star SQL - Beazley

## Goal
Learn the basic shape of a SQL query:
`SELECT ... FROM ... WHERE ... LIMIT ... LIKE ...`

## Main ideas
- `SELECT` chooses columns to return.
- `FROM` chooses the table.
- `WHERE` filters rows by a condition (boolean statement).
- `LIMIT` limits the number of rows shown.
- `LIKE` allows us to use wildcards such as `%` and `_` to match various characters.
- SQL keywords are usually written in uppercase for readability.
- Comments can be written with `--` or `/* ... */`.
- A common trick is to multiply one number by 1.0 to convert it into a decimal.
- SQL gives most precedence to `NOT` and then `AND` and finally `OR`.

## Fun things to know
```sql
SELECT 25 / 2 -- would return 12 and not 12.5
-- This is because SQL is doing integer division
-- To do decimal division, at least one of the operands must be a decimal, for instance 51.0 / 2

SELECT first_name from executions where last_name LIKE '%an' -- chooses last name ending with an while '_an' chooses single character preceeding 'an'
```

## Syntax I should remember
```sql
SELECT <columns>
FROM <table>
WHERE <condition>
LIMIT <integer>
WHERE <column> LIKE <pattern-match>;