from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# SQL Server configuration
# connection_string = 'mssql+pyodbc://<DESKTOP-RR4DCFC>:<355744>@<server>/<pizza_delivery>?driver=ODBC+Driver+17+for+SQL+Server'
connection_string = 'mysql+mysqlconnector://root:355744@localhost:3306/pizza_delivery'

engine = create_engine(connection_string, echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)


