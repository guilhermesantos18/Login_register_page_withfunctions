from django.urls import path, include
from django.contrib.auth import views
                
urlpatterns = [
    path('acconts/', include('django.contrib.auth.urls')),
    path('acconts/login/', views.LoginView.as_view(template_name='base/login.html')),
]
