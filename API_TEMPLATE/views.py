from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.template import loader
from .models import User
from .models import Product



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

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'product.html', {'product': product})

def user_view(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'user.html', {'user': user})