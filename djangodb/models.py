from django.db import models

# Create your models here.


class Home(models.Model):
	f_name = models.CharField(max_length = 80,blank=False)
	l_name = models.CharField(max_length= 50,blank=False)
	email = models.CharField(max_length=30,blank=False)
	age = models.IntegerField(blank=False)
	passwd = models.CharField(max_length=50,blank=False)
	
def __str__(self):
	return self.f_name
		
		