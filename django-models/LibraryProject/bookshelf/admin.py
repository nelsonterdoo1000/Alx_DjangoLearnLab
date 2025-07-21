from django.contrib import admin

from .models import Book, Department, Employee, Product, ProductDetail, Student, Course

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name',)
    search_fields = ('course_name',)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductDetailAdmin(admin.ModelAdmin):
    list_display = ('product_name','description')
    search_fields = ('product_name',)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name','departments')
    search_fields = ('name','departments')
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_year')
    search_fields = ('title','author','publication_year')
    list_filter = ('title',)


admin.site.register(Book,BookAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(ProductDetail,ProductDetailAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Course,CourseAdmin)