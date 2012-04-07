from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

class Branch(models.Model):
    """Part of the company refering to other (super)branches. If there is 
    none - it means it is the main branch therefore the company itself    
    """
    super_branch = models.ForeignKey('self', blank=True, null=True)
    name = models.CharField(max_length=40) 
    is_active = models.BooleanField(default=True)
    adress = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    # hardware # TODO ext
    # wiki TODO ext
    external_IP = models.IPAddressField(blank=True)
    def __unicode__(self):
        return u'%s' % (self.name)
        #return u'%s @ %s' % (self.name, self.company)
    def get_fields(self):
	    """make a list of field/values."""
	    full_list = [(field.verbose_name, field.value_to_string(self)) for field\
                                                        in self._meta.fields]
	    return full_list
	    
class BranchForm(ModelForm):
    class Meta:
        model = Branch

class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    workplace = models.ForeignKey(Branch)
    position = models.CharField(max_length=20, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    # language # TODO
    # permissions / Admins may change permissions of other users
    #                                                   to lower level ones
    def __unicode__(self):
        return u'%s' % (self.user)

