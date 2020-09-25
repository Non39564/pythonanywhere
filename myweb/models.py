import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return timezone.now() - datetime.timedelta(days=1) <= self.pub_date <= timezone.now()

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class displayusername(models.Model):
    username = models.CharField(max_length=200)

    def __str__(self):
        return self.username

class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Product(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    customer_name = models.CharField(max_length=120)
    email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    details = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
