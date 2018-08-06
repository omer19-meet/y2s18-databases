from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

k1 = Knowledge(topic="Farmercy", title="Banans", rate=8)

def add_article(article):
		# topic=topic,
		# title=title,
		# rate=rate)

	session.add(article)
	session.commit()

add_article(k1)


def query_all_articles():
	pass

def query_article_by_topic():
	pass

def delete_article_by_topic():
	pass

def delete_all_articles():
	pass

def edit_article_rating():
	pass
