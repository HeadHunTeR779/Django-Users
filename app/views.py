from django.shortcuts import render
from app.forms import UserForm, UserProfileInfoForm

#Building up the Login Functionality
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required #This is a decorator DUH! see the import path lol
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, 'app/index.html')


@login_required  #this DECORATOR makes it compulsory for this functionality to be invoked only when the user is already logged in .!.
def user_logout(request): #Can't use the name logout as its something I imported
    logout(request) #Thanks you django
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False  #By default we set it to False, User ain't registered yet

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        user_profile_info_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and user_profile_info_form.is_valid():

            user = user_form.save(commit=False) #save but don't commit in the database
            user.set_password(user.password)
            user.save()

            profile = user_profile_info_form.save(commit=False)
            profile.user = user #remember that OneToOneField Relation that is defined here

            if 'profile_pic' in request.FILES:                #Do this for all non-textual data like .csv files or images or audio
                profile.profile_pic = request.FILES['profile_pic'] #NOTE: we ain't doing this for the portfolio_site

            profile.save()
            registered = True   #Ok so officially registered and all stuff & shit is figured out

        else:
            print(user_form.errors, user_profile_info_form.errors)



    else:   #Means its a GET Request <3
        user_form = UserForm()
        user_profile_info_form = UserProfileInfoForm()

    context_dict = {'registered':registered, 'user_form':user_form, 'user_profile_info_form':user_profile_info_form }

    return render(request, 'app/registration.html', context = context_dict)


def user_login(request):     #Note that login is something I imported so can't use it as name <3

    if request.method == "POST":
        username = request.POST.get("usern")  #Look the name in <input> in login.html
        password = request.POST.get("pass")     #Look the name in <input> in login.html

        user = authenticate(username=username, password=password)  #Thanks you django <3

        if user: #If user was authenticated!
            if user.is_active:
                login(request,user) #Thanks you django again!
                return HttpResponseRedirect(reverse('index'))
                #Ok so render is like render(request, 'path/to/page.html',context) here HttpResponseRedirect Redirects the user to the
                #HARD-CODED URL given to it as ARGUMENT but hey! remember we don;t hard code URL instead we use dynamic URL TEMPLATE
                #TAGS which map the URL for us and the pay-off is huge if we ever need to change the url we just need to change it
                # in one place i.e. the the urlpatterns!   so I wanna use that same stuff here but here CANNOT use {% url 'index' %}
                # as I want to redirect it at my own index.html so what to do USE reverse() it taken the stuff after url with ''


            else:
                return HttpResponse("INACTIVE USER ACCOUNT!")

        else:
            print("Unauthenticated user")
            print("Username: {} Password: {}".format(username,password))
            return HttpResponse("Invalid Login Details Supplied .!.")


    else: #method wasn't post
        return render(request, "app/login.html")
