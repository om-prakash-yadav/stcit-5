from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length = 254,null=True)
    name = models.CharField(max_length=128)
    current_question = models.IntegerField(default=1)
    score = models.IntegerField(default=0)
    final_score = models.IntegerField(default=0)
    rank = models.IntegerField(default=0)
    timestamp = models.DateTimeField()
    slot = models.IntegerField(default=0)
    qualified = models.BooleanField(default=False)
    details_updated = models.BooleanField(default=False)

    mobile = models.CharField(max_length=13,null=True)

    year_of_study_choices = (
        ('Class 9', 'class 9'),
        ('Class 10', 'class 10'),
        ('Class 11', 'class 11'),
        ('Class 12', 'class 12'),
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
        ('5th Year', '5th Year'),
        ('Other','Other')
    )
    institute_name = models.CharField(max_length=100,null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    year_of_study = models.CharField(max_length=50, choices=year_of_study_choices, default="1st Year")
    
    def __str__(self):
        return self.name

class question(models.Model):
    Q_number = models.IntegerField()
    Question = models.TextField()
    image = models.ImageField(upload_to='images', blank=True)
    option1 = models.CharField(max_length=200, null=True)
    option2 = models.CharField(max_length=200, null=True)
    option3 = models.CharField(max_length=200, null=True)
    option4 = models.CharField(max_length=200, null=True)
    answer = models.CharField(max_length=200)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    accuracy = models.FloatField(default=0)

    def __str__(self):
        return str(self.Q_number) + " " + self.Question