from django.contrib import admin
from django.urls import path
from adminSystem import settings
from django.conf.urls.static import static
from base import views, AdminViews

urlpatterns = [   
    path('admin/', admin.site.urls),
    path('',views.ShowLoginPage,name="show_login"),
    path('doLogin',views.doLogin,name="do_login"),
    path('logout_user', views.logout_user,name="logout"),
    path('admin_home',AdminViews.admin_home,name="admin_home"),
    path('edit_user/<str:user_id>', AdminViews.edit_user,name="edit_user"),
    path('delete_user/<str:user_id>', AdminViews.delete_user,name="delete_user"),
    path('edit_user_save', AdminViews.edit_user_save,name="edit_user_save"),
    path('add_user', AdminViews.add_user,name="add_user"),
    path('add_user_save', AdminViews.add_user_save,name="add_user_save"),
]
