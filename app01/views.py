from django.shortcuts import render,HttpResponse,redirect
from app01.models import *
import json
# Create your views here.
def login(request):
    return render(request, 'login.html')

def user_valid(request):
    name = request.POST.get("name")
    ret = UserInfo.objects.filter(user=name)
    res={"state":True,"msg":""}
    if not ret:
        res['state']=False
        res['msg']="用户不存在"

    return HttpResponse(json.dumps(res))

def pwd_valid(request):
    name = request.POST.get("name")
    pwd = request.POST.get("pwd")
    user = UserInfo.objects.filter(user=name, pwd=pwd).first()
    res = {"state": False, "msg": "密码错误"}
    if user:
        res['state'] = True
        res['msg'] = ""
    return HttpResponse(json.dumps(res))

def login_sucess(request):
    # return HttpResponse('登录成功')
    obj = redirect('/index/')
    obj.set_cookie('is_login',True)
    return obj


def index(request):
    ret = request.COOKIES.get("is_login")
    if not ret:
        return redirect("/login/")
    return render(request, "index.html", locals())
