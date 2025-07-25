from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse
from accounts.models import ProfileModel 
from affairs import views
from django.conf import settings
from django.contrib.auth.models import User
from accounts.forms import ProfileRegisterForm,ProfileEditForm,UserEditForm
from django.contrib.auth.forms import PasswordChangeForm
import accounts

# Create your views here.

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            return redirect(settings.LOGIN_REDIRECT_URL)
        else:
            context = {
                "username": username,
                "errorMessage": "User does not exist or password is incorrect."
            }
            return render(request, "accounts/login.html", context)
    else:
        return render(request, 'accounts/login.html')


@login_required
def logoutView(request):
  logout(request)
  return HttpResponseRedirect(reverse(views.MainPageView))

from django.core.exceptions import ObjectDoesNotExist

@login_required
def profileView(request):
    profile, created = ProfileModel.objects.get_or_create(
        user=request.user,
        defaults={
            'Gender': ProfileModel.Man,
            'Credit': 0,
            'ProfileImage': 'ProfileImages/default.jpg',
        }
    )

    context = {
        "profile": profile
    }
    return render(request, "accounts/profile.html", context)




@login_required
def ProfileEditView(request):
    try:
        profile = request.user.profile
    except ProfileModel.DoesNotExist:
        messages.error(request, "No profile found.")
        return redirect("profile")  # or a safer fallback

    if request.method == "POST":
        profileEditForm = ProfileEditForm(request.POST, request.FILES, instance=profile)
        userEditForm = UserEditForm(request.POST, instance=request.user)

        if profileEditForm.is_valid() and userEditForm.is_valid():
            profileEditForm.save()
            userEditForm.save()
            return redirect("profile")
    else:
        profileEditForm = ProfileEditForm(instance=profile)
        userEditForm = UserEditForm(instance=request.user)

    context = {
        "profileEditForm": profileEditForm,
        "userEditForm": userEditForm,
        "ProfileImage": profile.ProfileImage
    }

    return render(request, "accounts/profileEdit.html", context)


@login_required
def changePasswordView(request):
    
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/changepassword.html', {'form': form})

def profileRegisterView(request):
    if request.method == "POST":
        profileRegisterForm = ProfileRegisterForm(request.POST, request.FILES)
        if profileRegisterForm.is_valid():
            # Create user
            user = User.objects.create_user(
                username=profileRegisterForm.cleaned_data["username"],
                email=profileRegisterForm.cleaned_data["email"],
                password=profileRegisterForm.cleaned_data["password"],
                first_name=profileRegisterForm.cleaned_data["first_name"],
                last_name=profileRegisterForm.cleaned_data["last_name"]
            )

            # Handle profile image (optional)
            image = profileRegisterForm.cleaned_data.get('ProfileImage')
            gender = profileRegisterForm.cleaned_data.get('Gender')
            credit = profileRegisterForm.cleaned_data.get('Credit')

            profileModel = ProfileModel(
                user=user,
                ProfileImage=image if image else 'ProfileImages/default.jpg',
                Gender=gender if gender is not None else ProfileModel.Man,
                Credit=credit if credit is not None else 0
            )

            profileModel.save()
            return HttpResponseRedirect(reverse(views.MainPageView))
    else:
        profileRegisterForm = ProfileRegisterForm()

    context = {
        "formsData": profileRegisterForm
    }
    return render(request, "accounts/profileRegister.html", context)
