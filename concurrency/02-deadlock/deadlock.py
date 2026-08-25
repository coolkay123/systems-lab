"""Create a circular wait and detect it with timed lock acquisition."""

import threading


first_lock = threading.Lock()
second_lock = threading.Lock()
both_holding_one_lock = threading.Barrier(2)


def worker(name: str, held: threading.Lock, wanted: threading.Lock) -> None:
    with held:
        print(f"{name}: acquired its first lock")
        both_holding_one_lock.wait()
        print(f"{name}: waiting for its second lock")
        acquired = wanted.acquire(timeout=0.5)
        if acquired:
            try:
                print(f"{name}: acquired both locks")
            finally:
                wanted.release()
        else:
            print(f"{name}: timeout detected a circular wait")


def main() -> None:
    workers = [
        threading.Thread(target=worker, args=("worker-a", first_lock, second_lock)),
        threading.Thread(target=worker, args=("worker-b", second_lock, first_lock)),
    ]
    for thread in workers:
        thread.start()
    for thread in workers:
        thread.join()
    print("Program recovered because lock acquisition used a timeout.")


if __name__ == "__main__":
    main()

