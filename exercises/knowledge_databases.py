from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()



def add_article(topic , title , rate):
    k_object = Knowledge(topic=topic, title=title, rate=rate)

    # k1 = Knowledge(topic="Farmercy", title="Banans", rate=8)
    session.add(k_object)
    session.commit()
    return k_object


# k1 = Knowledge(topic="Farmercy", title="Banans", rate=8)
# print(add_article("Biology", "Lions", 7))
# add_article("Tecnology", "Computers", 5)
# add_article("Tecnology", "Smartphonse", 10)
# add_article("Biology", "planets", 3)
# add_article('Astronomy', "Moon", 9)

def delete_article_by_topic(their_name):
    dlt = session.query(Knowledge).filter_by(topic=their_name).delete()
    return dlt
    session.commit()

# delete_article_by_topic("Biology")


def query_all_articles():
    articals = session.query(Knowledge).all()
    return articals

# print(query_all_articles())

def query_article_by_topic(their_name):
    topics = session.query(Knowledge).filter_by(topic=their_name).all()
    return topics




def delete_all_articles():
    daa = session.query(Knowledge).delete()
    session.commit()

def edit_article_rating(update_rating , artical_title):
    ear = session.query(Knowledge).filter_by(title= artical_title).all()
    for i in range(len(ear)):
        ear[i].rate = update_rating


edit_article_rating( 2, "Lions")
print(query_article_by_topic("Biology"))
    
