from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('bootcamp/<int:_id>', views.bootcamp),
    path('reg_log',views.reg_log),
    path('registration',views.registration),
    path('login',views.login),
    path('logout',views.logout), 
    path('profile', views.profile),
    path('home_student',views.home_student),
    path('info_bootcamp/<int:_id>',views.info_bootcamp),
    path('go_add_project',views.go_add_project),
    path('new_project',views.new_project),
    path('remove_project/<int:_id>',views.remove_project),
    path('go_edit_project/<int:_id>',views.go_edit_project),
    path('edit_project/<int:_id>',views.edit_project),
    path('go_edit_profile',views.go_edit_profile),
    path('edit_profile/<int:_id>',views.edit_profile),
    path('go_profile/<int:_id>',views.go_profile),
    path('add_comment/<int:_id>',views.add_comment)
]

