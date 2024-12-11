#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, page_number, progress_status, rating, genre, date_added):
        self.title = title
        self.author = author
        self.page_number = page_number
        self.progress_status = progress_status
        self.rating = rating
        self.genre = genre
        self.date_added = date_added

    @property
    def summary(self):
        """Return a formatted summary of the book."""
        return f"'{self.title}' by {self.author}, Genre: {self.genre}, Rating: {self.rating}/5"

    @staticmethod
    def validate_rating(rating):
        """Ensure the rating is between 1 and 5."""
        if 1 <= rating <= 5:
            return True
        raise ValueError("Rating must be between 1 and 5.")

    @staticmethod
    def validate_progress_status(status):
        """Ensure the progress status is valid."""
        valid_statuses = ["Not Started", "In Progress", "Completed"]
        if status in valid_statuses:
            return True
        raise ValueError(f"Invalid progress status. Choose from: {', '.join(valid_statuses)}")
