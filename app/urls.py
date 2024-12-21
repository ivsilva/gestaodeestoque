from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('', views.home, name='home'),

    path('api/v1/', include('authentication.urls')),
    path('',include('brands.urls')),
    path('',include('categories.urls')),
    path('',include('suppliers.urls')),
    path('',include('inflows.urls')),
    path('',include('outflows.urls')),
    path('',include('products.urls')),

]
