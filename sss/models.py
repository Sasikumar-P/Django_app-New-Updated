from django.db import models
from django.contrib.auth.models import User
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank=True)
    phonenumber = models.IntegerField(default=0)
    address = models.CharField(max_length=50, default=0)
    state = models.CharField(max_length=30, default=0)
    city = models.CharField(max_length=60, default=0)    
    country = models.CharField(max_length=50, default=0)
   
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __unicode__(self):
        return self.name
class Family(models.Model):
    fathername = models.CharField(max_length=30)
    mothername = models.CharField(max_length=30)
    brothername = models.CharField(max_length=30)
    sistername = models.CharField(max_length=30)
    grandfathername = models.CharField(max_length=30)
    grandmothername = models.CharField(max_length=30)
    annualincome = models.IntegerField()    
    def __unicode__(self):
        return self.fathername


class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.title









class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
