# Lab 01: Race condition

Two threads repeatedly perform a forced read-pause-write operation on one shared
counter. The pause makes an otherwise timing-dependent lost update easy to see.

```sh
python3 concurrency/01-race-condition/race.py
```

Questions:

1. Why can the broken result be less than the expected result?
2. Which part is the critical section?
3. Why must the lock cover both the read and the write?

