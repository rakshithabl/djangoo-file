from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
      
    def save(self,*args,**kwargs):
        if not self.email:
            self.email=f"{self.name.lower().replace('','.')}@example.com"
        super(Student,self).save(*args,**kwargs)

def __str__(self):
    return self.name
      