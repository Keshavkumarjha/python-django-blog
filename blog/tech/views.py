from tech.models import Contact,Post
from django.shortcuts import render,redirect
from .models import Contact
from django.contrib.auth.models import User, Group,auth
from django.contrib.auth import authenticate, login
# Create your views here.
def index(request):
    data=Post.objects.all()
    return render(request,'index.html',{'data':data})
def user_post(request,pk):
    post=Post.objects.get(pk=pk)
        
    return render(request, 'post.html',{'post':post})
    
    
        

    
      
    


def user_about(request):
    return render(request,'about.html')



def user_login(request):

    if request.method=='POST':
        username=request.POST['username']
        password1=request.POST['password1']
        user = auth.authenticate(username=username ,password=password1)

        if user is not None:
            auth.login(request,user)
            return redirect("/admin/")
        else:
            # messages.info(request,'Username and Password not Match')
            return render(request, 'core/login.html')
    else:

        return render(request, 'login.html')
   
    

        
 
    


def user_contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']
        data = Contact(name=name,email=email,phone=phone,message=message)
        data.save()
        # print("save data........................")
    return render(request,'contact.html')
