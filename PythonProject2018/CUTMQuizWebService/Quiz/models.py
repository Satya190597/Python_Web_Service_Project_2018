from django.db import models

# Question Bank Model
class QuestionBank(models.Model):
    question = models.CharField(max_length=250)
    category = models.CharField(max_length=250)
    option_one = models.CharField(max_length=250)
    option_two = models.CharField(max_length=250)
    option_three = models.CharField(max_length=250)
    option_four = models.CharField(max_length=250)
    ans = models.CharField(max_length=250)
