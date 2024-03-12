from django.db import models


class Students(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)

    class Meta:
        db_table = "wanafunzi"


class Teachers(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)


class Docters(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)


class Parents(models.Model):
    FirstName = models.CharField(max_length=20)
    LastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    age = models.IntegerField()
    id_no = models.IntegerField()
    contact = models.CharField(max_length=10)
    date_of_birth = models.DateField()


class Post(models.Model):
    Title = models.CharField(max_length=25)
    Description = models.CharField(max_length=100)
    Author = models.CharField(max_length=25)
    Time = models.DateTimeField(max_length=15)

    def _str_(self):
        return self.Title
