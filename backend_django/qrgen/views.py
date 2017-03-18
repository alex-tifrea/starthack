from django.shortcuts import render
from qrgen.models import UserInfo
from django.http import HttpResponse

import uuid

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_uid(request):
    uid = uuid.uuid4()
    UserInfo.objects.create(uid=)
    return HttpResponse("Hello, world. You're at the polls index.")

def user_info(request, uid):
    user_info = UserInfo.objects.get(uid=uid)
    response = "UserID: %s\nTimestamp: %s\nPublic Key: %s\n"
    return HttpResponse(response % (user_info.uid, user_info.ts,
            user_info.pub_key))
