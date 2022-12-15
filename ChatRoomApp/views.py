from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import Room_Details,Message_Details
from django.contrib import messages
from googletrans import Translator


# Create your views here.
def home(request):
    return render(request,'index.html')

def create_room_page(request):
    return render(request, 'CreateRoom.html')
def join_room_page(request):
    return render(request, 'JoinRoom.html')

def create_room(request):

    room_name=request.POST["room_name"]
    password = request.POST["pass"]
    username = request.POST["username"]
    lang = request.POST["lang"]
    if Room_Details.objects.filter(Room_Name=room_name).exists():
        #messages.info(request,"Room name already exists. Please create a new or join the existing one")
        return redirect (home)
    else:
        new_room=Room_Details.objects.create(Room_Name=room_name,Password=password,Created_By=username)
        new_room.save()
        #return redirect(chat_page,room_name,username,lang)
        return redirect("chatpage/"+room_name+"/?username="+username+"&lang="+lang)

def join_room(request):
    room_name = request.POST["room_name"]
    username = request.POST["username"]
    lang = request.POST["lang"]
    return redirect("chatpage/" + room_name + "/?username=" + username + "&lang=" + lang)

# def chat_page (request,room_name,username,lang):
#     return HttpResponse("Working")
def room_name_validation (request):
    room_name=request.GET["room_name"]
    if Room_Details.objects.filter(Room_Name=room_name).exists():
        return HttpResponse("Room Name already exists")


def password_validation (request):
    room_name=request.GET["room_name"]
    password = request.GET["password"]
    print(room_name,password)

    if not Room_Details.objects.filter(Room_Name=room_name, Password=password).exists():
        return HttpResponse("Username and Password is incorrect")


def chat_page (request,room_name):
    username=request.GET["username"]
    lang = request.GET.get("lang")
    room_details = Room_Details.objects.get(Room_Name=room_name)
    return render(request,'ChatPage.html',
                  {
                   'username':username,
                    'lang':lang,
                    'room_name':room_name,
                  })

def insert_message(request,room_name):
    username=request.GET["username"]
    lang = request.GET["lang"]
    print(username,lang)
    message = request.GET["message"]
    new_message=Message_Details.objects.create(Message=message,User=username,room_name=room_name)
    new_message.save()
    return HttpResponse("Gaya message DB mein")

def getmessages(request):
    lang=request.GET["lang"]
    room_name=request.GET["room_name"]
    username = request.GET["username"]
    print(lang)
    if Message_Details.objects.filter(room_name=room_name).exists():
        messages = Message_Details.objects.filter(room_name=room_name)
        messages_list = list(messages.values())
        for i in messages_list:
            if i["User"] != username:
                # translator = Translator()
                # result = translator.translate(i["Message"], dest=lang)
                # i["Message"]=result.text
                i["Delivered_dttm"] = i["Delivered_dttm"].strftime("%I:%M %p")
            else:
                i["Delivered_dttm"] = i["Delivered_dttm"].strftime("%I:%M %p")
        return JsonResponse({"messages":messages_list})


