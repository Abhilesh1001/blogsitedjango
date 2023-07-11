from django.shortcuts import render, HttpResponse,redirect
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout


# Create your views here.
# html pages

def home(request):
    return render(request,'home/home.html')
    
def contact(request):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        
        if len(name)<2 or len(email)<3 or len(content)<5 or len(content)<4:
            messages.error(request,'Fill the form correctly')
        else:
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,'Contact Form Submit Successfully')
    return render(request,'home/contact.html')

def about(request):
    return render(request,'home/about.html')

def search(request):
    query =request.GET['query']
    if len(query)>78:
        allPost =Post.objects.none()
    else:
        allPosttitle = Post.objects.filter(title__icontains=query)
        allPostContains = Post.objects.filter(content__icontains=query)
        allPost = allPosttitle.union(allPostContains)
    if allPost.count() ==0:
        messages.error(request,'No search result found please found find the query')
    
    return render(request,'home/search.html',{'allPost':allPost,'query':query}) 

# Auntheticals APIS

def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        password = request.POST['password']
        password2 = request.POST['password2']
        email = request.POST['email']

        print(username,fname,lname,password,password2,email)
        # Checks the inputs fields 
        if len(username)>10:
            return redirect('home')
        
        if password !=password2:
            messages.error(request,'Password didnot Match')
            return redirect('home')
        # Create user
        myuser =User.objects.create_user(username,email,password)
        myuser.first_name = fname
        myuser.last_name =lname
        myuser.save()
        messages.success(request,'Your User icoder has been set')
        return redirect('home')
    else:
        return HttpResponse('Not Allow this form')

def handlelogin(request):
    if request.method == 'POST':
        loginuseername = request.POST['loginusername']
        loginuseerpassword = request.POST['loginpassword']

        user = authenticate(username=loginuseername,password=loginuseerpassword)

        if user is not None:
            login(request,user)
            messages.success(request,'Susscessfully login')
        else:
            messages.error(request,'invalid Quadential Please try again')



    return redirect('home')

def handlelogout(request):
    logout(request)
    messages.success(request,'Susscessfully logout')
    return redirect('home')