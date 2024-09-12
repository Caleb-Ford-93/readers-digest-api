# Table Book_Categories {
#   id int pk
#   category_id int [ref: > Category.id]
#   book_id int [ref: > Book.id]
#   created_at timestamp
# }

from django.db import models


class Book_Category(models.Model):
    category_id = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="categories"
    )
    book_id = models.ForeignKey("Book", on_delete=models.CASCADE, related_name="books")
    created_at = models.DateField(auto_now_add=True)
