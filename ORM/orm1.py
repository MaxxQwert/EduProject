from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String, Boolean

engine = create_engine("postgresql://postgres:0000@localhost/postgres")
metadata = MetaData()
print()

users_table = Table(
    "users5",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, default=False),
)

if __name__ == "__main__":
    metadata.create_all(engine)
