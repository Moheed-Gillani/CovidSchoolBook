from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from student.models import *
from django.views.generic.edit import CreateView,FormView,UpdateView,DeleteView
from django.views.generic import ListView,DetailView
from student.forms import Studentform,TeacherForm,SchoolForm
from django.shortcuts import get_object_or_404

# view the list of tidents
class StudentList(ListView):
    queryset=Student.objects.order_by('joined')
    template_name='student/student_list.html'

# view for  the details of particular student with there id 
class ClassListStudent(DetailView):
    model=Grade
    template_name='student/class_of_student.html'

# view for  the details of particular student with there teachers
class ClassListTeacher(DetailView):
    model=Grade
    template_name='student/class_of_teachers.html'


class StudentDetail(DetailView):
    model=Student
    context_object_name='students'
    template_name='student/student_detail.html'

# view to update the student record
class UpdateStudent(UpdateView):
    model=Student
    fields=['photo','name','school','Covid_19','gaurdain_name','Guardain_contact','rollno','joined','grade','address']
    template_name='student/add_student.html'
    success_url='/Students'
# view to delete the student record
class DeleteStudent(DeleteView):
    model=Student
    template_name='student/student_confirm_delete.html'
    success_url='/Students'


# view to get the lis of teachers
class TeacherList(ListView):
    model=Teacher
    template_name='employer/teacher_list.html'

# view to get the details of particular teachers
class TeacherDetail(DetailView):
    model=Teacher
    context_object_name='teachers'
    template_name='employer/teachers_detail.html'

class UpdateTeacher(UpdateView):
    model=Teacher
    fields=['photo','name','school','Covid_19','gender','email','contact','subjects','address','grade']
    template_name='employer/add_teacher.html'
    success_url='/teacher'

#view to delete the teachers
class DeleteTeacher(DeleteView):
    model=Teacher
    template_name='employer/teacher_confirm_delete.html'
    success_url='/teacher'

# view to add the student records
class AddStudent(CreateView):
    model=Student
    template_name='student/add_student.html'
    fields=['photo','name','school','Covid_19','gaurdain_name','Guardain_contact','rollno','joined','grade','address']
    success_url='/Students'

# views to add teachers records
class AddTeacher(CreateView):
    model=Teacher
    template_name='employer/add_teacher.html'
    fields=['photo','name','school','Covid_19','gender','email','contact','subjects','address','grade']
    success_url='/teacher'
     
 # views to add school records   
class SchoolList(ListView):
    model=School
    template_name='school/school_list.html'

# view to add the school records
class AddSchool(CreateView):
    model=School
    template_name='school/add_school.html'
    fields=['school_name','location','owner_name','owner_contact']
    success_url='/school_list'

# view to update the school records
class UpdateSchool(UpdateView):
    model=School
    fields=['school_name','location','owner_name','owner_contact']
    template_name='school/add_school.html'
    success_url='/school_list'


# view to Delete the school records
class DeleteSchool(DeleteView):
    model=School
    template_name='school/school_confirm_delete.html'
    success_url='/school_list'
