from google.appengine.ext import ndb

class Message(ndb.Model):
	trip = ndb.StringProperty(required=True)
	date_time = ndb.DateTimeProperty(required=True)
	count = ndb.IntegerProperty(required=True)

class Trip(ndb.Model):
	tripname = ndb.StringProperty(required=True)
	travelers = ndb.KeyProperty(repeated=True)
        length = ndb.StringProperty(required=True)
	itinerary = ndb.BlobKeyProperty()
	destination = ndb.StringProperty(required=True)
		
class TripTraveler(ndb.Model):
        name = ndb.StringProperty(required=True)
