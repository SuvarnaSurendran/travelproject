from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField(blank=True)

    def __str__(self):
        return self.name

class Team(models.Model):
    Name = models.CharField(max_length=250)
    Img = models.ImageField(upload_to='pics')
    Desc = models.TextField()

    def __str__(self):
        return self.Name