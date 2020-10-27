from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from .forms import NewUserForm
import operator

# Create your views here.
def logout_request(request):
    #logout(request)
    #messages.info(request, "Logged out successfully!")
    #return redirect("home1.html")
    return render(request,'home1.html')
def login_request(request):
    return render(request,'login.html')
    #form=AuthenticationForm()

      # return render(request=request,template_name="login.html",context={"form":form})

    #if request.method == 'POST':
    #form=AuthenticationForm(request=request,data=request.POST)
    #if form.is_valid():
    #    username=form.cleaned_data.get('username')
    #    password=form.cleaned_data.get('password')
    #    user=authenticate(username=username,password=password)
    #    if user is not None:
    #        login(request,user)
    #        messages.info(request,f"You are logged in as {username}")
    #        return redirect('/')
    #    else:
    #        messages.error(request,"Invalid username or password.")
  # else:
    #   messages.error(request,"Invalid username or password.")

    #def logout_request(request):
        #logout(request)
        #messages.info(request,"Logged out succesfully!")\
        #return render(request,'home1.html')
        #return redirect("main:home")

def register(request):
    return render(request,'register.html')

def about(request):
    return render(request,'about.html',{'s':'Successfull Website '})

def home(request):
    return render(request,'home1.html',{'hithere':'Put your words'})

def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word]+=1
        else:
            #add
            worddictionary[word]=1
            sortedwords=sorted(worddictionary.items(),key=operator.itemgetter(1),reverse=True)

  #sortedwords=sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})


#def home(request):
    #return HttpResponse('Congrates!')
#def Egg(request):
    #return HttpResponse('<h1><font color="red">Hello! you are succeded in your work!</font></h1>')
#from django.http import HttpResponse
#from django.shortcuts import render
#def home(request):
    #return render(request,'home1.html')




#form.py
#from django import forms
#from django.contrib.auth.forms import UserCreationForm
#from django.contrib.auth.models import User
#class NewUserForm(UserCreationForm):
#    email=forms.EmailField(required=True)

#    class Meta:
#        model = User
#        fields = ('username','email','password','password2')
#        def save(self,commit=True):
#            user=super(NewUserForm,self).save(commit=False)
#            user.email=self.cleande_data["email"]
#            if commit:
#                user.save()
#                return user
