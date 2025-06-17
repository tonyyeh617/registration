from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.contrib import messages
from django.contrib.auth import get_user_model

# 首頁
def index(request):
    return render(request, 'index.html')

# Page1 頁面（會員專區）
def page1(request):
    return render(request, 'page1.html')

# 註冊新會員
def useradd(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        tel = request.POST.get('phone')
        cBirthday = request.POST.get('birthday')
        email = request.POST.get('email')

        User = get_user_model()

        # 檢查帳號是否存在
        if User.objects.filter(username=username).exists():
            messages.error(request, "帳號已被使用，請使用其他帳號。")
            return render(request, 'useradd.html')

        # 檢查密碼是否一致
        if password != repassword:
            messages.error(request, "密碼與確認密碼不一致，請重新輸入。")
            return render(request, 'useradd.html')
   
        # 若通過以上檢查，建立新帳號
        user = User.objects.create_user(username=username, password=password, email=email)
        print(f"tel={tel}")
        user.is_staff = False # 工作人員狀態，設定True則可以登入admin後台
        user.is_active = True
        user.tel = tel
        user.cBirthday = cBirthday
        user.save()

        messages.success(request, "註冊成功，請登入。")
        return redirect('userlogin')

    return render(request, 'useradd.html')

# 登入
def userlogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"歡迎 {username} 回來！")
            return redirect('/index/')
        else:
            messages.error(request, "登入失敗，請檢查帳號與密碼")
            return redirect('/userlogin/')
    
    return render(request, 'userlogin.html')

# 登出
def userlogout(request):
    logout(request)
    messages.info(request, "您已成功登出")
    return redirect('/index/')
