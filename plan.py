import webapp2
import base_page
from google.appengine.ext import ndb
from google.appengine.api import images
from google.appengine.ext import blobstore
import db_defs

class Plan(base_page.BaseHandler):
	def __init__(self, request, response):
		self.initialize(request, response)
		self.template_values = {}
		self.template_values['upload_url'] = blobstore.create_upload_url('/trip/add')

	def render(self, page):	
		self.template_values['travelers'] = [{'name': x.name, 'key':x.key.urlsafe()} for x in db_defs.TripTraveler.query(ancestor=ndb.Key(db_defs.TripTraveler, self.app.config.get('default-group'))).fetch()]
		self.template_values['trips'] = [{'tripname': x.tripname, 'key':x.key.urlsafe()}  for x in db_defs.Trip.query(ancestor=ndb.Key(db_defs.Trip, self.app.config.get('default-group'))).fetch()]
		base_page.BaseHandler.render(self, page, self.template _values)

	def get(self):
		self.render('plan.html')

	def post(self, itinerary_key=None):
		action = self.request.get('action')
                if action == 'add_trip':
                        k = ndb.Key(db_defs.Trip, self.app.config.get('default-group'))
                        newtrip = db_defs.Trip(parent=k)
                        newtrip.tripname = self.request.get('trip-tripname')
                        newtrip.travelers = [ndb.Key(urlsafe=x) for x in self.request.get_all('travelers[]')]
                        newtrip.startdate = '1/2/2004'
                        newtrip.enddate = '1/2/2005'
                        newtrip.itinerary = itinerary_key
                        newtrip.destination =  self.request.get('newtrip-destination')
                        newtrip.put()
                        self.template_values['message'] = 'Added trip ' + newtrip.tripname + 'to your trips'
                else:
                        self.template_value['message'] = 'Action ' + action + ' is unknown.'
