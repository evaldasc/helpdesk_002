from django.db import models
from django.contrib.auth.models import User

##class Company(models.Model):
##    name = models.CharField(max_length=40) #
#    isActive = models.BooleanField(True) #
#    email = models.EmailField(blank=True)
#    administrator = models.ForeignKey(User, blank=True) # ? 
#    # wiki TODO
#    # subscribers = models.ManyToManyField(User, blank=True) # TODO ?
#    # contracts # TODO
#    def __unicode__(self):
#        return u'%s' % (self.name)

class Branch(models.Model):
    """Part of the company refering to other (super)branches. If there is 
    none - it means it is the main branch therefore the company itself    
    """
    # - company = models.ForeignKey(Company)
    super_branch = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=40) 
    is_active = models.BooleanField(default=True)
    # - branchName = models.CharField(max_length=50, default=company.name)
    adress = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    # hardware # TODO ext
    # wiki TODO ext
    external_IP = models.IPAddressField(blank=True)
    def __unicode__(self):
        return u'%s' % (self.name)
        #return u'%s @ %s' % (self.name, self.company)

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    workplace = models.ForeignKey(Branch)
    position = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    # language # TODO
    # permissions / Admins may change permissions of other users
    #                                                   to lover level ones
    def __unicode__(self):
        return u'%s' % (self.user)

