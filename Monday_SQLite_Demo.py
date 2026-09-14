import sqlite3

DB_NAME = "repair_shop.db"


def create_table():
    """Create the CUSTOMER table if it does not already exist."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS customer (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                phone TEXT,
                email TEXT
            )
        """)


def add_customer(name, phone, email):
    """Insert one customer into the database."""
    with sqlite3.connect(DB_NAME) as conn:
        conn.execute(
            """
            INSERT INTO customer (name, phone, email)
            VALUES (?, ?, ?)
            """,
            (name, phone, email)
        )


def show_customers():
    """Read and display all customers."""
    with sqlite3.connect(DB_NAME) as conn:
        rows = conn.execute(
            """
            SELECT customer_id, name, phone, email
            FROM customer
            ORDER BY customer_id
            """
        ).fetchall()

    print("\nCUSTOMERS")
    print("---------")

    if not rows:
        print("No customers found.")
        return

    for row in rows:
        print(row)


def main():
    create_table()

    print("CELL PHONE REPAIR SHOP - CUSTOMER DATABASE")
    print("------------------------------------------")

    name = input("Customer name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    add_customer(name, phone, email)
    print("\nCustomer added.")

    show_customers()


if __name__ == "__main__":
    main()
