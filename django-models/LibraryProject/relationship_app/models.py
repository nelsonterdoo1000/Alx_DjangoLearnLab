from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.title} by {self.author}"

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name
    
class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} | {self.library}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    ROLE_CHOICES = [
        ('Admin','Admin'),
        ('Member','Member'),
        ('Librarian','Librarian'),
    ]
    role = models.CharField(max_length=20,choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username}'s Profile"