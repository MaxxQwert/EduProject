from sqlalchemy import MetaData, create_engine, Table

engine = create_engine("postgresql://postgres:0000@localhost/maxx")
metadata = MetaData(bind=engine)


def main():
    users_table = Table(
        "table_name",
        metadata,
        autoload=True,
    )
    for col in users_table.columns:
        print(f"Column {col.name!r}", repr(col))


if __name__ == '__main__':
    main()