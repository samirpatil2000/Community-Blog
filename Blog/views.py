from django.conf import settings
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from django.views.generic import View
from .models import Post ,ForFun
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin  # this is for you canot add post without logged in
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.core.mail import EmailMessage

from django.contrib import messages
from django.core.mail import send_mail, send_mass_mail



# from .forms import PostUpdateForm



# Create your views here.


def home(request):

    return render(request,'Blog/home.html')
def about(request):
    return render(request,'Blog/about.html')

def join_us(request):
    # email = EmailMessage('Subject', 'Body', to=['samirspatil2000@gmail.com'])
    # email.send()
    return render(request,'Blog/join_us.html')
def latest(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request,'Blog/latest.html',context)

def join_page(request):
    return render(request,'Blog/joining_email.html')



def send_email(request):
    if request.method =="GET":
         # name = request.GET.get('name', None)
        #  email = request.GET.get('email', None)
        #  message = request.GET.get('message', None)
        # # send_mail(subject,message,from_email,to_list,fail_silently=True)
        #  subject="Joining request"
        #  #message="welcome"
        #  from_email=settings.EMAIL_HOST_USER
        #  to_list=[email,settings.EMAIL_HOST_USER]
        #  send_mail(subject,message,from_email,to_list,fail_silently=True)

         return redirect(request,'Blog/joining_email.html')


    return render(request,'Blog/joining_email.html')

#
# class SendFormEmail(View):
#
#     def get(self, request):
#         # Get the form data
#         name = request.GET.get('name', None)
#         email = request.GET.get('email', None)
#         message = request.GET.get('message', None)
#
#         # Send Email
#         #
#         # send_mail(
#         #     'subject',
#         #     'body of the message',
#         #     'sender@example.com',
#         #     [
#         #         'receiver1@example.com',
#         #         'receiver2@example.com'
#         #     ]
#         # )
#         #
#         # send_mail(
#         #     'subject',
#         #     'body of the message',
#         #     'samirspatil742099@gmil.com',
#         #     [
#         #         'bluekoko53@gmail.com'
#         #     ]
#         # )
#
#         send_mail(
#             'Subject - Django Email Testing',   # This is subject
#             'Hello ' + str(name) + ',\n' + str(message),    # This is Body meance actual message that you wanted to sent
#             'samirspatil742099@gmail.com',   # Admin
#             [ 'bluekoko53@gmail.com' ] # This is email from html template
#         )
#
#         # Redirect to same page after form submit
#         messages.success(request, ('Email sent successfully.'))
#         return redirect('conformation-email')
# #
# #
#



class PostListView(ListView):
    model = Post
    template_name = 'Blog/latest.html'
                                           #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'Blog/user_post.html'
                                           #<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
   # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user= get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')






class PostDetailView(DetailView):
    model = Post

#This is for profile Pic in UserPostListView
class PostDetailViewForProfile(DetailView):
    model=Post
    template_name = 'Blog/user_public_profile.html'




class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','sub_title','attractiv_lines','content','blog_image_1','content_2']

    title=Post._meta.get_field('title')
    author=Post.author


    #title = Post.cleaned_data.get('title')
    #email = Post._meta.get_field('email')
    # email='bluekoko53@gmail.com'
    # subject = title,author
    # message = "New Post Is Created "
    # from_email = settings.EMAIL_HOST_USER
    # to_list = [email, settings.EMAIL_HOST_USER]
    # send_mail(subject, message, from_email, to_list, fail_silently=True)


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','sub_title','attractiv_lines','content','blog_image_1','content_2']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post= self.get_object()
        if self.request.user== post.author:
            return True
        return False



class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post= self.get_object()
        if self.request.user== post.author:
            return True
        return False

#class PostProfile




## Now create the detail viwes for the user profile pictures and all
#class ProfilePostDeatils


# TJIS IS FOR CLASS

# def imageupdate(request):
#     image_form=PostUpdateForm()
#     context={
#         'image_form':image_form,
#     }
#     return render(request,'Blog/post_form.html',context)

