from sqlalchemy.orm import create_engine, Session
engine = create_engine("postgres+psycopg2://postgres:pass@localhost/mydb")
from sqlalchemy.orm import sessionmaker, Session

Session = sessionmaker(bind=engine)
session = Session(bind=engine)

session = Session ()

c1 = Customer(first_name='Toby',
              last_name='Miller',
              username='tmiller',
              email='tmiller@example.com',
              address='1662 Kinney Street',
              town='Wolfden'
              )

c2 = Customer(first_name='Scott',
              last_name='Harvey',
              username='scottharvey',
              email='scottharvey@example.com',
              address='424 Patterson Street',
              town='Beckinsdale'
              )
c1, c2

c1.first_name, c1.last_name
c2.first_name, c2.last_name

session.add_all([c1, c2])
session.commit()


