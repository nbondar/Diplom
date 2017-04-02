from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
deployment = Table('deployment', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('namespace_id', Integer),
    Column('timestamp', DateTime),
)

namespace = Table('namespace', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('count', Integer),
    Column('user_id', Integer),
    Column('timestamp', DateTime),
)

payment = Table('payment', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('status', Integer),
    Column('user_id', Integer),
    Column('period_begin', DateTime),
    Column('period_end', DateTime),
    Column('price', Float),
)

pods = Table('pods', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=50)),
    Column('deployment_id', Integer),
    Column('replicas', Integer),
    Column('size', Float),
    Column('status', Integer),
    Column('timestamp', DateTime),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
    Column('role', SmallInteger, default=ColumnDefault(0)),
    Column('passw', String(length=32)),
    Column('name', String(length=32)),
    Column('surname', String(length=32)),
    Column('phonenumber', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['deployment'].create()
    post_meta.tables['namespace'].create()
    post_meta.tables['payment'].create()
    post_meta.tables['pods'].create()
    post_meta.tables['user'].columns['phonenumber'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['deployment'].drop()
    post_meta.tables['namespace'].drop()
    post_meta.tables['payment'].drop()
    post_meta.tables['pods'].drop()
    post_meta.tables['user'].columns['phonenumber'].drop()
