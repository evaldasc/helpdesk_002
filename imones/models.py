from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=40)
    isActive = models.BooleanField(True)
    email = models.EmailField(blank=True)
    administrator = models.ForeignKey(User, blank=True)
    # subscribers = models.ManyToManyField(User, blank=True) # TODO
    # contracts # TODO
    def __unicode__(self):
        return u'%s' % (self.name)

class Branch(models.Model):
    company = models.ForeignKey(Company)
    branchName = models.CharField(max_length=50)
    adress = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    # hardware # TODO
    IP = models.IPAddressField(blank=True)
    def __unicode__(self):
        return u'%s @ %s' % (self.branchName, self.company)

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    workplace = models.ForeignKey(Branch)
    position = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobilePhone = models.CharField(max_length=20, blank=True)
    # language # TODO
    def __unicode__(self):
        return u'%s' % (self.user)

