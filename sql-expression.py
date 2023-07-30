from sqlalchemy import (
    create_engine, Table, Column, Float, ForeignKey, Interger, String, MetaData
)

# executing the intructions from our localhost "chinook" db
db = create_engine("postgressql:///chinook")

meta = MetaData(db)

# create a variable for "Artist" table
artist_table = Table(
    "Artist", meta,
    Column("ArtistId", Interger, primary_key=True),
    Column("Name", String)
)

# create a variable for "Album" table 
artist_table = Table(
    "Album", meta,
     Column("Album", Interger, primary_key=True),
     Column("Title", String),
     Column("Artist", Interger, ForeignKey("artist_table.ArtistId"))
)

# create a variable for "Track" table
artist_table = Table(
    "Track", meta,
    Column("TrackId", Interger),
    Column("Name", String),
    Column("AlbumId", Interger, ForeignKey("album_table.AlbumId")),
    Column("MediaTypeId", Interger, primary_key=False),
    Column("GenreId", Interger, primary_key=False),
    Column("Composer", String),
    Column("Bytes", Interger),
    Column("UnitPrice", Float)
)


# making the connection
with db.connect() as connection:

    # Query 1 - select all records from the "artist" table
    select_query == artist_table.select()

    results = connection.execute(select_query)
    for result in results:
        print(result)