from django.shortcuts import render_to_response
from imones.models import Company, Branch
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def get_user_info(user):
    """Return nice representation of user nd a company it works in
    """
    userinfo = [user.username, " (", user.get_full_name(), ", ", 
                                user.get_profile().workplace.company.name, ")"]
    userinfo = ''.join(userinfo)
    return userinfo

@login_required
def meniu(request):
    context = {}
    context["user"] = get_user_info(request.user)
#   company = Company.objects.get(pk="1")
#   return render_to_response('basic.html', {'company': company})
    return render_to_response('portal/index.html', context)

@login_required
def users(request):
    context = {}
    context["user"] = get_user_info(request.user)
#    company = Company.objects.get(pk="1")
#    return render_to_response('basic.html', {'company': company})  
    return render_to_response('portal/index.html', context)
    
@login_required
def companies(request):
    context = {}
    context["user"] = get_user_info(request.user)
    context["companies"] = Company.objects.all()
    return render_to_response('portal/companies.html', context)
    
@login_required
def company_detail(request, id):
    context = {}
    context["user"] = get_user_info(request.user)
    context["company"] = Company.objects.get(pk=id)
    context["branches"] = Branch.objects.filter(company=id)
    return render_to_response('portal/company_details.html', context)
