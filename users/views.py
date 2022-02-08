from django.shortcuts import render, redirect
from django.contrib import messages #to display flash messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) # an instance of the class 
        if form.is_valid():
            form.save() #creating a new user
            username = form.cleaned_data.get('username')
            # messages are put in base-template {% for message in messages %}
            messages.success(request, f'Your account has been created! You can now log in!') #one-time alert 
            return redirect('login') 
    else:
        form = UserRegisterForm() # a blank form 
    return render(request,'users/register.html',{'form':form}) # 'form' is the 'context'

@login_required 
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                    request.FILES, 
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') 
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request,'users/profile.html', context)