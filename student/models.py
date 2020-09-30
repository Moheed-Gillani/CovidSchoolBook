
from django.db import models

# Create your models here.

# table to add School deatails
class School(models.Model):
    school_name=models.CharField(max_length=100)
    location=models.CharField(max_length=400)
    owner_name=models.CharField(max_length=200)
    owner_contact=models.CharField(max_length=12)
    def __str__(self):
        return self.school_name

    # method to return total number of teachers teaching in Schhol
    def total_Teachers(self):
        return self.school_teacher.all().count()
        
    # method to return total number of Students studing in School
    def total_students(self):
        return self.school_students.all().count()

# Model for grade to acess student class in which they are studing
class Grade(models.Model):
    school_grade=models.IntegerField(default=0)
    def __str__(self):
        return str(self.school_grade)
        # method to return teachers who are teaching these classes
    def these_grade_student__Teachers(self):
        return self.teacher_set.all()

# student table to add student
class Student(models.Model):
 
    photo=models.ImageField(upload_to='students',blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE,blank=True,null=True)
    name=models.CharField(max_length=100)
    Covid_19=models.BooleanField(default=False,editable=True,blank=True)
    gaurdain_name=models.CharField(max_length=100)
    Guardain_contact= models.CharField(max_length=12)
    rollno=models.IntegerField(default=0)
    joined=models.DateField()
    grade=models.ForeignKey(Grade,on_delete=models.CASCADE,default=0)
    address=models.CharField(max_length=100,blank=True)
    def __str__(self):
        return self.name
    # method to return class of student in which they are currently in
    def student_of_grade(self):
        return self.grade



# Subjects of differnt teachers
class Subject(models.Model):
    sub_name=models.CharField(max_length=100)
    def __str__(self):
        return  self.sub_name  

# table to add teacher in database
class Teacher(models.Model):
    gender=(
        ('M','Male'),
        ('F','Female'),
    )
    photo=models.ImageField(upload_to='teachers',blank=True)
    school=models.ForeignKey(School,on_delete=models.CASCADE,null=True)
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,choices=gender)
    Covid_19=models.BooleanField(default=False,editable=True,blank=True)
    email=models.EmailField()
    contact= models.CharField(max_length=12)
    subjects=models.ManyToManyField(Subject,)
    address=models.CharField(max_length=100,blank=True)
    grade=models.ManyToManyField(Grade,)
    def __str__(self):
        return  self.name
    # method to return the teacher subject which they teaching
    def teacher_has_subject(self):
        return self.subjects.all()
#    method to return name  of class which they are teaching
    def teach_student_of_grade(self):
        return self.grade.all()


    