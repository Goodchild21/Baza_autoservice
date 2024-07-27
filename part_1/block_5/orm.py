import sqlalchemy as dz_orm
from sqlalchemy.orm import Session, declarative_base
import datetime

engine = dz_orm.create_engine('sqlite:///dz_orm.db')
Base = declarative_base()


class Custumers(Base):
    __tablename__ = 'custumers'

    id = dz_orm.Column('id', dz_orm.Integer, primary_key=True)
    firstname = dz_orm.Column('firstname', dz_orm.Text, nullable=False)
    middlename = dz_orm.Column('middlename', dz_orm.Text)
    lastname = dz_orm.Column('lastname', dz_orm.Text, nullable=False)
    phone = dz_orm.Column('phone', dz_orm.String(11), nullable=False)

class Mechanics(Base):
    __tablename__ = 'mechanics'

    id = dz_orm.Column('id', dz_orm.Integer, primary_key=True)
    firstname = dz_orm.Column('firstname', dz_orm.Text, nullable=False)
    middlename = dz_orm.Column('middlename', dz_orm.Text, nullable=False)
    lastname = dz_orm.Column('lastname', dz_orm.Text)
    specialization = dz_orm.Column('specialization', dz_orm.String(50), nullable=False)

class Parts(Base):
    __tablename__ = 'parts'

    id = dz_orm.Column('id', dz_orm.Integer, primary_key=True)
    parts = dz_orm.Column('parts', dz_orm.Text)
    price = dz_orm.Column('price', dz_orm.Float)

class Orders(Base):
    __tablename__ = 'orders'

    id = dz_orm.Column('id', dz_orm.Integer, primary_key=True)
    type_of_repair = dz_orm.Column('type_of_repair', dz_orm.Text)
    custumer_id = dz_orm.Column('custumer_id', dz_orm.Integer, dz_orm.ForeignKey(Custumers.id))
    mechanic_id = dz_orm.Column('mechanic_id', dz_orm.Integer, dz_orm.ForeignKey(Mechanics.id))
    parts_id = dz_orm.Column('parts_id', dz_orm.Integer, dz_orm.ForeignKey(Parts.id))
    total_price = dz_orm.Column('total_price', dz_orm.Float)
    created_date = dz_orm.Column('created_date', dz_orm.String, default=datetime.datetime.now())



Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


#============================Заполнение================================
with Session(engine) as conn:
    input_1_1 = Custumers(firstname='Aleksey',
                        middlename='Aleksandrovich',
                        lastname='Batashev',
                        phone='89534217689')
    input_1_2 = Custumers(firstname='Ivan', middlename='Ivanovich', lastname='Ivanov', phone='89534217690')
    input_1_3 = Custumers(firstname='Pedr', middlename='Pedrovich', lastname='Shpak', phone='89534217691')


    input_2_1 = Mechanics(firstname='Koliy', middlename= 'Kolich', specialization='engine_repair')
    input_2_2 = Mechanics(firstname='Geka', middlename='Sipliy', specialization='gearbox_repair')
    input_2_3 = Mechanics(firstname='Michal', middlename='Michalich', specialization='all_questions')


    input_3_1 = Parts(parts='camshaft х 2', price=54000.8)
    input_3_2 = Parts(parts='transmission_oil х 4', price=36400.6)
    input_3_3 = Parts(parts='spark_plug х 4', price=16400.4)

    
    input_3_1 = Orders(type_of_repair='replacing camshafts',
                        custumer_id=1,
                        mechanic_id=1,
                        parts_id=1,
                        total_price=70000.8)
    input_3_2 = Orders(type_of_repair='replacing transmission oil',
                        custumer_id=2,
                        mechanic_id=2,
                        parts_id=2,
                        total_price=50000.6)
    input_3_3 = Orders(type_of_repair='replacing spark plug',
                        custumer_id=3,
                        mechanic_id=3,
                        parts_id=3,
                        total_price=30000.4)
    

    # conn.add(input_1)
    # conn.add(input_2)
    # conn.add(input_3)
    conn.add_all([input_1_1, input_1_2, input_1_3])
    conn.add_all([input_2_1, input_2_2, input_2_3])
    conn.add_all([input_3_1, input_3_2, input_3_3])
    conn.commit()
