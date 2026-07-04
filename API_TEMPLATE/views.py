from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.template import loader
from .models import User



# Create your views here.
def login(request):
    return render(request, 'login.html')    

class CreateUserView(View):
    def get(self, request):
        return render(request, 'create_user.html')
    
def details(request, user_id):
    return HttpResponse("User details for user with ID %d" % user_id)

def nombre(request, user_name):
    return HttpResponse("User details for user with name %s" % user_name)

def index(request):
    lastest_user_list = User.objects.order_by('-created_at')[:5]
    template = loader.get_template('index.html')
    context = {"lastest_user_list": lastest_user_list}
    return HttpResponse(template.render(context, request))

#OTHER WAYS TO RENDER A TEMPLATE
#def index(request):
#    lastest_user_list = User.objects.order_by('-created_at')[:5]
#    context = {"lastest_user_list": lastest_user_list}
#    return render(request,"index.html, context)

def role(request):
    return HttpResponse("Role details for role with ID %d" % role_id)   