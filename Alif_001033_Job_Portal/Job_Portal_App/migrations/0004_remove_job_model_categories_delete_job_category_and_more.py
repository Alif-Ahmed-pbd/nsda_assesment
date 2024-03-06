# Generated by Django 5.0.3 on 2024-03-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Portal_App', '0003_job_category_job_model_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_model',
            name='categories',
        ),
        migrations.DeleteModel(
            name='job_category',
        ),
        migrations.AddField(
            model_name='job_model',
            name='categories',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
