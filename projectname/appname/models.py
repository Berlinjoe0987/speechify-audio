from django.db import models

# Create your models here.
class data(models.Model):
    word1=models.CharField(max_length=100)
    word2=models.CharField(max_length=100)



class Word(models.Model):
    word = models.CharField(max_length=100)

    def __str__(self):
        return self.word