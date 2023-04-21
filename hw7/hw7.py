import sqlalchemy as db

# Create a new database named "films_db"
engine = db.create_engine('sqlite:///films_db.db')
connection = engine.connect()

# Define the table structure
metadata = db.MetaData()
films = db.Table('films', metadata,
                 db.Column('id', db.Integer, primary_key=True),
                 db.Column('title', db.String),
                 db.Column('director', db.String),
                 db.Column('release_year', db.Integer))

# Create the table
metadata.create_all(engine)

# Add 3 films to the films table
query = db.insert(films).values([
    {'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'release_year': 1972},
    {'title': 'The Shawshank Redemption', 'director': 'Frank Darabont', 'release_year': 1994},
    {'title': 'The Dark Knight', 'director': 'Christopher Nolan', 'release_year': 2008}
])
connection.execute(query)

# Update the director of a film
query = db.update(films).where(films.c.title == 'The Godfather').values(director='Martin Scorsese')
connection.execute(query)

# Print the data from the table
query = db.select([films])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()
print(result_set)

# Delete all data from the table
query = db.delete(films)
connection.execute(query)