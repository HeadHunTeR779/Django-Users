from django.shortcuts import render
from app.forms import UserForm, UserProfileInfoForm

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

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
