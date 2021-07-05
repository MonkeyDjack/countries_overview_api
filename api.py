from happiness_overview import *
from obesity_overview import Obesity, ObesityList
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


@app.route('/happiness_info', methods=['GET'])
def get_happiness_info():
	return jsonify(Happiness.get_all_happiness_info())

@app.route('/happiness_info/<string:country>', methods=['GET'])
def get_happiness_info_by_country(country):
	return_value = Happiness.get_country_happiness(country)
	return jsonify(return_value)

@app.route('/happiness_info', methods=['POST'])
def add_happiness_info():
	request_data = request.get_json()
	Happiness.add_happiness_info(request_data["rank"], request_data["country"],request_data["score"], request_data["gdp"],request_data["social_support"], request_data["healthy_life_expectancy"],request_data["life_choices_freedom"], request_data["generosity"],request_data["corruption_perception"])
	response = Response("info added!", 201, mimetype='application/json')
	return response

@app.route('/happiness_info/<string:country>', methods=['PUT'])
def update_happiness_info(country):
	request_data = request.get_json()
	Happiness.update_happiness_info(request_data["rank"], request_data["country"],request_data["score"], request_data["gdp"],request_data["social_support"], request_data["healthy_life_expectancy"],request_data["life_choices_freedom"], request_data["generosity"],request_data["corruption_perception"]) 
	response = Response("Info Updated", status=200, mimetype='application/json')
	return response

@app.route('/happiness_info/<string:country>', methods=['DELETE'])
def remove_happiness_info(country):
	Happiness.delete_happiness_info(country)
	response = Response("Info Deleted", status=200, mimetype='application/json')
	return response

#Happiness xml routes
@app.route('/happiness_infoxml', methods=['GET'])
def get_happiness_infoxml():
	xml= json2xml.Json2xml(Happiness.get_all_happiness_info(), wrapper="happiness_overview", attr_type=False).to_xml()
	if validate(xml, "schemas/xsd_schemas/happiness_schema.xsd"):
		return xml
	else:
		return print('Not valid! :(')

@app.route('/happiness_infoxml/<string:country>', methods=['GET'])
def get_happiness_info_by_countryxml(country):
	xml= json2xml.Json2xml(Happiness.get_country_happiness(country), wrapper="happiness_overview",pretty=True, attr_type=False).to_xml()
	return xml

@app.route('/happiness_infoxml', methods=['POST'])
def add_happiness_infoxml():

	request_data = request.data
	request_data = xmltodict.parse(request_data)
	Happiness.add_happiness_info(request_data["happiness_overview"]["item"]["rank"], request_data["happiness_overview"]["item"]["country"],request_data["happiness_overview"]["item"]["score"], request_data["happiness_overview"]["item"]["gdp"],request_data["happiness_overview"]["item"]["social_support"], request_data["happiness_overview"]["item"]["healthy_life_expectancy"],request_data["happiness_overview"]["item"]["life_choices_freedom"], request_data["happiness_overview"]["item"]["generosity"],request_data["happiness_overview"]["item"]["corruption_perception"])
	response = Response("info added!", 201, mimetype='application/xml')
	return response

@app.route('/happiness_infoxml/<string:country>', methods=['PUT'])
def update_happiness_infoxml(country):
	request_data = request.data
	request_data = xmltodict.parse(request_data)
	Happiness.update_happiness_info(request_data["happiness_overview"]["item"]["rank"], request_data["happiness_overview"]["item"]["country"],request_data["happiness_overview"]["item"]["score"], request_data["happiness_overview"]["item"]["gdp"],request_data["happiness_overview"]["item"]["social_support"], request_data["happiness_overview"]["item"]["healthy_life_expectancy"],request_data["happiness_overview"]["item"]["life_choices_freedom"], request_data["happiness_overview"]["item"]["generosity"],request_data["happiness_overview"]["item"]["corruption_perception"])
	response = Response("info updated!", 201, mimetype='application/xml')
	return response



#Population json routes
@app.route('/population_info', methods=['GET'])
def get_population_info():
	return jsonify(Population.get_all_population_info())

@app.route('/population_info/<string:country>', methods=['GET'])
def get_population_info_by_country(country):
	return_value = Population.get_country_population(country)
	return jsonify(return_value)

@app.route('/population_info', methods=['POST'])
def add_population_info():
	request_data = request.get_json()
	Population.add_population_info(request_data["country"],request_data["population_value"], request_data["yearly_change"],request_data["land_area"], request_data["migrants"],request_data["med_age"])
	response = Response("info added!", 201, mimetype='application/json')
	return response

@app.route('/population_info/<string:country>', methods=['PUT'])
def update_population_info(country):
	request_data = request.get_json()
	Population.update_population_info(request_data["country"],request_data["population_value"], request_data["yearly_change"],request_data["land_area"], request_data["migrants"],request_data["med_age"]) 
	response = Response("Info Updated", status=200, mimetype='application/json')
	return response

@app.route('/population_info/<string:country>', methods=['DELETE'])
def remove_population_info(country):
	Population.delete_population_info(country)
	response = Response("Info Deleted", status=200, mimetype='application/json')
	return response

#Population xml routes

@app.route('/population_infoxml', methods=['GET'])
def get_population_infoxml():
	xml= json2xml.Json2xml(Population.get_all_population_info(), wrapper="population_overview",pretty=True, attr_type=False).to_xml()
	return xml

@app.route('/population_infoxml/<string:country>', methods=['GET'])
def get_population_info_by_countryxml(country):
	xml= json2xml.Json2xml(Population.get_country_population(country), wrapper="population_overview",pretty=True, attr_type=False).to_xml()
	return xml

@app.route('/population_infoxml', methods=['POST'])
def add_population_infoxml():
	request_data = request.data
	request_data = xmltodict.parse(request_data)
	Population.add_population_info(request_data["population_overview"]["item"]["country"],request_data["population_overview"]["item"]["population_value"], request_data["population_overview"]["item"]["yearly_change"],request_data["population_overview"]["item"]["land_area"], request_data["population_overview"]["item"]["migrants"],request_data["population_overview"]["item"]["med_age"])
	response = Response("info added!", 201, mimetype='application/xml')
	return response

@app.route('/population_infoxml/<string:country>', methods=['PUT'])
def update_population_infoxml(country):
	request_data = request.data
	request_data = xmltodict.parse(request_data)
	Population.update_population_info(request_data["population_overview"]["item"]["country"],request_data["population_overview"]["item"]["population_value"], request_data["population_overview"]["item"]["yearly_change"],request_data["population_overview"]["item"]["land_area"], request_data["population_overview"]["item"]["migrants"],request_data["population_overview"]["item"]["med_age"]) 
	response = Response("Info Updated", status=200, mimetype='application/xml')
	return response



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

	