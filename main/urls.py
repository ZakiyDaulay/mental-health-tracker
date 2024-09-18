from django.urls import path
from main.views import show_main,create_mood_entry,show_xml,show_xml_by_id,register,login_user,logout_user


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('logout/', logout_user, name='logout'),
    path('create-mood-entry',create_mood_entry,name='create_mood_entry'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register')
]