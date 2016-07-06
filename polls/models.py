from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    age=models.IntegerField(default=1)

    def __unicode__(self):
        return self.name

class Audio_Video_models(models.Model):
    audio=models.FileField(max_length=200)
    video=models.FileField(max_length=300)


    def __unicode__(self):
        return '%s,%s' %(self.audio,self.video)

class Address(models.Model):
    address=models.ForeignKey(Contact)
    place=models.CharField(max_length=100)

    def __unicode__(self):
        return self.place

class Login(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Entry(models.Model):
    name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    age=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone_number=models.CharField(max_length=100)



    def __unicode__(self):
        return '%s, %s' %(self.name,self.password)

        
class Bhavcopy(models.Model):
    bhav_date = models.DateField()
    sc_code = models.IntegerField()
    sc_name = models.CharField(max_length=200)
    sc_group = models.CharField(max_length=10)
    sc_type = models.CharField(max_length=10)
    open = models.FloatField(max_length=20)
    high = models.FloatField(max_length=200)
    low = models.FloatField(max_length=200)
    close = models.FloatField(max_length=200)
    last = models.FloatField(max_length=200)
    prevclose = models.FloatField(max_length=200)
    no_trades = models.IntegerField()
    no_of_shrs = models.IntegerField()
    net_turnov = models.FloatField(max_length=200)
    tdcloindi = models.CharField(max_length=200)




class Files_Upload_Model(models.Model):
    files=models.FileField(upload_to='documents/%Y/%m/%d')


    def __unicode__(self):
        return unicode(self.files) or u''







