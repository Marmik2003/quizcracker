from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from student.models import StudentResponse, TestTaken
from teacher.models import Test, Option
from .models import TestTaken


@login_required
def student_index(request):
    if request.method != 'POST':
        exams = Test.objects.filter(
            test_start_time__gte=(timezone.now()),
        ).exclude(testtaken__student=request.user,)
        return render(request, 'student-index.html', context={
            'exams': exams
        })


@login_required
def student_past_exams(request):
    if request.method != 'POST':
        exams = Test.objects.filter(
            test_start_time__lte=(timezone.now()),
        ).union(Test.objects.filter(testtaken__student=request.user))
        return render(request, 'student-past-exam.html', context={
            'exams': exams
        })


@login_required
def student_exam(request, exam_id):
    if request.method != 'POST':
        if exam_id in list(request.user.testtaken_set.values_list('test_id', flat=True)):
            messages.error(request, 'Sorry, you can\'t take test second time!')
            return redirect('student_index')
        else:
            test_trial = Test.objects.get(id=exam_id)
            return render(request, 'student-exam.html',
                          context={'test': test_trial})


@login_required
def exam_result(request, test_id):
    if request.method != 'POST':
        test_taken = TestTaken.objects.get(
            test_id=test_id,
            student=request.user
        )
        test = test_taken.test
        total_q = test.question_set.count()
        wrong_a = int(total_q) - int(test_taken.points)
        return render(request, 'exam_result.html', context={
            'test_taken': test_taken,
            'test': test,
            'total_q': total_q,
            'wrong_a': wrong_a
        })


@login_required
def ajax_submit(request):
    option_list = request.GET.getlist('option_list[]')
    test_id = request.GET.get('test_id')
    print(option_list)
    marks = 0
    test = Test.objects.get(id=test_id)
    for option_id in option_list:
        option = Option.objects.get(id=option_id)
        question = option.question
        StudentResponse.objects.create(
            student=request.user,
            answer=option
        )
        if option.id == question.correct_option.id:
            marks += 1
        else:
            pass

    TestTaken.objects.create(
        student=request.user,
        test=test,
        points=marks
    )
    return HttpResponse("ResultChecked Successfully! serverpass")
