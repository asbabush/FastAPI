import sqlalchemy
import databases

metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqllite.db")
engine = sqlalchemy.create_engine("sqlite:///sqllite.db")
