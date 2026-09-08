# Select Star SQL - Execution Hiatuses

## Goal
Learning `JOIN ...` blocks, types of join.

## Main ideas
- The `JOIN` block takes the form of `<table1> JOIN <table2> ON <clause>`.

- The `JOIN` command defaults to performing what is called an `“inner join”` in which `unmatched rows are dropped`.

- To preserve all the rows of the left table, we use a `LEFT JOIN` in place of the vanilla JOIN. The `empty parts of the row are left alone, which means they evaluate to NULL`.

- The `RIGHT JOIN` can be used to `preserve unmatched rows in the right table`, and the `OUTER JOIN` can be used to `preserve unmatched rows in both`.

- The `date()` function returns the date as text in this format: `YYYY-MM-DD`.

- The `time()` function returns the time as text in formatted as `HH:MM:SS` or as HH:MM:SS.SSS if the subsec modifier is used.

- The `datetime()` function returns the date and time formatted as `YYYY-MM-DD HH:MM:SS` or as YYYY-MM-DD HH:MM:SS.SSS if the subsec modifier is used.

- The `julianday()` function returns the Julian day - `the fractional number of days since noon in Greenwich on November 24, 4714 B.C.` (Proleptic Gregorian calendar).

- The `unixepoch()` function returns a unix timestamp - the `number of seconds since 1970-01-01 00:00:00 UTC`. The unixepoch() function normally returns an integer number of seconds, but with the optional subsec modifier it will return a floating point number which is the fractional number of seconds.

- The `strftime()` function returns the date formatted according to the `format string specified as the first argument`. The format string supports the most common substitutions found in the strftime() function from the standard C library plus two new substitutions, %f and %J.


``` sql
SELECT
  last_ex_date AS start,
  ex_date AS end,
  ex_date - last_ex_date AS day_difference
FROM executions
JOIN previous
  ON executions.ex_number = previous.ex_number
ORDER BY day_difference DESC
LIMIT 10
```

- `previous` is derived from `executions`, so we’re effectively joining executions to itself. This is called a `“self join”` and is a powerful technique for `allowing rows to get information from other parts of the same table`.
 ```sql
 SELECT
  last_ex_date AS start,
  ex_date AS end,
  JULIANDAY(ex_date) - JULIANDAY(last_ex_date) AS day_difference
FROM executions
JOIN (
    SELECT
      ex_number + 1 AS ex_number,
      ex_date AS last_ex_date
    FROM executions
  ) previous
  ON executions.ex_number = previous.ex_number
ORDER BY day_difference DESC
LIMIT 10

select
  last_ex_date AS start,
  ex_date AS end,
  JULIANDAY(ex_date) - JULIANDAY(last_ex_date) AS day_difference
FROM executions join executions previous 
on executions.ex_number = previous.ex_number + 1
order by day_difference desc limit 10
 ```

## Fun things to know
```sql
tableA JOIN tableB ON 0 returns 0 rows.
tableA OUTER JOIN tableB ON 1 returns 15 rows
```