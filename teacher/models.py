from django.db import models

# Create your models here.


class Subject(models.Model):
    subject_name = models.CharField(max_length=100)


class Test(models.Model):
    test_name = models.CharField(max_length=150)
    test_start_time = models.DateTimeField()
    # test_end_time = models.DateTimeField()
    test_total_mins = models.IntegerField()
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)
    students = models.ManyToManyField('user.User')

    def __str__(self):
        return self.test_name


class Question(models.Model):
    question_text = models.TextField()
    subject = models.ForeignKey('teacher.Subject', on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=15)
    correct_option = models.ForeignKey('Option', on_delete=models.SET_NULL, related_name='correct_ans', null=True)
    test = models.ForeignKey('Test', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.question_text[:30] + '...'


class Option(models.Model):
    option_text = models.CharField(max_length=150)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
