from app.models.user import User
from app.models.review import Review
from app.models.place import Place


def test_review_creation():
    """
    Test the creation of a Review object with valid attributes and
    relationships to a User and a Place.

    This test verifies:
    - The attributes of the Review object are correctly initialized.
    - The relationships between the Review, Place, and User objects
    are functioning as expected.
    """
    # Create an instance of User for the test
    user = User(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        password="securepassword"
    )

    # Create an instance of Place for the test
    place = Place(
        title="Test Place",
        description="A beautiful place to stay.",
        price=100.0,
        latitude=37.7749,
        longitude=-122.4194,
        owner=user
    )

    # Create an instance of Review
    review = Review(text="Great place!", rating=5, place=place, user=user)

    # Verify that the attributes are correctly defined
    assert review.text == "Great place!"
    assert review.rating == 5
    assert review.place == place
    assert review.user == user
    print("Review creation test passed!")


def test_set_text():
    """
    Test the 'set_text' method of the Review object.

    This test verifies that:
    - The text of the Review can be modified using the set_text method.
    """
    user = User(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        password="securepassword"
    )
    place = Place(
        title="Test Place",
        description="A beautiful place to stay.",
        price=100.0,
        latitude=37.7749,
        longitude=-122.4194,
        owner=user
    )
    review = Review(text="Great place!", rating=5, place=place, user=user)

    # Modify the text of the review
    review.set_text("Amazing place!")
    assert review.text == "Amazing place!"
    print("Set text test passed!")


def test_set_rating():
    """
    Test the 'set_rating' method of the Review object.

    This test verifies that:
    - The rating of the Review can be modified using the set_rating method.
    """
    user = User(
        first_name="Test",
        last_name="User",
        email="test@example.com",
        password="securepassword"
    )
    place = Place(
        title="Test Place",
        description="A beautiful place to stay.",
        price=100.0,
        latitude=37.7749,
        longitude=-122.4194,
        owner=user
    )
    review = Review(text="Great place!", rating=5, place=place, user=user)

    # Modify the rating of the review
    review.set_rating(4)
    assert review.rating == 4
    print("Set rating test passed!")


# Run the tests
test_review_creation()
test_set_text()
test_set_rating()
