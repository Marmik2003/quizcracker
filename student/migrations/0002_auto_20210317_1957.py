# Generated by Django 3.1.7 on 2021-03-17 14:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testtaken',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='testtaken',
            name='test',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.test'),
        ),
        migrations.AddField(
            model_name='studentresponse',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.option'),
        ),
        migrations.AddField(
            model_name='studentresponse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
