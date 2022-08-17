from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pic')
    des=models.TextField()

    def __str__(self):
        return self.name
class team(models.Model):
    names=models.CharField(max_length=250)
    imges=models.ImageField(upload_to='pic')
    des1=models.TextField()

    def __str__(self):
        return self.names
