import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# engine = sqlalchemy.create_engine('sqlite:///test_sqlite2.db', echo=True)
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:パスワード@localhost/test_mysql_database2')

Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True
    )
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

person1 = Person(name='Mike')
session.add(person1)
person2 = Person(name='Kota')
session.add(person2)
person3 = Person(name='Jon')
session.add(person3)

session.commit()

person4 = session.query(Person).filter_by(name='Mike').first()
person4.name = 'Michel'
session.commit()

person5 = session.query(Person).filter_by(name='Jon').first()
session.delete(person5)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)
