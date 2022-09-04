"""ViCalc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import home_v, logout_v, register_v, login_v, covid_info_v, covid_quiz_v, map_v, info_v
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_v, name="home"),
    path('logout/', logout_v, name='logout'),
    path('register/', register_v, name="register"),
    path('login/', login_v, name="login"),
    path('covid_info/', covid_info_v, name="covid_info"),
    # path('covid_checker/', symptom_checker_v, name="symptom_checker"),
    path('covid_quiz/', covid_quiz_v, name="covid_quiz"),
    path('map/', map_v, name="map"),
    path('covid_info/<str:name>', info_v, name="info")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
