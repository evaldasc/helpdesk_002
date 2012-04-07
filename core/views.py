from django.shortcuts import render_to_response
from core.models import Branch, BranchForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
debug = 0

def get_user_info(user):
    """Return nice representation of user and a company it works in
    """
    userinfo = [user.username, " (", user.get_full_name()]
    
    try:
        userinfo.extend([", ", user.get_profile().workplace.name, ")"])
    except:
        userinfo.extend([", ", "no company", ")"])
    
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
    context["companies"] = Branch.objects.filter(super_branch__isnull=True)
    return render_to_response('portal/companies.html', context)
    
@login_required
def company_detail(request, id):
    if debug: print "ID = " + str(id)  # FOR DEBUGING PURPOSES ONLY
    context = {}
    branch = Branch.objects.get(pk=id)
    context["user"] = get_user_info(request.user)
    context["branch"] = branch
    context["subbranches"] = Branch.objects.filter(super_branch=id)
    #--
    form = BranchForm(request.POST or None, instance=id and branch)
    
    if request.method == 'POST' and form.is_valid():
        form.save()      

    context["form"] = form
    #--
    return render_to_response('portal/company_details.html', context)
