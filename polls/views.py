from django.shortcuts import render
from .models import *


def test(request):
    z = TestModule.objects.all().count()
    key = request.GET.get("key")
    key2 = request.GET.get("key2")
    key3 = request.GET.get("key3")
    key4 = request.GET.get("key4")
    if key4:
        key2 = key4
    if key2:
        p = TestModule.objects.get(id=int(key2))
        if key:
            p.otvet = key
            p.okornot()
        if key4:
            p.pod()
        p.save()
    if key3:
        for i in range(1, z):
            dop = TestModule.objects.get(id=i)
            dop.otvet = "noAnswer"
            dop.ok = "noAnswer"
            dop.podsk = "."
            dop.save()
    data = TestModule.objects.all()
    return render(request, "learning.html", context={"list": data})


def converter(request):
    key11 = request.GET.get("key11")
    key12 = request.GET.get("key12")
    if key11:
        p = conv(before=key11)
        p.save()
    res = conv.objects.all()
    if key12:
        res.delete()
    return render(request, "converter.html", context={"list": res})


def converterdate(request):
    key21 = request.GET.get("key21")
    key22 = request.GET.get("key22")
    if key21:
        p = conv(before=key21)
        p.save()
    res = conv.objects.all()
    if key22:
        res.delete()
    return render(request, "converterdate.html", context={"list": res})


def main(request):
    return render(request,"main.html")


def options(request):
    return render(request,"options.html")


def about(request):
    return render(request,"about.html")