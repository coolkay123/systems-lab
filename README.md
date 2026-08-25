# Systems Lab

An executable lab notebook for learning backend and core systems engineering.
Each topic is learned by predicting, building, breaking, observing, and explaining.

## Learning path

1. [SQL and databases](sql/README.md)
2. [Concurrency and deadlocks](concurrency/README.md)
3. [DNS, TCP, TLS, and HTTP](networking/README.md)
4. [Distributed systems](distributed-systems/README.md)

## Start here

Requirements:

- Python 3.10 or newer
- Git
- A terminal

Run all current labs:

```sh
make labs
```

Or begin with the first SQL lab:

```sh
python3 sql/01-select-basics/run.py
```

## Progress

| Topic | Experiment | Status | Key lesson |
|---|---|---:|---|
| SQL | SELECT basics | Ready | Filter, sort, and aggregate a small dataset |
| Concurrency | Shared-counter race | Ready | Read-modify-write is not automatically safe |
| Concurrency | Two-lock deadlock | Ready | Circular lock acquisition prevents progress |
| Networking | Trace a URL | Planned | Follow DNS through the HTTP response |
| Distributed systems | Replicated key-value store | Planned | Study consistency under failure |

Update this table after finishing a lab. Keep the lesson to one sentence.

## The lab loop

For every experiment:

1. Write a prediction before running the code.
2. Run the smallest possible demonstration.
3. Break it deliberately.
4. Save useful output, logs, or traces.
5. Explain the result in your own words.
6. Change one variable and repeat.

Copy [`templates/experiment.md`](templates/experiment.md) when starting a lab.

## Repository rule

Documentation follows experimentation. Notes should explain something you ran,
observed, or tested—not merely repeat a book or tutorial.

