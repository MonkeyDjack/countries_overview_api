from happiness_overview import *
from obesity_overview import *
from population_overview import *
from validator import *
from settings import *
from json2xml import json2xml#used to convert json to xml for xml routes
from json2xml.utils import readfromurl, readfromstring, readfromjson
from schemas import *
from dicttoxml import dicttoxml
import xmltodict
from flask import Flask, Response, Request, current_app, jsonify


@api.representation('application/xml') #application/xml header
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
api.add_resource(ObesityList, '/obesitylist',
                                      '/')
api.add_resource(Obesity, '/obesitylist/<record_country>')

#Population routes routes
api.add_resource(PopulationList, '/populationlist',
                                      '/')
api.add_resource(Population, '/populationlist/<record_country>')

#Happiness routes routes
api.add_resource(HappinessList, '/populationlist',
                                      '/')
api.add_resource(Happiness, '/populationlist/<record_country>')





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

	