from django.shortcuts import render_to_response
from imones import models
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

@login_required
def users(request):
#    company = models.Company.objects.get(pk="1")
#    return render_to_response('basic.html', {'company': company})
    return render_to_response('portal/index.html')
    
@login_required
def imones(request):
#    company = models.Company.objects.get(pk="1")
#    return render_to_response('basic.html', {'company': company})
    return render_to_response('portal/index.html')
