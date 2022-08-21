from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    ism = models.CharField(max_length=50)
    email = models.EmailField()
    jins = models.CharField(max_length=6, choices=[("Erkak", "Erkak"), ("Ayol", "Ayol")])
    shahar = models.CharField(max_length=30)
    mamlakat = models.CharField(max_length=30)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.ism


class Video(models.Model):
    nom = models.CharField(max_length=30)
    preview = models.FileField()
    sana = models.DateTimeField(auto_now_add=True)
    matni = models.CharField(max_length=200)
    korishlar_s = models.PositiveSmallIntegerField()
    url = models.URLField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom


class Playlist(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)



class Comment(models.Model):
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    izoh = models.CharField(max_length=200)
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.izoh


class Kanal(models.Model):
    nom = models.CharField(max_length=12)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    obunachilar = models.IntegerField()
    malumot = models.CharField(max_length=500)

    def __str__(self):
        return self.nom


class History(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.video


