import pytest
from app.models.place import Place
from app.models.user import User
from app.models.review import Review


def test_place_creation():
    """
    Test the creation of a Place object and its relationship
    with a Review and a User object.

    This test checks that:
    - A Place object is correctly created with the provided attributes.
    - A Review object can be associated with a Place.
    - The relationship between Place and Review works as expected.
    """

    # Create a user (owner of the place)
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")

    # Create a place with given details and an owner
    place = Place(title="Cozy Apartment",
                  description="A nice place to stay",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Create a review associated with the place and the user owner
    review = Review(text="Great stay!", rating=5, place=place, user=owner)

    # Add the review to the place
    place.add_review(review)

    # Assertions to verify the attributes are correctly initialized
    assert place.title == "Cozy Apartment"
    assert place.price == 100
    assert len(place.reviews) == 1
    assert place.reviews[0].text == "Great stay!"
    print("Place creation and relationship test passed!")


def test_place_creation_with_invalid_owner():
    """
    Test the creation of a Place object with an invalid owner (None).

    This test checks that:
    - Creating a Place without a valid owner raises a ValueError.
    - The error message matches the expected value.
    """
    # Use pytest to check that the exception is raised
    with pytest.raises(ValueError) as excinfo:
        place = Place(title="Invalid Place",
                      description="This should fail",
                      price=100, latitude=37.7749,
                      longitude=-122.4194,
                      owner=None)

    # Verify that the error message matches
    assert str(excinfo.value) == "Owner must be an instance of User."
    print("Invalid owner test passed!")


def test_set_title():
    """
    Test the set_title method with valid and invalid inputs.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Valid title
    assert place.set_title("New Title") is None
    assert place.title == "New Title"

    # Title too long
    assert place.set_title("A" * 101) == "The title is too long."

    # Title not a string
    assert place.set_title(12345) == "Title must be a non-empty string."

    # Empty title
    assert place.set_title("") == "Title must be a non-empty string."


def test_set_description():
    """
    Test the set_description method with valid and invalid inputs.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Valid description
    assert place.set_description("New Description") is None
    assert place.description == "New Description"

    # Description not a string
    assert place.set_description(12345) == "The description must be a string."


def test_set_price():
    """
    Test the set_price method with valid and invalid inputs.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Valid price
    assert place.set_price(200) is None
    assert place.price == 200

    # Price not a number
    assert place.set_price("200") == "Price must be a positive number."

    # Price not positive
    assert place.set_price(-50) == "Price must be a positive number."

    # Price is zero
    assert place.set_price(0) == "Price must be a positive number."


def test_set_latitude():
    """
    Test the set_latitude method with valid and invalid inputs.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Valid latitude
    assert place.set_latitude(40.7128) is None
    assert place.latitude == 40.7128

    # Latitude not a number
    assert place.set_latitude(
        "40.7128") == "Latitude must be between -90 and 90."

    # Latitude out of range
    assert place.set_latitude(91) == "Latitude must be between -90 and 90."

    # Latitude at the boundary
    assert place.set_latitude(90) is None
    assert place.latitude == 90
    assert place.set_latitude(-90) is None
    assert place.latitude == -90


def test_set_longitude():
    """
    Test the set_longitude method with valid and invalid inputs.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Valid longitude
    assert place.set_longitude(-74.0060) is None
    assert place.longitude == -74.0060

    # Longitude not a number
    assert place.set_longitude(
        "74.0060") == "Longitude must be between -180 and 180."

    # Longitude out of range
    assert (place.set_longitude(-181) ==
            "Longitude must be between -180 and 180.")

    # Longitude at the boundary
    assert place.set_longitude(180) is None
    assert place.longitude == 180
    assert place.set_longitude(-180) is None
    assert place.longitude == -180


def test_add_multiple_reviews():
    """
    Test adding multiple reviews to a place.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    review1 = Review(text="Great stay!", rating=5, place=place, user=owner)
    review2 = Review(text="Awesome!", rating=4, place=place, user=owner)

    place.add_review(review1)
    place.add_review(review2)

    assert len(place.reviews) == 2
    assert place.reviews[0].text == "Great stay!"
    assert place.reviews[1].text == "Awesome!"


def test_add_multiple_amenities():
    """
    Test adding multiple amenities to a place.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    place.add_amenity("Wi-Fi")
    place.add_amenity("Pool")

    assert len(place.amenities) == 2
    assert "Wi-Fi" in place.amenities
    assert "Pool" in place.amenities


def test_set_title_special_cases():
    """
    Test the set_title method with special cases.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Title with special characters
    assert place.set_title("New Title!@#") is None
    assert place.title == "New Title!@#"

    # Empty title
    assert place.set_title("") == "Title must be a non-empty string."


def test_set_description_special_cases():
    """
    Test the set_description method with special cases.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Description with special characters
    assert place.set_description("New Description!@#") is None
    assert place.description == "New Description!@#"

    # Empty description
    assert place.set_description("") is None
    assert place.description == ""


def test_set_price_special_cases():
    """
    Test the set_price method with special cases.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Price as a float
    assert place.set_price(150.75) is None
    assert place.price == 150.75

    # Price as a very large number
    assert place.set_price(1e10) is None
    assert place.price == 1e10


def test_set_latitude_special_cases():
    """
    Test the set_latitude method with special cases.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Latitude as a float
    assert place.set_latitude(40.7128) is None
    assert place.latitude == 40.7128

    # Latitude at the boundary
    assert place.set_latitude(90) is None
    assert place.latitude == 90
    assert place.set_latitude(-90) is None
    assert place.latitude == -90


def test_set_longitude_special_cases():
    """
    Test the set_longitude method with special cases.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    # Longitude as a float
    assert place.set_longitude(-74.0060) is None
    assert place.longitude == -74.0060

    # Longitude at the boundary
    assert place.set_longitude(180) is None
    assert place.longitude == 180
    assert place.set_longitude(-180) is None
    assert place.longitude == -180


def test_add_multiple_reviews_and_amenities():
    """
    Test adding multiple reviews and amenities to a place.
    """
    owner = User(first_name="Alice", last_name="Smith",
                 email="alice.smith@example.com", password="password123")
    place = Place(title="Test Place", description="A test place",
                  price=100,
                  latitude=37.7749,
                  longitude=-122.4194,
                  owner=owner)

    review1 = Review(text="Great stay!", rating=5, place=place, user=owner)
    review2 = Review(text="Awesome!", rating=4, place=place, user=owner)

    place.add_review(review1)
    place.add_review(review2)

    assert len(place.reviews) == 2
    assert place.reviews[0].text == "Great stay!"
    assert place.reviews[1].text == "Awesome!"

    place.add_amenity("Wi-Fi")
    place.add_amenity("Pool")

    assert len(place.amenities) == 2
    assert "Wi-Fi" in place.amenities
    assert "Pool" in place.amenities
