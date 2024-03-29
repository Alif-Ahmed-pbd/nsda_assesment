from django.db import models
from django.utils import timezone

from django.contrib.auth.models import AbstractUser

class Custom_User(AbstractUser):
    USER=[
        ('recruiter','Recruiter'),('jobseeker','JobSeeker')
    ]
    display_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    user_type=models.CharField(choices=USER,max_length=120)
    profile_pic=models.ImageField(upload_to="media/profile_pic",null=True)
    about= models.TextField(max_length=10000,null=True)
    post = models.CharField(max_length = 100, null = True)
    company_name = models.CharField(max_length = 100, null = True)
    skills=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.display_name
    





class job_model(models.Model):
    job_title = models.CharField(max_length=100, null=True)
    number_of_openings = models.CharField(max_length=100, null=True)
    location = models.CharField(max_length=100, null=True)
    description = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)
    job_creator = models.ForeignKey(Custom_User, on_delete=models.CASCADE)
    skills = models.TextField(null = True )
    categories = models.CharField(max_length=30, null=True)


    def __str__(self):
        return self.job_title
        
class jobApplyModel(models.Model):
    
    job=models.ForeignKey(job_model,on_delete=models.CASCADE,related_name='applications')
    applicant=models.ForeignKey(Custom_User,on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    skills = models.CharField(max_length=255, blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.applicant.display_name} applied for {self.job.job_title}"

class RecruiterProfile(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True, related_name='recruiterprofile')

    def __str__(self):
        return self.user.display_name
    

class JobSeekerProfile(models.Model):
    user = models.OneToOneField(Custom_User,on_delete=models.CASCADE,null=True, related_name='jobseekerprofile')
    
    skills=models.CharField(max_length=100,null=True)
    
    def __str__(self):
        return self.user.display_name