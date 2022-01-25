from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm # commenting this because we are no longer using this UserCreationForm instead we are using the custom UserRegisterForm that we created in forms.py file
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) # if the method is post the form will still have the entered data
        if form.is_valid():
            form.save() # to save the user
            username=form.cleaned_data.get('username') # if the form is valid get the username
            messages.success(request, f'your account now has been created ! You now be will able to login')
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'your account now has been updated')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)
