from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('places', description='Place operations')

# Define the models for related entities
amenity_model = api.model('PlaceAmenity', {
    'id': fields.String(description='Amenity ID'),
    'name': fields.String(description='Name of the amenity')
})

user_model = api.model('PlaceUser', {
    'id': fields.String(description='User ID'),
    'first_name': fields.String(description='First name of the owner'),
    'last_name': fields.String(description='Last name of the owner'),
    'email': fields.String(description='Email of the owner')
})

# Define the place model for input validation and documentation
place_model = api.model('Place', {
    'title': fields.String(required=True,
                           description='Title of the place'),
    'description': fields.String(description='Description of the place'),
    'price': fields.Float(required=True,
                          description='Price per night'),
    'latitude': fields.Float(required=True,
                             description='Latitude of the place'),
    'longitude': fields.Float(required=True,
                              description='Longitude of the place'),
    'owner_id': fields.String(required=True,
                              description='ID of the owner'),
    'owner': fields.Nested(user_model,
                           description='Owner details'),
    'amenities': fields.List(fields.String,
                             required=True,
                             description="List of amenities ID's")
})

facade = HBnBFacade()


@api.route('/')
class PlaceList(Resource):
    @api.expect(place_model)
    @api.response(201, 'Place successfully created')
    @api.response(400, 'Invalid input data')
    def post(self):
        """Register a new place"""
        place_data = api.payload
        owner_id = place_data.get(owner_id)
        """verify is owner exist"""
        owner = facade.get_user(owner_id)
        if not owner:
            return{'error': 'Owner not found'}, 404
        
        new_place = facade.create_place(place_data)
        return new_place, 201


@api.response(200, 'List of places retrieved successfully')
def get(self):
    """Retrieve a list of all places"""
    places = facade.get_all_places()
    if places is not None:
        return places, 200
    else:
        return {'message': 'List of places not retrieved successfully'}, 500


@api.route('/<place_id>')
class PlaceResource(Resource):
    @api.response(200, 'Place details retrieved successfully')
    @api.response(404, 'Place not found')
    def get(self, place_id):
        """Get place details by ID"""
        # Placeholder for the logic to retrieve a place by ID,
        # including associated owner and amenities
        place = facade.get_place(place_id)
        if not place:
            return {'error': 'Place not found'}, 404
        return place, 200

    @api.expect(place_model)
    @api.response(200, 'Place updated successfully')
    @api.response(404, 'Place not found')
    @api.response(400, 'Invalid input data')
    def put(self, place_id):
        """Update a place's information"""
        # Placeholder for the logic to update a place by ID
        place_data = api.payload
        updated_place = facade.update_place(place_id, place_data)
        if not updated_place:
            return {'error': 'Place not found'}, 404
        return updated_place, 200