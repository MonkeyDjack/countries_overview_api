#from happiness_overview import *
#from obesity_overview import *
#from population_overview import *
#
#results = db.session.query(HappinessRecord, ObesityRecord, PopulationRecord).join(ObesityRecord, ObesityRecord.country == HappinessRecord.country).join(PopulationRecord, PopulationRecord.country == ObesityRecord.country).with_entities(HappinessRecord.country, HappinessRecord.rank, PopulationRecord.population_value, HappinessRecord.score, ObesityRecord.both_sexes).all()
#
#
#class GeneralRecord(results):
#
#
#    def serialize(results):
#        return {
#            'countryOverview': {
#                'country': results.country,
#                'rank': results.rank,
#                'population_value': results.population_value,
#                'score': results.score,
#                'both_sexes': results.both_sexes
#            }
#            
#        }

#class HappinessList(Resource):
#	def get(self):
#		records = GeneralRecord.query.all()
#		return [GeneralRecord.serialize(record) for record in records]