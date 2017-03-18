from django.http import HttpResponse
from qrgen.models import UserInfo
from django.shortcuts import render
from django.utils import timezone

import Crypto
from Crypto.PublicKey import RSA
from Crypto.Util import asn1
from base64 import b64decode

import qrcode
from qrcode.image.pure import PymagingImage

import uuid

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def get_uid(request):
    uid = uuid.uuid4()
    UserInfo.objects.create(uid=uid, ts=timezone.now(), pub_key="")
    return HttpResponse("Created user with UID %s" % uid)

def update_key(request):
    # TODO: POST request. pass uid and public key.
    # TODO: Replace with actual public key and uid.
    uid = "id1"
    pubkey = 'AAAAB3NzaC1yc2EAAAADAQABAAABAQDZSgC7+MTaiEI5cLBWaFEWPPQ8D1XmUs7AGzb1gq3z8OdCx6AoVAg5Lt59Wz8NBSOvRh+m8qUVAkJi3I2oLyPzg28rUmbIo3be7K7s2P9r5JY7Ujr7NboRanEzaL+JEmLYxBy7jXB9SCiF9H6wEaMs9Noqy8h7b1+Jn4OMasmn2aVDvuCoBV2oDcCIjSqSnJU+SQutLkoTNnyMnuTc8jheUzjyF6rP+vyvbc4BLtGNwclOvAvgKTRvrd4bCPDxz3MpbcECUOpQuSrwdyQc+AFicKU9PjD10jhHTL8LNLbUFkU+F4lxt8KbaBzb0/wtOSRiirMmlzPa4hyq8zUEuZLv'

    user_info = UserInfo.objects.get(uid=uid)
    user_info.pub_key = pubkey
    user_info.ts = timezone.now()
    user_info.save()
    return HttpResponse("Updated key for user " + uid)

def user_info(request, uid):
    user_info = UserInfo.objects.get(uid=uid)
    response = "UserID: %s\nTimestamp: %s\nPublic Key: %s\n"
    return HttpResponse(response % (user_info.uid, user_info.ts,
            user_info.pub_key))

def encode_qr(request):
    # TODO: Replace this with actual payload
    payload = 'something something'
    # TODO: Replace this with actual uid
    uid = "id1"

    # Import public key from DB
#     str_pubkey = UserInfo.objects.get(uid=uid).pub_key
#     bin_pubkey = b64decode(bytes(str_pubkey, 'ascii'))
#     key64 = b'MIGJAoGBAJNrHWRFgWLqgzSmLBq2G89exgi/Jk1NWhbFB9gHc9MLORmP3BOCJS9konzT/+Dk1hdZf00JGgZeuJGoXK9PX3CIKQKRQRHpi5e1vmOCrmHN5VMOxGO4d+znJDEbNHODZR4HzsSdpQ9SGMSx7raJJedEIbr0IP6DgnWgiA7R1mUdAgMBAAE='
#     pubkey_obj = RSA.importKey(b64decode(key64))

    # TODO: Use some actual encryption. Maybe.
#     encrypted_payload = keyPub.encrypt(payload, 0)

    encrypted_payload = bytes(payload, 'ascii')

    img_file = 'test.png'
    img = qrcode.make(encrypted_payload, image_factory=PymagingImage)
    img.save(open(img_file, "wb"))

    with open(img_file, "rb") as f:
        return HttpResponse(f.read(), content_type="image/png")
