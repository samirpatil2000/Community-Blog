from django.urls import path
from .import views
from django.views.generic import TemplateView
from.views import PostListView,PostDetailView, PostCreateView,PostUpdateView,PostDeleteView,UserPostListView ,PostDetailViewForProfile#,SendFormEmail
urlpatterns=[
    #path('', views.home, name='blog_home'),
    path('about/', views.about, name='about'),
    path('joinus/', views.join_us, name='join_us'),
    path('', PostListView.as_view(), name='latest'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/userprofile/<int:pk>/',PostDetailViewForProfile.as_view(),name='post-userprofile'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<str:username>/', UserPostListView.as_view(), name='user-posts'),

    path('joinemail/',views.join_page,name='joining-page'),
    path('send_email_confirm/',views.send_email,name='send_mail')

   # path('joiningemail/' ,views.SendFormEmail.as_view(), name='conformation-email')
    #path('joiningemail/' ,views.send_email, name='conformation-email')
]