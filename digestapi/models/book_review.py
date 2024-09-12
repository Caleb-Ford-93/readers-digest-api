# Table Book_Review {
#   id int pk
#   book_id int [ref: > Book.id]
#   auth_user varchar [ref: > User.id]
#   rating int
#   comment text
#   posted_date datetime
# }

from django.db import models
from django.contrib.auth.models import User


class Book_Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_created"
    )
    book_id = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="Book")
    rating = models.IntegerField()
    comment = models.CharField(max_length=400)
    posted_date = models.DateField(auto_now_add=True)
