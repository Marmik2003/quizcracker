from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_index, name='student_index'),
    path('past_exams', views.student_past_exams, name='student_past_exams'),
    path('exam_portal/<int:exam_id>', views.student_exam, name='student_exam'),
    path('exam_check', views.ajax_submit, name='ajax_submit'),
    path('exam_result/<int:test_id>', views.exam_result, name='exam_result'),
]