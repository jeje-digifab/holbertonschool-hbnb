from app.persistence.repository import InMemoryRepository


class HBnBFacade:
    def __init__(self):
        self.user_repo = InMemoryRepository()
        self.place_repo = InMemoryRepository()
        self.review_repo = InMemoryRepository()
        self.amenity_repo = InMemoryRepository()

    # Placeholder method for creating a user
    def create_user(self, user_data):
        # Logic will be implemented in later tasks
        pass

    # Placeholder method for fetching a place by ID
    def create_place(self, place_data):
        """
        Logic to create a place,
        including validation for price, latitude, and longitude.
        """
        title = place_data.get('title')
        price = place_data.get('price')
        latitude = place_data.get('latitude')
        longitude = place_data.get('longitude')
        owner_id = place_data.get('owner_id')
        amenities = place_data.get('amenities')

        new_place = Place(title=title, price=price, latitude=latitude,
                          longitude=longitude, owner_id=owner_id)

        if amenities:  # Check if amenities are provided
            new_place.amenities = []  # Initialize the amenities attribute
            for amenity_id in amenities:
                amenity = self.get_amenity_by_id(amenity_id)
                if amenity:
                    new_place.amenities.append(amenity)

        # Store the new Place object in the repository
        self.place_repo.save(new_place)

        return new_place

    def get_place(self, place_id):
        """
        Retrieve a place by ID, including associated owner and amenities.
        """
        return self.place_repo.get_by_id(place_id)

    def get_all_places(self):
        """
        Retrieve all places stored in memory.
        """
        return self.place_repo.get_all()

    def update_place(self, place_id, place_data):
        """
        Update a place's information if it exists.
        """
        place = self.place_repo.get_by_id(place_id)
        if not place:
            raise ValueError("Place not found")

        # Update place attributes if provided in place_data
        if 'title' in place_data:
            place.title = place_data['title']
        if 'price' in place_data:
            place.price = place_data['price']
        if 'latitude' in place_data:
            place.latitude = place_data['latitude']
        if 'longitude' in place_data:
            place.longitude = place_data['longitude']
        if 'owner_id' in place_data:
            place.owner_id = place_data['owner_id']
        if 'amenities' in place_data:
            place.amenities = place_data['amenities']

        # Save the updated place
        self.place_repo.save(place)

        return place
