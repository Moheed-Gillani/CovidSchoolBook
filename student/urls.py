from django.urls import path,include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from sms import settings
from student.views import *
urlpatterns=[
    path('',TemplateView.as_view(template_name='admin/me.html'),name='about-me'),
    # view the list of students
    path('Students',StudentList.as_view(),name='student_list'),

    # view to add the student records
    path('add_student',AddStudent.as_view(),name='add_student'),
    # view to update the student records
    path('update_student/<int:pk>',UpdateStudent.as_view(),name='update_student'),
    # view to delete the student records
    path('delete_student/<int:pk>',DeleteStudent.as_view(),name='delete_student'),
    # view to list the student records details
    path('details/<int:pk>',StudentDetail.as_view(),name='student_detail'),
    # view to list the teacher records
    path('teacher',TeacherList.as_view(),name='teacher_list'),
    # view to add the teacher records
    path('add_teacher',AddTeacher.as_view(),name='add_teacher'),
    #view to update the teacher
    path('update_teacher/<int:pk>',UpdateTeacher.as_view(),name='update_teacher'),
    #view to delete teachers
    path('delete_teachers/<int:pk>',DeleteTeacher.as_view(),name='delete_teacher'),
    # view to list the teacher details of records records
    path('teacher/<int:pk>',TeacherDetail.as_view(),name='teacher_detail'),
    #view to show the school records
    path('school_list',SchoolList.as_view(),name='school_list'),
    # view to add the school records
    path('add_school',AddSchool.as_view(),name='add_school'),
    # view to update the school records
    path('update_school/<int:pk>',UpdateSchool.as_view(),name='update_school'),
    # view to delete the school records
    path('delete_school/<int:pk>',DeleteSchool.as_view(),name='delete_school'),
    #about me
    #view to filter students by grades
    path('Student_of_class/<int:pk>',ClassListStudent.as_view(),name='class-list'),
    #view to filter teachers by grades
    path('teacher_of_class/<int:pk>',ClassListTeacher.as_view(),name='class-list-teacher'),
    #view to create authentication syestem
    #login views
    path('accounts/login/',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    #logout views
    path('accounts/logout/',auth_views.LogoutView.as_view(),name='logout'),
    #password change
    path('accounts/password_change/',auth_views.PasswordChangeView.as_view(template_name='accounts/change_password.html'),name='password_change'),
    #password_change_done
    path('accounts/password_change/done',auth_views.PasswordChangeDoneView.as_view(template_name='accounts/password_change_confirm.html'),name='password_change_done'),  
    #register user
  
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)