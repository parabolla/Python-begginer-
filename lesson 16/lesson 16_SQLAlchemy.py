from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///mydb.sqlite")
base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Users(base):
    __tablename__ = "competetion"
    competetion_id = Column(Integer, primary_key=True)
    competetion_name = Column(String)
    world_record = Column(String)
    set_data = Column(String)

    def __init__(self, competetion_id, competetion_name, world_record, set_data):
        self.competetion_id = competetion_id
        self.competetion_name = competetion_name
        self.world_record = world_record
        self.set_data = set_data

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (
            self.competetion_id, self.competetion_name, self.world_record, self.set_data)


base.metadata.create_all(engine)

# new_person = Users(5, "Porte", 10, '2015-10-10')
# new_person3 = Users(10, "Porke", 11, '2017-09-09')
# session.add(new_person3)
# # session.commit()
# session.rollback()
for competetion, competetion2 in session.query(Users.competetion_id,
                                               Users.competetion_name):
    print(competetion, competetion2)
