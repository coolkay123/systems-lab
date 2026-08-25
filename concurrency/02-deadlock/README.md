# Lab 02: Deadlock

Two threads acquire the same locks in opposite orders. A barrier ensures that
each thread holds one lock before attempting the other. Timed acquisition lets
the program report the deadlock instead of hanging forever.

```sh
python3 concurrency/02-deadlock/deadlock.py
```

Then fix it by making both workers acquire locks in the same order. Explain
which deadlock condition that change removes.

