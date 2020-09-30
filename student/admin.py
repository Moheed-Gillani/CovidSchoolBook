from django.contrib import admin
from student.models import  Student,Subject,Teacher,Grade,School
# Register your models here.
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Grade)
admin.site.register(School)
