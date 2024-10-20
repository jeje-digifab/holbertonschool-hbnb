from app.models.BaseModel import BaseModel
from app.models.user import User
from app.models.place import Place


class Review(BaseModel):
    """
    A class representing a review for a place.

    Attributes:
    ----------
    text : str
        The content of the review.
    rating : int or float
        The rating of the place, which must be between 1 and 5.
    place : Place
        The place that is being reviewed.
        Must be an instance of the Place class.
    user : User
        The user who made the review. Must be an instance of the User class.
    """

    def __init__(self, text, rating, place, user):
        """
        Initializes a new Review instance.
        """
        super().__init__()

        if not isinstance(user, User):
            raise ValueError("User must be an instance of User.")

        if not isinstance(place, Place):
            raise ValueError("Place must be an instance of Place.")

        self.text = text
        self.rating = rating
        self.place = place
        self.user = user

    def set_text(self, text):
        """
        Sets the text for the review and saves the changes.
        """
        if not isinstance(text, str):
            raise ValueError("The text must be a string.")

        self.text = text
        self.save()

    def set_rating(self, rating):
        """
        Sets the rating for the review and saves the changes.
        """
        if not isinstance(rating, (int, float)):
            raise ValueError("The rating must be an integer or float.")

        if rating < 1 or rating > 5:
            raise ValueError("Rating must be between 1 and 5.")

        self.rating = rating
        self.save()
