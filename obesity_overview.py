from settings import *
import json
import simplexml
from sqlalchemy import desc

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Obesity(db.Model):
	__tablename__ = 'obesity_overview'
	country = db.Column(db.String(40), primary_key=True, unique=True)
	both_sexes = db.Column(db.FLOAT, nullable = False)
	male = db.Column(db.FLOAT, nullable = False)
	female = db.Column(db.FLOAT, nullable = False)
	def json(self):
		return{
			'country': self.country,
			'both_sexes': self.both_sexes,
			'male': self.male,
			'female': self.female
		}

	def add_obesity_info(_country, _both_sexes, _male, _female):
		new_obesity_info = Obesity(country = _country, both_sexes = _both_sexes, male = _male, female = _female)
		db.session.add(new_obesity_info)
		db.session.commit()
	def get_all_obesity_info():
		return [Obesity.json(obesity) for obesity in Obesity.query.all()]

	def get_country_obesity(_country):
		return [Obesity.json(Obesity.query.filter_by(country=_country).first())]

	def update_obesity_info(_country, _both_sexes, _male, _female):
		obesity_to_update = Obesity.query.filter_by(country = _country).first()
		obesity_to_update.country = _country
		obesity_to_update.both_sexes = _both_sexes
		obesity_to_update.male = _male
		obesity_to_update.female = _female
		db.session.commit()

	def delete_obesity_info(_country):
		Obesity.query.filter_by(country = _country).delete()
		db.session.commit()
