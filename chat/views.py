from django.shortcuts import render, redirect
from chat.models import Room, Message
from django.http import HttpResponse, JsonResponse
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import datetime

mail_host = "smtp.163.com"
mail_user="vxfnt9"
mail_pass="TTYYOGDYIUKQCAVR"
sender="vxfnt9@163.com"
receivers = ['smicpsyclub@gmail.com','jeff060812@gmail.com']

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    if Room.objects.filter(name=room).exists():
        room_details = Room.objects.get(name=room)
        cr=Message.objects.create(value="{} joined room {}.".format(username, room), user="System", room=room_details.id)
        cr.save()
        #title="{} returned back to room {}!".format(username, room)
        #content="{} returned to room {}. Join: http://127.0.0.1:8000/{}/?username=admin".format(username, room, room)
        #sendEmail(content, title)
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        room_details = Room.objects.get(name=room)
        new_room.save()
        cr=Message.objects.create(value="{} created room {}.".format(username, room), user="System", room=room_details.id)
        cr.save()
        #title="{} created room {}!".format(username, room)
        #content="{} just created room {}. Join: http://127.0.0.1:8000/{}/?username=admin".format(username, room, room)
        #sendEmail(content, title)
        return redirect('/'+room+'/?username='+username)


def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    message = message.replace("<","&lt;")
    message=message.replace(">","&gt;")
    username = username.replace("<","&lt;")
    username=username.replace(">","&gt;")
    if not message.isspace():
        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()
        return HttpResponse('Message sent successfully')
    return HttpResponse('Can not send empty message.')


def getMessages(request, room):
    room_details = Room.objects.get(name=room)
    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})

def sendEmail(content, title):
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)

def leftRoom():
    print(2)