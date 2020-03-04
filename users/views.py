from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from .forms import UserRegisterForm,UserUpadeteForm,ProfileUpdateForm


# Create your views here.
def register_user(request):
    if request.method =='POST':

        form =UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            email=form.cleaned_data.get('email')
            messages.success(request,f' Your Account Has Been Created for {username} !')
            # send the joining mail
            # send_mail(subject,message,from_email,to_list,fail_silently=True)
            subject = " Hello " + username
            message="welcome"
            from_email = settings.EMAIL_HOST_USER
            to_list = [email,settings.EMAIL_HOST_USER]
            send_mail(subject, message, from_email, to_list, fail_silently=True)


            # This mail for the the Admin

            subject_me=username+ "is just regiter to our site "
            message_me="you know"
            to_me=[settings.EMAIL_HOST_USER]
            send_mail(subject_me, message_me,from_email, to_me, fail_silently=True)

            return redirect('login')  # name that you give to that url
    else:
        form=UserRegisterForm()

    return render(request,'users/register.html',{'form':form})


@login_required()  # this is for profile page if logout the it will give page 404 error
def profile(request):
    if request.method == 'POST':

        u_form=UserUpadeteForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            p_form.save()
            messages.success(request, f' Your Account Has Been Updated !')
            return redirect('profile')
    else:
        u_form = UserUpadeteForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form':u_form ,
        'p_form':p_form
    }
    return render(request,'users/Profile_Edit.html',context)



