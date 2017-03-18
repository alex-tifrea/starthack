from django.http import HttpResponse
from qrgen.models import UserInfo
from django.shortcuts import render
from django.utils import timezone

import Crypto
from Crypto.PublicKey import RSA

import qrcode
from qrcode.image.pure import PymagingImage

import uuid
import subprocess

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_uid(request):
    uid = uuid.uuid4()
    UserInfo.objects.create(uid=uid, ts=timezone.now(), pub_key="")
    return HttpResponse("Created user with UID %s" % uid)

def user_info(request, uid):
    user_info = UserInfo.objects.get(uid=uid)
    response = "UserID: %s\nTimestamp: %s\nPublic Key: %s\n"
    return HttpResponse(response % (user_info.uid, user_info.ts,
            user_info.pub_key))

def encode_qr(request):
    payload = request.body
    uid = request.POST.get("uid", "") 

    # Import public key from DB
    bin_pubkey = UserInfo.objects.get(uid=uid).pub_key
    formatted_pubkey = """
        -----BEGIN PUBLIC KEY-----
        {0}
        -----END PUBLIC KEY-----
    """.format(bin_pubkey)
    pubkey_obj = RSA.importKey(formatted_pubkey)

    result = subprocess.run(['python2 crypto_helper.py', formatted_pubkey + " " + payload], stdout=subprocess.PIPE)
    #encrypted_payload = pubkey_obj.encrypt(payload)
    encrypted_payload = result.stdout

    img_file = "test.png"
    img = qrcode.make(encrypted_payload, image_factory=PymagingImage)
    img.save(open(img_file, "w"))

    with open(img_file, "rb") as f:
        return HttpResponse(f.read(), content_type="image/png")
