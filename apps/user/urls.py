from django.urls import path
from apps.user import views


urlpatterns = [
    # Pages
    path('', views.index, name="index"),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('about-us/', views.about_us, name='about-us'),
    path('product/', views.author, name='product'),
    path('registers/', views.registration, name='registers'),
    path('logins/', views.handleLogin, name='logins'),
    path('logouts/', views.LogOut, name='logouts'),
    path('profile/', views.profile, name='profile'),
    path('profiles/', views.profiles, name='profiles'),
    path('wobook/<int:pk>/',views.woodybook,name="wobook"),
    path('delor/<int:pk>/',views.delorder,name="delor"),
    path('radd/<int:pk>/',views.orreturn,name="radd"),
    path('feedback/', views.feedbackk, name='feedback'),
]
