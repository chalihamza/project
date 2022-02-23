from django.db import models


class Team(models.Model):
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Designation = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos/%Y/%M/%d/')
    facebook = models.URLField(max_length=250)
    google = models.URLField(max_length=250)
    twitter = models.URLField(max_length=250)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.FirstName
