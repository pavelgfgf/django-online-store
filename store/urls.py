"""
URL configuration for store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from authorization.views import RegisterView, TokenView
from categories.views import CategoriesView
from listproducts.views import ListProductDetails
from products.views import ProductDetails
from buyproduct.views import BuyProductList
from ads.views import AdList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/registration', RegisterView.as_view()),
    path('api/auth', TokenView.as_view()),
    path('api/categories', CategoriesView.as_view()),
    path('api/categories/<int:pk>/products', ListProductDetails.as_view()),
    path('api/products/<int:pk>', ProductDetails.as_view()),
    path('api/products/<int:pk>/buy', BuyProductList.as_view()),
    path('api/ads', AdList.as_view()),
]
