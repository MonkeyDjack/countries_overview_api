from happiness_overview import *
from obesity_overview import Obesity, ObesityList
from population_overview import *
from validator import *
from settings import *

from schemas import *
from flask import Flask, Response, Request, current_app, jsonify


@api.representation('text/xml') #application/xml header
def output_xml(data, code, headers=None):
	resp = make_response(dumps({'response' : data}), code) # parses data from db to xml with response as a root
	resp.headers.extend(headers or {})
	return resp

@api.representation('application/json')
def output_json(data, code, headers=None):
	resp = make_response(json.dumps({'response': data}), code)
	resp.headers.extend(headers or {})
	return resp

#obesity routes
api.add_resource(ObesityList, '/obesity',
                                      '/')
api.add_resource(Obesity, '/obesity/<record_country>')

#Population routes routes
api.add_resource(PopulationList, '/population',
                                      '/')
api.add_resource(Population, '/population/<record_country>')

#Happiness routes routes
api.add_resource(HappinessList, '/happiness',
                                      '/')
api.add_resource(Happiness, '/happiness/<record_country>')





#test of join
@app.route('/happiness_population', methods=['GET'])
def get_two_tables():
	db_data = db.session.query(Population, Happiness, Obesity). \
	select_from(Population).join(Happiness, Happiness.country == Population.country). \
	join(Obesity, Obesity.country == Population.country).all()
	db_data = json.dumps([dict(d) for d in db_data])
	return jsonify(db_data)

if __name__ == "__main__":
	app.run(port=5000, debug=True)

	