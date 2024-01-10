from django.urls import path, include
from . import views
from django_email_verification import urls as email_urls

urlpatterns = [
    path('', views.create, name='register'),
    path('users/', views.users_home, name='users_catalog'),
    path('signup/', views.registration, name='logIN'),
    path('email/', include(email_urls)),
    path('land/', views.landing_page, name='landing_page'),
    path('login/', views.log_in, name='login_page'),
    # path('about', views.about, name='about'),
    # path('contacts', views.contacts, name='contacts'),
]
