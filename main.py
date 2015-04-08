import webapp2

#config = {default-group': 'base-data'}

app  = webapp2.WSGIApplication ([
	('/edit/trip', 'edit_trip.EditTrip'),
	('/edit', 'edit.Edit'),
	('/trip/add', 'add_trip.AddTrip'),
	('/admin', 'admin.Admin'),
	('/', 'base_page.Welcome')
], debug=True)
#], debug=True, config=config)
