#!/usr/bin/env python3

from faker import Faker
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Game

fake = Faker()

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///seed_db.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Game).delete()
    session.commit()
    # print(fake.profile())
    games=[Game(title=fake.name(),genre=fake.word(),platform=fake.word(),price=random.randint(0,60)) for i in range(50)]
    session.bulk_save_objects(games)
    # print(games)
    # ffvii = Game(title="Final Fantasy VII", platform="Playstation", genre="RPG", price=30)
    # mk8 = Game(title="Mario Kart 8", platform="Switch", genre="Racing", price=50)
    # session.bulk_save_objects([ffvii, mk8])
    session.commit()
    # import ipdb; ipdb.set_trace()
