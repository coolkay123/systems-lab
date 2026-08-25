"""Demonstrate a lost update, then protect the critical section with a lock."""

import threading
import time


ITERATIONS = 100
THREADS = 4


def run_counter(use_lock: bool) -> int:
    counter = 0
    lock = threading.Lock()

    def increment() -> None:
        nonlocal counter
        for _ in range(ITERATIONS):
            if use_lock:
                with lock:
                    current = counter
                    time.sleep(0.0001)
                    counter = current + 1
            else:
                current = counter
                time.sleep(0.0001)
                counter = current + 1

    workers = [threading.Thread(target=increment) for _ in range(THREADS)]
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    return counter


def main() -> None:
    expected = ITERATIONS * THREADS
    broken = run_counter(use_lock=False)
    fixed = run_counter(use_lock=True)

    print(f"Expected:           {expected}")
    print(f"Without mutex:      {broken}")
    print(f"With mutex:         {fixed}")
    assert fixed == expected


if __name__ == "__main__":
    main()

