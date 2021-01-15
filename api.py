from happiness_overview import *
from obesity_overview import *
from population_overview import *
from settings import *
from json2xml import json2xml#used to convert json to xml for xml routes
from json2xml.utils import readfromurl, readfromstring, readfromjson
from schemas import *
from dicttoxml import dicttoxml
import xmltodict
from flask import Flask, Response, Request, current_app, jsonify


#Happiness routes
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
	xml= json2xml.Json2xml(Happiness.get_all_happiness_info(), wrapper="happiness_overview",pretty=True, attr_type=False).to_xml()
	return xml

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

#Obesity routes
@app.route('/obesity_info', methods=['GET'])
def get_obesity_info():
	return jsonify(Obesity.get_all_obesity_info())

@app.route('/obesity_info/<string:country>', methods=['GET'])
def get_obesity_info_by_country(country):
	return_value = Obesity.get_country_obesity(country)
	return jsonify(return_value)

@app.route('/obesity_info', methods=['POST'])
def add_obesity_info():
	request_data = request.get_json()
	Obesity.add_obesity_info(request_data["country"], request_data["both_sexes"], request_data["male"], request_data["female"])
	response = Response("info added!", 201, mimetype='application/json')
	return response

@app.route('/obesity_info/<string:country>', methods=['PUT'])
def update_obesity_info(country):
	request_data = request.get_json()
	Obesity.update_obesity_info(request_data["country"], request_data["both_sexes"],request_data["male"], request_data["female"]) 
	response = Response("Info Updated", status=200, mimetype='application/json')
	return response

@app.route('/obesity_info/<string:country>', methods=['DELETE'])
def remove_obesity_info(country):
	Obesity.delete_obesity_info(country)
	response = Response("Info Deleted", status=200, mimetype='application/json')
	return response

#Obesity xml routes
@app.route('/obesity_infoxml', methods=['GET'])
def get_obesity_infoxml():
	xml= json2xml.Json2xml(Obesity.get_all_obesity_info(), wrapper="obesity_overview",pretty=True, attr_type=False).to_xml()
	return xml

@app.route('/obesity_infoxml/<string:country>', methods=['GET'])
def get_obesity_info_by_countryxml(country):
	xml = json2xml.Json2xml(Obesity.get_country_obesity(country), wrapper="obesity_overview",pretty=True, attr_type=False).to_xml()
	return xml

@app.route('/obesity_infoxml', methods=['POST'])
def add_obesity_infoxml():
	request_data = request.data
	request_data = xmltodict.parse(request_data)
	Obesity.add_obesity_info(request_data["obesity_overview"]["item"]["country"], request_data["obesity_overview"]["item"]["both_sexes"],request_data["obesity_overview"]["item"]["male"], request_data["obesity_overview"]["item"]["female"])
	response = Response("info added!", 201, mimetype='application/xml')
	return response

@app.route('/obesity_infoxml/<string:country>', methods=['PUT'])
def update_obesity_infoxml(country):
	request_data = request.data
	request_data = xmltodict.parse(request_data)
	Obesity.update_obesity_info(request_data["obesity_overview"]["item"]["country"], request_data["obesity_overview"]["item"]["both_sexes"],request_data["obesity_overview"]["item"]["male"], request_data["obesity_overview"]["item"]["female"]) 
	response = Response("Info Updated", status=200, mimetype='application/xml')
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
	app.run(port=1234, debug=True)

	