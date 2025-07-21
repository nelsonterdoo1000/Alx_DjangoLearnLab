from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.title} by {self.author} published in {self.publication_year}"


class Department(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    name = models.CharField(max_length=200)
    departments = models.ForeignKey(Department,on_delete=models.CASCADE,related_name='departments')

    def __str__(self):
        return f"{self.name} in {self.departments}"


class Product(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class ProductDetail(models.Model):
    description = models.TextField()
    product_name = models.OneToOneField(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product_name} | {self.description}"

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    

class Course(models.Model):
    course_name = models.CharField(max_length=100,default=None)
    students = models.ManyToManyField(Student,related_name='course')
    def __str__(self):
        return f"{self.course_name}"