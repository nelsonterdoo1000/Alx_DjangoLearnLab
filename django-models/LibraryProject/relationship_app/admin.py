from django.contrib import admin
from .models import UserProfile,Librarian,Library,Book

admin.site.register(UserProfile)
admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(Book)

