from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    summary = models.TextField()
    genre = models.CharField(max_length=200)

    def __str__(self):
        return self.title