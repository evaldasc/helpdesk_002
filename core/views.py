from django.shortcuts import render_to_response
from django.shortcuts import render
from core.models import Branch, BranchForm, UserProfile
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import logging
from django.core.context_processors import csrf

logger = logging.getLogger(__name__)

def get_user_info(user):
    """Return nice representation of active user and a company it works in
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
    context["active_user"] = get_user_info(request.user)
    return render(request, 'portal/index.html', context)
   
@login_required
def companies(request):
    context = {}
    context["active_user"] = get_user_info(request.user)
    context["companies"] = Branch.objects.filter(super_branch__isnull=True)
    return render(request, 'portal/companies.html', context)
    
@login_required
def company_detail(request, id):
    logger.debug("Company ID = " + str(id)) # DEBUG
    context = {}
    branch = Branch.objects.get(pk=id)
    context["active_user"] = get_user_info(request.user)
    context["branch"] = branch
    context["subbranches"] = Branch.objects.filter(super_branch=id)
    #--
    form = BranchForm(request.POST or None, instance=id and branch)
    
    if request.method == 'POST' and form.is_valid():
        form.save()      

    context["form"] = form
    #--
    return render(request, 'portal/company_details.html', context)
    
@login_required
def company_users(request, id):
    logger.debug("Company ID = " + str(id)) # DEBUG
    context = {}
    context["active_user"] = get_user_info(request.user)
    context["user_list"] = UserProfile.objects.filter(workplace=id)
    try:
        context["branch"] = Branch.objects.get(pk=id)
    except:
        logger.info("No such company by ID = " + str(id))  # DEBUG
        context["branch"] = "<?>"  
    if not context["user_list"]:                            # DEBUG
        logger.info("No users in company ID = " + str(id))  # DEBUG
        
    return render(request, 'portal/users.html', context)
    
@login_required
def user_detail(request, id):
    context = {}
    context["user"] = get_user_info(request.user)

    return render(request, 'portal/index.html', context)
