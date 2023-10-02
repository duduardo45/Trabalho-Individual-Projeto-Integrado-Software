"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from appBTD6introduction import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),

    path('password_reset/', views.PasswordReset.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDone.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetComplete.as_view(), name='password_reset_complete'),

  
    path('users/registrar/',views.create_user,name='cadastrar'),
    path('users/editar/<id>',views.formUserEdit,name='update_user'),
    path('',views.home,name='home'),
    path('alterar/',views.alteracoes),
    path('alterar/formGenero/',views.formGenero),
    path('alterar/formGenero/add/',views.formGeneroAdd),
    path('alterar/formGenero/edit/<id>',views.formGeneroEdit),
    path('alterar/formGenero/remove/<id>',views.formGeneroRemove),
    path('alterar/formHistoria/',views.formHistoria),
    path('alterar/formHistoria/add/',views.formHistoriaAdd),
    path('alterar/formHistoria/edit/<id>',views.formHistoriaEdit),
    path('alterar/formHistoria/remove/<id>',views.formHistoriaRemove),
    path('admin/', admin.site.urls),
]
