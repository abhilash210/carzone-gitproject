from django.db import models

class Team(models.Model):
    fristname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    photo=models.ImageField(upload_to='photos/%y/%m/%d/')
    facebook_link=models.URLField(max_length=100)
    Twitter_link=models.URLField(max_length=100)
    google_plus_link=models.URLField(max_length=100)
    def __str__(self):
        return self.fristname


