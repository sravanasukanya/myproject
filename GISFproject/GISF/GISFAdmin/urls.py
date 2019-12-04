from django.urls import path

from .views import NewUserCreate, homepage, about, loginView, logout_view, register, mainmenu

app_name = 'MyAdmin'

urlpatterns = [
    path('registration/', NewUserCreate, name="NewUserCreate"),
    path('', homepage, name='homepage'),
    path('About/', about, name='About'),
    path('clogin/', loginView, name='clogin'),
    path('log-out/', logout_view, name='logout'),
    path("Newregister/", register, name="register"),
    path('mainmenu/', mainmenu, name='mainmenu'),
     ]