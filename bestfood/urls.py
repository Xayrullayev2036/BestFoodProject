"""
URL configuration for bestfood project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from category import views

urlpatterns = [
                  path("", views.HomePanel.as_view(), name="home-panel"),
                  path('', include("category.urls")),
                  path('', include("orderfood.urls")),
                  path('', include("post.urls")),
                  path('', include("users.urls")),
                  path("home/", views.Home.as_view(), name="home"),
                  path("products/", views.MenuPanel.as_view(), name="product-panel"),
                  path("about/", views.AboutPanel.as_view(), name="about-panel"),
                  path('adminpanel/', views.AdminPanel.as_view(), name='admin-panel'),
                  path('admin/', admin.site.urls),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
