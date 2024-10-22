from app.persistence.repository import InMemoryRepository
from app.models.user import User
from app.models.place import Place

class HBnBFacade:
    """Facade for managing users and places in the HBnB application.

    This class provides an interface to interact with user and place
    repositories, allowing for operations such as creating, retrieving,
    updating, and authenticating users.
    """

    def __init__(self):
        """Initialize the HBnBFacade with in-memory repositories for users,
        places, reviews, and amenities.
        """
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    def create_user(self, user_data):
        """Create a new user with the provided data.

        Args:
            user_data (dict): A dictionary containing user attributes.

        Returns:
            User: The created User instance.
        """
        user = User(**user_data)
        self.user_repo.add(user)
        return user

    def get_user(self, user_id):
        """Retrieve a user by their unique ID.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            User: The User instance if found, otherwise None.
        """
        return self.user_repo.get(user_id)

    def get_all_users(self):
        """Retrieve all users in the repository.

        Returns:
            list: A list of User instances.
        """
        return self.user_repo.get_all()

    def get_user_by_email(self, email):
        """Retrieve a user by their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            User: The User instance if found, otherwise None.
        """
        return self.user_repo.get_by_attribute('email', email)

    def update_user(self, user_id, user_data):
        """Update an existing user with new data.

        Args:
            user_id (str): The unique identifier of the user to update.
            user_data (dict): A dictionary containing the
            updated user attributes.

        Returns:
            User: The updated User instance if the user was found and updated,
            otherwise None.
        """
        user = self.get_user(user_id)
        if user:
            for key, value in user_data.items():
                setattr(user, key, value)
            self.user_repo.update(user_id, user_data)
            return user
        return None

    def authenticate_user(self, email, password):
        """Authenticate a user by checking their email and password.

        Args:
            email (str): The email address of the user.
            password (str): The password provided for authentication.

        Returns:
            User: The authenticated User instance
            if successful, otherwise None.
        """
        user = self.user_repo.get_by_attribute('email', email)
        if user and user.check_password(password):
            return user
        return None

    def create_place(self, place_data):
        owner_id = place_data.pop('owner_id', None)
        if not owner_id:
            return None, "Owner ID is required"

        owner = self.get_user(owner_id)
        if not owner:
            return None, "Owner not found"

        try:
            place = Place(
                title=place_data.get('title'),
                description=place_data.get('description'),
                price=place_data.get('price'),
                latitude=place_data.get('latitude'),
                longitude=place_data.get('longitude'),
                owner=owner
            )
            self.place_repo.add(place)
            return place, None
        except ValueError as e:
            return None, str(e)
    # Placeholder method for fetching a place by ID

    def get_place(self, place_id):
        place = self.place_repo.get(place_id)
        if place:
            return {
                'id': place.id,
                'title': place.title,
                'description': place.description,
                'price': place.price,
                'latitude': place.latitude,
                'longitude': place.longitude,
                'owner': {
                    'id': place.owner.id,
                    'first_name': place.owner.first_name,
                    'last_name': place.owner.last_name,
                    'email': place.owner.email
                },
                'reviews': [self.get_review(review.id) for review in place.reviews],
                'amenities': [self.get_amenity(amenity.id) for amenity in place.amenities]
            }
        return None

    def get_all_places(self):
        return self.place.repo.get_all()

    def update_place(self, place_id, place_data):
        place = self.place_repo.get(place_id)
        if not place:
            return None, "Place not found"

        error_message = None
        if 'title' in place_data:
            error_message = place.set_title(place_data['title'])
        if 'description' in place_data:
            error_message = place.set_description(place_data['description'])
        if 'price' in place_data:
            error_message = place.set_price(place_data['price'])
        if 'latitude' in place_data:
            error_message = place.set_latitude(place_data['latitude'])
        if 'longitude' in place_data:
            error_message = place.set_longitude(place_data['longitude'])

        if error_message:
            return None, error_message

        self.place_repo.update(place_id, place)
        return place, None

    def create_amenity(self, amenity_data):
        # Placeholder for logic to create an amenity
        pass

    def get_amenity(self, amenity_id):
        # Placeholder for logic to retrieve an amenity by ID
        pass

    def get_all_amenities(self):
        # Placeholder for logic to retrieve all amenities
        pass

    def update_amenity(self, amenity_id, amenity_data):
        # Placeholder for logic to update an amenity
        pass
