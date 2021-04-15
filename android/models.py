from django.db import models
from django.conf import settings
from .category import Choice


class App(models.Model):
    name = models.CharField(max_length = 100)
    applink = models.CharField(max_length = 200)
    app_category = models.CharField(max_length = 50, choices = Choice, default = Choice[0])
    sub_category = models.CharField(max_length = 50,choices = Choice, default = Choice[0])
    points = models.IntegerField(default = 0)
    img = models.FileField(upload_to = 'media')

    def __str__(self):
        return self.name



class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    apps = models.ForeignKey(App, on_delete = models.CASCADE, related_name='related_items')
    points = models.IntegerField(default = 0)
    screenshot = models.FileField(upload_to = 'media', null = True)
    task_completed = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username

class UserDownloads(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete =models.CASCADE)
    apps = models.ForeignKey(App,on_delete = models.CASCADE)
    visited = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username