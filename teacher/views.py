from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect

from .models import Subject, Option, Question, Test

# Create your views here.


@login_required
@user_passes_test(lambda u: u.is_staff)
def teacher_dashboard(request):
    if request.method != 'POST':
        last_test = Test.objects.last()
        tests = Test.objects.all()
        return render(request, 'teacher-layout.html', context={
            'last_test': last_test,
            'tests': tests
        })


@login_required
@user_passes_test(lambda u: u.is_staff)
def set_subjects_tch(request):
    if request.method != 'POST':
        subjects = Subject.objects.all()
        return render(request, 'teacher-subjects.html', context={'subjects': subjects})
    else:
        subject = request.POST['subject']
        Subject.objects.create(
            subject_name=subject
        )
        return redirect('set_subjects_tch')


@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_subjects_tch(request, sub_id):
    if request.method != 'POST':
        subjects = Subject.objects.all()
        subject = Subject.objects.get(id=sub_id)
        return render(request, 'teacher-subjects.html', context={
            'subjects': subjects,
            'subject': subject,
        })
    else:
        subject = request.POST['subject']
        Subject.objects.filter(id=sub_id).update(
            subject_name=subject
        )
        return redirect('set_subjects_tch')


@login_required
@user_passes_test(lambda u: u.is_staff)
def delete_subject(request, sub_id):
    sub = Subject.objects.get(id=sub_id)
    sub.delete()
    return redirect('set_subjects_tch')


@login_required
@user_passes_test(lambda u: u.is_staff)
def set_questions_tch(request):
    if request.method != 'POST':
        subjects = Subject.objects.all()
        questions = Question.objects.all()
        return render(request, 'teacher-questions.html', context={
            'subjects': subjects,
            'questions': questions
        })
    else:
        subject_name = request.POST['subject_name']
        difficulty = request.POST['difficulty']
        question_name = request.POST['question_name']
        option_1 = request.POST['option_1']
        option_2 = request.POST['option_2']
        option_3 = request.POST['option_3']
        option_4 = request.POST['option_4']
        correct_ans = request.POST['correct_ans']

        question = Question.objects.create(
            subject_id=subject_name,
            difficulty=difficulty,
            question_text=question_name,
        )

        option_1_data = Option(question=question, option_text=option_1)
        option_2_data = Option(question=question, option_text=option_2)
        option_3_data = Option(question=question, option_text=option_3)
        option_4_data = Option(question=question, option_text=option_4)
        option_1_data.save()
        option_2_data.save()
        option_3_data.save()
        option_4_data.save()
        if correct_ans == '1':
            question.correct_option = option_1_data
        elif correct_ans == '2':
            question.correct_option = option_2_data
        elif correct_ans == '3':
            question.correct_option = option_3_data
        elif correct_ans == '4':
            question.correct_option = option_4_data

        question.save()
        return redirect('set_questions_tch')


@login_required
@user_passes_test(lambda u: u.is_staff)
def edit_questions_tch(request, q_id):
    if request.method != 'POST':
        subjects = Subject.objects.all()
        questions = Question.objects.all()
        question = Question.objects.get(id=q_id)
        options = Option.objects.filter(question=question)
        return render(request, 'teacher-question-edit.html', context={
            'subjects': subjects,
            'questions': questions,
            'question': question,
            'options': options
        })
    else:
        subject_name = request.POST['subject_name']
        difficulty = request.POST['difficulty']
        question_name = request.POST['question_name']
        option_1 = request.POST['option_1']
        option_2 = request.POST['option_2']
        option_3 = request.POST['option_3']
        option_4 = request.POST['option_4']
        correct_ans = request.POST['correct_ans']

        Question.objects.filter(id=q_id).update(
            subject_id=subject_name,
            difficulty=difficulty,
            question_text=question_name,
        )
        question = Question.objects.get(id=q_id)
        Option.objects.filter(question_id=q_id).delete()
        option_1_data = Option(question=question, option_text=option_1)
        option_2_data = Option(question=question, option_text=option_2)
        option_3_data = Option(question=question, option_text=option_3)
        option_4_data = Option(question=question, option_text=option_4)
        option_1_data.save()
        option_2_data.save()
        option_3_data.save()
        option_4_data.save()
        if correct_ans == '1':
            question.correct_option = option_1_data
        elif correct_ans == '2':
            question.correct_option = option_2_data
        elif correct_ans == '3':
            question.correct_option = option_3_data
        elif correct_ans == '4':
            question.correct_option = option_4_data

        question.save()
        return redirect('set_questions_tch')


@login_required
@user_passes_test(lambda u:u.is_staff)
def delete_question(request, q_id):
    Question.objects.get(id=q_id).delete()
    return redirect('set_questions_tch')


@login_required
@user_passes_test(lambda u: u.is_staff)
def set_exam_tch(request):
    if request.method != 'POST':
        subjects = Subject.objects.all()
        questions = Question.objects.all()
        return render(request, 'teacher-exams.html', context={
            'subjects': subjects,
            'questions': questions,
        })
    else:

        test_title = request.POST['test_title']
        subject = request.POST['subject']
        test_date = request.POST['test_date']
        test_start_time = request.POST['test_start_time']
        test_dur = request.POST['test_dur']

        questions = {i: val for i, val in request.POST.items() if i.startswith('question_')}

        test = Test.objects.create(
            test_name=test_title,
            subject_id=subject,
            test_start_time=(test_date+' '+test_start_time),
            test_total_mins=test_dur
        )
        for question in questions:
            q1 = Question.objects.get(id=questions[question])
            q1.test = test
            q1.save()
        messages.success(request, 'Test scheduled!')
        return redirect('set_exam_tch')


@login_required
@user_passes_test(lambda u: u.is_staff)
def view_result_tch(request):
    if request.method != 'POST':
        tests = Test.objects.all()
        return render(request, 'teacher-results.html', context={
            'tests': tests
        })
