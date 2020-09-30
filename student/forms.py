from django import forms
from django.urls import reverse
from django.forms import ModelForm
from django.contrib.auth.models import User
from student.models import Student,Teacher,Grade,Subject,School




class Studentform(forms.Form):
    
    name=forms.CharField(max_length=200)
    gaurdain_name=forms.CharField(max_length=100)
    Guardain_contact= forms.CharField(max_length=12)
    rollno=forms.IntegerField()
    joined=forms.DateField()
    grade=forms.ModelChoiceField(queryset=Grade.objects.all())
    fee=forms.DecimalField(max_digits=10,decimal_places=2)
class TeacherForm(forms.Form):
    gender=(
        ('M','Male'),
        ('F','Female'),
        )

    name=forms.CharField(max_length=100)
    gender=forms.CharField(max_length=10,widget=forms.Select(choices=gender))
    email=forms.EmailField()
    contact= forms.CharField(max_length=12)
    subjects=forms.ModelMultipleChoiceField(queryset=Subject.objects.all())
    salary=forms.DecimalField(max_digits=10,decimal_places=2)
    grade=forms.ModelMultipleChoiceField(queryset=Grade.objects.all())

class SchoolForm(forms.Form):
     school_name=forms.CharField(max_length=100)
     location=forms.CharField(max_length=400)
     owner_name=forms.CharField(max_length=200)
     owner_contact=forms.CharField(max_length=12)
     school_teacher=forms.ModelMultipleChoiceField(queryset=Teacher.objects.all())
     school_students=forms.ModelMultipleChoiceField(queryset=Student.objects.all())




