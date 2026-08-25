.PHONY: help labs sql race deadlock

help:
	@echo "make sql       Run the starter SQL lab"
	@echo "make race      Run the race-condition lab"
	@echo "make deadlock  Run the deadlock-detection lab"
	@echo "make labs      Run every current lab"

sql:
	python3 sql/01-select-basics/run.py

race:
	python3 concurrency/01-race-condition/race.py

deadlock:
	python3 concurrency/02-deadlock/deadlock.py

labs: sql race deadlock

