# pip install databases sqlalchemy asyncpg psycopg2-binary
from databases import Database
from sqlalchemy import (
    MetaData,
    create_engine,
    Table,
    Column,
    Integer,
    Identity,
    String,
    Text,
    DateTime,
    ARRAY,
    func
)

#  insert

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/postgres"

database = Database(DATABASE_URL)
metadata = MetaData()

recipes = Table(
    "recipes",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    # Column("author", String),
    Column("keywords", String),
    Column("image_urls", ARRAY(String)),
    Column("created_at", DateTime, server_default=func.now()),
)

engine = create_engine(DATABASE_URL)

metadata.create_all(engine)