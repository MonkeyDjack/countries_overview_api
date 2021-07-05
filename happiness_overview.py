from settings import *
import json
from sqlalchemy import desc


	#db initialization
db = SQLAlchemy(app)
#ma = Marshmallow(app)

class Happiness(db.Model):
	__tablename__ = 'happiness_overview'
	rank = db.Column(db.Integer,nullable = False, unique = True)
	country = db.Column(db.String(40), primary_key=True, unique=True)
	score = db.Column(db.FLOAT, nullable = False)
	gdp = db.Column(db.FLOAT, nullable = False)
	social_support = db.Column(db.FLOAT, nullable = False)
	healthy_life_expectancy = db.Column(db.FLOAT, nullable = False)
	life_choices_freedom = db.Column(db.FLOAT, nullable = False)
	generosity = db.Column(db.FLOAT, nullable = False)
	corruption_perception = db.Column(db.FLOAT, nullable = False)
	def json(self): #function to convert the output to json
		return { 
			'rank': self.rank, 
			'country': self.country,
			'score': self.score, 
			'gdp': self.gdp, 
			'social_support': self.social_support, 
			'healthy_life_expectancy': self.healthy_life_expectancy, 
			'life_choices_freedom': self.life_choices_freedom, 
			'generosity': self.generosity,
			'corruption_perception': self.corruption_perception
		
		}
	

	def add_happiness_info(_rank, _country, _score, _gdp,_social_support,_healthy_life_expectancy,_life_choices_freedom,_generosity,_corruption_perception):
		new_happiness_info = Happiness(rank=_rank, country=_country, score=_score, gdp=_gdp,social_support=_social_support,healthy_life_expectancy=_healthy_life_expectancy,life_choices_freedom=_life_choices_freedom,generosity=_generosity,corruption_perception=_corruption_perception)
		db.session.add(new_happiness_info)
		db.session.commit()  
	def get_all_happiness_info():
		return [Happiness.json(happiness) for happiness in Happiness.query.all()]
	def get_country_happiness(_country):
		return [Happiness.json(Happiness.query.filter_by(country=_country).first())]

	def update_happiness_info(_rank, _country, _score, _gdp,_social_support,_healthy_life_expectancy,_life_choices_freedom,_generosity,_corruption_perception):
		country_to_update = Happiness.query.filter_by(country=_country).first()
		country_to_update.rank = _rank
		country_to_update.country = _country
		country_to_update.score = _score
		country_to_update.gdp = _gdp
		country_to_update.social_support = _social_support
		country_to_update.healthy_life_expectancy = _healthy_life_expectancy
		country_to_update.life_choices_freedom = _life_choices_freedom
		country_to_update.generosity = _generosity
		country_to_update.corruption_perception = _corruption_perception
		db.session.commit()
	def delete_happiness_info(_country):
		Happiness.query.filter_by(country=_country).delete()
		db.session.commit()
		

