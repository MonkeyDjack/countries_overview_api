from settings import *
import json

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Population(db.Model):
	__tablename__ = 'population_overview'
	country = db.Column(db.String(40), primary_key=True, unique=True)
	population_value = db.Column(db.Integer, nullable=False)
	yearly_change = db.Column(db.Float, nullable=True)
	land_area = db.Column(db.Integer, nullable=True)
	migrants = db.Column(db.Integer, nullable=True)
	med_age = db.Column(db.Integer, nullable=True)

	def json(self):
		return {
			'country': self.country,
			'population_value': self.population_value,
			'yearly_change': self.yearly_change,
			'land_area': self.land_area,
			'migrants': self.migrants,
			'med_age': self.med_age
		}

	def add_population_info(_country, _population_value, _yearly_change, _land_area, _migrants, _med_age):
		new_population_info = Population(country = _country, population_value = _population_value, yearly_change = _yearly_change, land_area = _land_area, migrants =_migrants, med_age = _med_age)
		db.session.add(new_population_info)  # add new info to database session
		db.session.commit()

	def get_all_population_info():
		return [Population.json(population) for population in Population.query.all()]
	def get_country_population(_country):
		return [Population.json(Population.query.filter_by(country=_country).first())]

	def update_population_info(_country, _population_value, _yearly_change, _land_area, _migrants, _med_age):
		country_to_update = Population.query.filter_by(country=_country).first()
		country_to_update.country = _country
		country_to_update.population_value = _population_value
		country_to_update.yearly_change = _yearly_change
		country_to_update.land_area = _land_area
		country_to_update.migrants = _migrants
		country_to_update.med_age = _med_age
		db.session.commit()

	def delete_population_info(_country):
		Population.query.filter_by(country=_country).delete()
		db.session.commit()
