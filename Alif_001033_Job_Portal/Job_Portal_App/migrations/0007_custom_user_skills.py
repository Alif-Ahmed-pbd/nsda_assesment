# Generated by Django 5.0.3 on 2024-03-06 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_Portal_App', '0006_remove_recruiterprofile_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='skills',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
