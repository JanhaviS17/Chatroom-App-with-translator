from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name="Home"),
    path("CreateRoom.html",views.create_room_page,name="create_room_page"),
    path("JoinRoom.html",views.join_room_page,name="join_room_page"),
    path("create_room",views.create_room,name="Creating"),
    path("room_name_validation",views.room_name_validation,name="RoomValidation"),
    path("password_validation",views.password_validation,name="PassValidation"),
    path("join_chat_room",views.join_room,name="Joining"),
    path("chatpage/<str:room_name>/",views.chat_page,name="ChatPage"),
    path("chatpage/<str:room_name>/insert_message",views.insert_message,name="MessageInsertion"),
    path("getMessages",views.getmessages,name="GetMessages"),
]