from flask_restx import Namespace, Resource, fields
from app.services.facade import HBnBFacade

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'first_name': fields.String(required=True, description='First name'),
    'last_name': fields.String(required=True, description='Last name'),
    'email': fields.String(required=True, description='Email')
})

facade = HBnBFacade()

@api.route('/')
class UserList(Resource):
    @api.expect(user_model, validate=True)
    @api.response(201, 'User created')
    @api.response(400, 'Bad request')
    def post(self):
        """Create a new user"""
        user_data = api.payload
        existing_user = facade.get_user_by_email(user_data['email'])
        if existing_user:
            return {'error': 'Email already registered'}, 400

        user = facade.create_user(user_data)
        if not user:
            return {'error': 'Failed to create user'}, 400
        return {'id': user.id, 'first_name': user.first_name,
                'last_name': user.last_name, 'email': user.email}, 201

    @api.response(200, 'Success')
    def get(self):
        """Get all users"""
        users = facade.get_all_users()
        return [{'id': user.id, 'first_name': user.first_name,
                 'last_name': user.last_name,
                 'email': user.email} for user in users], 200

@api.route('/<user_id>')
class UserResource(Resource):
    @api.response(200, 'Success')
    @api.response(404, 'User not found')
    def get(self, user_id):
        """Get a user by ID"""
        user = facade.get_user(user_id)
        if not user:
            return {'error': 'User not found'}, 404
        return {'id': user.id, 'first_name': user.first_name,
                'last_name': user.last_name, 'email': user.email}, 200

    @api.expect(user_model, validate=True)
    @api.response(200, 'User updated')
    @api.response(404, 'User not found')
    def put(self, user_id):
        """Update a user"""
        user_data = api.payload
        updated_user = facade.update_user(user_id, user_data)
        if not updated_user:
            return {'error': 'User not found'}, 404
        return {'id': updated_user.id, 'first_name': updated_user.first_name,
                'last_name': updated_user.last_name,
                'email': updated_user.email}, 200