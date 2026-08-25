"""Create an in-memory SQLite database and execute the lab's queries."""

from pathlib import Path
import sqlite3


LAB_DIR = Path(__file__).resolve().parent


def statements(sql: str):
    """Yield complete SQL statements while ignoring comments and blank lines."""
    buffer = ""
    for line in sql.splitlines():
        if line.lstrip().startswith("--") or not line.strip():
            continue
        buffer += line + "\n"
        if sqlite3.complete_statement(buffer):
            yield buffer.strip()
            buffer = ""
    if buffer.strip():
        raise ValueError("queries.sql ends with an incomplete statement")


def main() -> None:
    connection = sqlite3.connect(":memory:")
    connection.executescript((LAB_DIR / "schema.sql").read_text())

    query_text = (LAB_DIR / "queries.sql").read_text()
    for number, query in enumerate(statements(query_text), start=1):
        cursor = connection.execute(query)
        headings = [column[0] for column in cursor.description]
        rows = cursor.fetchall()

        print(f"\nQuery {number}\n{'-' * 40}")
        print(" | ".join(headings))
        for row in rows:
            print(" | ".join(str(value) for value in row))


if __name__ == "__main__":
    main()

