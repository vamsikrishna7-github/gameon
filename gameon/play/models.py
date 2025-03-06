from django.db import models
from decimal import Decimal
from django.core.validators import MaxValueValidator

class UsersInfo(models.Model):
    id = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    password = models.CharField(max_length=50, null=False)
    level = models.IntegerField(default=0, validators=[MaxValueValidator(1000)])
    score = models.DecimalField(decimal_places=4, max_digits=10, default=0.0)

class QuestionBank(models.Model):
    id = models.AutoField(primary_key=True)
    q_name = models.CharField(max_length=2555, null=False)
    answer = models.CharField(max_length=2555, null=False)

