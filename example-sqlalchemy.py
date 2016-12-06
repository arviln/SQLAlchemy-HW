
# coding: utf-8

# Using SQLAlchemy to Talk to a Database
# =====================
# SqlAlchemy helps you use a database to store and retrieve information from python.  It abstracts the specific storage engine from te way you use it - so it doesn't care if you end up using MySQL, SQLite, or whatever else. In addition, you can use core and the object-relational mapper (ORM) to avoid writing any SQL at all.  The [SQLAlchemy homepage](http://www.sqlalchemy.org/) has lots of good examples and full documentation.


from sqlalchemy import *
import datetime
import mediacloud

mc = mediacloud.api.MediaCloud('e0ca07461a0f1fb81d96d5584ab9ddc02bed9978581a0a770dd9b3ce75b0d82f')

# ## Basic SQL Generation
# The core library generates SQL for you.  Read more about it on their [expression language tutorial page](http://docs.sqlalchemy.org/en/rel_1_0/core/index.html). Below are some basic examples.

# ### Creating a Table
# Read more about [defining and creating tables](http://docs.sqlalchemy.org/en/rel_1_0/core/tutorial.html#define-and-create-tables).



## add `echo=True` to see log statements of all the SQL that is generated
#engine = create_engine('sqlite:///:memory:',echo=True) # just save the db in memory for now (ie. not on disk)
#metadata = MetaData()
## define a table to use
#queries = Table('queries', metadata,
#    Column('id', Integer, primary_key=True),
#    Column('keywords', String(400), nullable=False),
#    Column('timestamp', DateTime, default=datetime.datetime.now),
#)
#metadata.create_all(engine) # and create the tables in the database
#
#
## ### Inserting Data
## Read more about generating [SQL insert statements](http://docs.sqlalchemy.org/en/rel_1_0/core/tutorial.html#insert-expressions).
#
#
#
#insert_stmt = queries.insert()
#str(insert_stmt) # see an example of what this will do
#
#
#insert_stmt = queries.insert().values(keywords="puppies")
#str(insert_stmt)
#
#
#db_conn = engine.connect()
#result = db_conn.execute(insert_stmt)
#result.inserted_primary_key # print out the primary key it was assigned
#
#
#insert_stmt = queries.insert().values(keywords="kittens")
#result = db_conn.execute(insert_stmt)
#result.inserted_primary_key # print out the primary key it was assigned
#
#
#
#
#
## # Retrieving Data
## Read more about using [SQL select statments](http://docs.sqlalchemy.org/en/rel_1_0/core/tutorial.html#selecting).
#
#
#
#from sqlalchemy.sql import select
#select_stmt = select([queries])
#results = db_conn.execute(select_stmt)
#for row in results:
#    print row
#
#
#
#
#select_stmt = select([queries]).where(queries.c.id==1)
#for row in db_conn.execute(select_stmt):
#    print row
#
#
#
#
#select_stmt = select([queries]).where(queries.c.keywords.like('p%'))
#for row in db_conn.execute(select_stmt):
#    print row
#
#
## ## ORM
## You can use their ORM library to handle the translation into full-fledged python objects.  This can help you build the Model for you [MVC](https://en.wikipedia.org/wiki/Model–view–controller) solution.
#
#
#
#import datetime
#from sqlalchemy import *
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import sessionmaker
#Base = declarative_base()
#
#
## ### Creating a class mapping
## Read more about [creating a mapping](http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#declare-a-mapping).
#
#
#
#class Query(Base):
#    __tablename__ = 'queries'
#    id = Column(Integer, primary_key=True)
#    keywords = Column(String(400))
#    timestamp = Column(DateTime,default=datetime.datetime.now)
#    def __repr__(self):
#        return "<Query(keywords='%s')>" % (self.keywords)
#Query.__table__
#
#
## ### Creating a connection and session
## Read more about [creating this stuff](http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#creating-a-session).
#
#
#
#engine = create_engine('sqlite:///:memory:') # just save the db in memory for now (ie. not on disk)
#Base.metadata.create_all(engine)
#Session = sessionmaker(bind=engine)
#my_session = Session()
#
#
## ### Inserting Data
## Read more about [inserting data with an ORM](http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#adding-new-objects).
#
#
#
#query = Query(keywords="iguana")
#query.keywords
#
#
#
#
#my_session.add(query)
#my_session.commit()
#query.id
#
#
## ### Retrieving Data
## Read more about [retrieving data from the db](http://docs.sqlalchemy.org/en/rel_1_0/orm/tutorial.html#querying) via an ORM class.
#
#for q in my_session.query(Query).order_by(Query.timestamp):
#    print q
#
#
#
#query1 = Query(keywords="robot")
#query2 = Query(keywords="puppy")
#my_session.add_all([query1,query2])
#my_session.commit()
#
#
#
#for q in my_session.query(Query).order_by(Query.timestamp):
#    print q
#
#
#
#for q in my_session.query(Query).filter(Query.keywords.like('r%')):
#    print q



#MAS.500 HW


# add `echo=True` to see log statements of all the SQL that is generated
engine = create_engine('sqlite:///:memory:',echo=True) # just save the db in memory for now (ie. not on disk)
metadata = MetaData()
# define a table to use
queries = Table('queries', metadata,
    Column('id', Integer, primary_key=True),
    Column('keywords', String(400), nullable=False),
    Column('sentcount', Integer, nullable = False),
    Column('timestamp', DateTime, default=datetime.datetime.now),
)
metadata.create_all(engine) # and create the tables in the database



keyword1 = 'trump'
search1 = mc.sentenceCount(keyword1, solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
print search1['count'] # prints the number of sentences found

insert_stmt = queries.insert().values(keywords = keyword1, sentcount = search1['count'])
str(insert_stmt)

db_conn = engine.connect()
result = db_conn.execute(insert_stmt)
result.inserted_primary_key # print out the primary key it was assigned

keyword2 = 'pence'
search2 = mc.sentenceCount(keyword2, solr_filter=[mc.publish_date_query( datetime.date( 2016, 9, 1), datetime.date( 2016, 10, 1) ), 'tags_id_media:1' ])
print search2['count'] # prints the number of sentences found

insert_stmt = queries.insert().values(keywords = keyword2, sentcount = search2['count'])
str(insert_stmt)

db_conn = engine.connect()
result = db_conn.execute(insert_stmt)
result.inserted_primary_key # print out the primary key it was assigned


from sqlalchemy.sql import select
select_stmt = select([queries.c.sentcount])
results = db_conn.execute(select_stmt)
summation = 0
for row in results:
    summation = summation + row[0]
print summation
