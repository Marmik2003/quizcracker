from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_dashboard, name='teacher_dashboard'),
    path('subjects', views.set_subjects_tch, name='set_subjects_tch'),
    path('subjects/delete/<int:sub_id>', views.delete_subject, name='delete_subject'),
    path('subjects/edit/<int:sub_id>', views.edit_subjects_tch, name='edit_subjects_tch'),
    path('questions', views.set_questions_tch, name='set_questions_tch'),
    path('questions/edit/<int:q_id>', views.edit_questions_tch, name='edit_questions_tch'),
    path('questions/delete/<int:q_id>', views.delete_question, name='delete_question'),
    path('exams', views.set_exam_tch, name='set_exam_tch'),
    path('results', views.view_result_tch, name='view_result_tch'),
]
