"""
URL configuration for CRUD project.

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
from django.urls import path,include
from App import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    #Home
    path('', views.home, name='home'),
    #Add
    path('add_product', views.add_product, name='add_product'),
    #View
    path('product/<str:product_id>', views.product, name='product'),
    #Edit
    path('edit_product/<str:product_id>', views.edit_product, name='edit_product'),
    #Delete
    path('delete_product/<str:product_id>', views.delete_product, name='delete_product'),
    #Filter
    path('filter_product', views.filter_product, name="filter_product"),
    path('read_pdf', views.read_pdf, name="read_pdf"),
    path('go_filter', views.go_filter, name="go_filter"),
    path('pdf/week.pdf', views.serve_pdf, name='pdf'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
