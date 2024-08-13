import sqlalchemy as dz_core
import datetime

engine = dz_core.create_engine('sqlite:///dz_core.db')
meta = dz_core.MetaData()

custumers = dz_core.Table(
    'custumers',
    meta,
    dz_core.Column('id', dz_core.Integer, primary_key=True),
    dz_core.Column('firstname', dz_core.Text, nullable=False),
    dz_core.Column('middlename', dz_core.Text),
    dz_core.Column('lastname', dz_core.Text, nullable=False),
    dz_core.Column('phone', dz_core.String(11), nullable=False)
)
mechanics = dz_core.Table(
    'mechanics',
    meta,
    dz_core.Column('id', dz_core.Integer, primary_key=True),
    dz_core.Column('firstname', dz_core.Text, nullable=False),
    dz_core.Column('middlename', dz_core.Text, nullable=False),
    dz_core.Column('lastname', dz_core.Text),
    dz_core.Column('specialization', dz_core.String(50), nullable=False)
)
parts = dz_core.Table(
    'parts',
    meta,
    dz_core.Column('id', dz_core.Integer, primary_key=True),
    dz_core.Column('parts', dz_core.Text),
    dz_core.Column('price', dz_core.Float),
)
orders = dz_core.Table(
    'orders',
    meta,
    dz_core.Column('id', dz_core.Integer, primary_key=True),
    dz_core.Column('type_of_repair', dz_core.Text),
    dz_core.Column('custumer_id', dz_core.ForeignKey("custumers.id")),
    dz_core.Column('mechanic_id', dz_core.ForeignKey("mechanics.id")),
    dz_core.Column('parts_id', dz_core.ForeignKey("parts.id")),
    dz_core.Column('total_price', dz_core.Float),
    dz_core.Column('created_date', dz_core.String, default=datetime.datetime.now())
)


meta.drop_all(engine)
meta.create_all(engine)



# ==============================Заполнение================================
with engine.connect() as conn:
    input_1 = dz_core.insert(custumers).values(firstname='Aleksey',
                                            middlename='Aleksandrovich',
                                            lastname='Batashev',
                                            phone='89534217689')
    input_2 = dz_core.insert(custumers).values(firstname='Ivan', middlename='Ivanovich', lastname='Ivanov', phone='89534217690')
    input_3 = dz_core.insert(custumers).values(firstname='Pedr', middlename='Pedrovich', lastname='Shpak', phone='89534217691')
    conn.execute(input_1)
    conn.execute(input_2)
    conn.execute(input_3)

    # select_test = dz_core.select(custumers)
    # print(conn.execute(select_test).all())
    conn.commit()



with engine.connect() as conn:
    input_1 = dz_core.insert(mechanics).values(firstname='Koliy', middlename= 'Kolich', specialization='engine_repair')
    input_2 = dz_core.insert(mechanics).values(firstname='Geka', middlename='Sipliy', specialization='gearbox_repair')
    input_3 = dz_core.insert(mechanics).values(firstname='Michal', middlename='Michalich', specialization='all_questions')
    conn.execute(input_1)
    conn.execute(input_2)
    conn.execute(input_3)

    # select_test = dz_core.select(mechanics)
    # print(conn.execute(select_test).all())
    conn.commit()


with engine.connect() as conn:
    input_1 = dz_core.insert(parts).values(parts='camshaft х 2', price=54000.8)
    input_2 = dz_core.insert(parts).values(parts='transmission_oil х 4', price=36400.6)
    input_3 = dz_core.insert(parts).values(parts='spark_plug х 4', price=16400.4)
    conn.execute(input_1)
    conn.execute(input_2)
    conn.execute(input_3)
    conn.commit()


with engine.connect() as conn:
    input_1 = dz_core.insert(orders).values(type_of_repair='replacing camshafts',
                                        custumer_id=1,
                                        mechanic_id=1,
                                        parts_id=1,
                                        total_price=70000.8)
    input_2 = dz_core.insert(orders).values(type_of_repair='replacing transmission oil',
                                        custumer_id=2,
                                        mechanic_id=2,
                                        parts_id=2,
                                        total_price=70000.8)
    input_3 = dz_core.insert(orders).values(type_of_repair='replacing spark plug',
                                        custumer_id=3,
                                        mechanic_id=3,
                                        parts_id=3,
                                        total_price=70000.8)
    conn.execute(input_1)
    conn.execute(input_2)
    conn.execute(input_3)
    conn.commit()


# ----------------------------------Изменения и выборки-----------------------------------
with engine.connect() as conn:
    # +
    update_1 = dz_core.update(mechanics).values(specialization='Grand_master_boy').where(mechanics.c.middlename == 'Sipliy')
    conn.execute(update_1)
    # select_test = dz_core.select(mechanics)
    # print(conn.execute(select_test).all())

    # +
    update_2 = dz_core.update(custumers).where(custumers.c.id == 2).values(firstname='Oleg', middlename='Olegovich', lastname='Olegov')
    conn.execute(update_2)
    # select_test1 = dz_core.select(custumers)
    # print(conn.execute(select_test1).all())

    # +
    delete_1 = dz_core.delete(orders).where(orders.c.id == 3)
    conn.execute(delete_1)
    # select_test2 = dz_core.select(orders)
    # print(conn.execute(select_test2).all())

    # +
    delete_2 = dz_core.delete(mechanics).where(mechanics.c.specialization == 'all_questions')
    conn.execute(delete_2)
    # select_test3 = dz_core.select(mechanics)
    # print(conn.execute(select_test3).all())

    # +
    select_1 = dz_core.select(custumers).where(custumers.c.lastname == 'Batashev')
    # print(conn.execute(select_1).first())

    conn.commit()
