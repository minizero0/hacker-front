from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .models import CUser, Organ, Service, Area, Job, Product, Brand
# from .forms import UserForm, OrganForm, LoginForm

# 맨 첫화면 _ 메인 페이지
def main(request):
    return render(request, 'main.html')

# 소개 페이지
# def introduce(request):
#     return render(request, 'introduce.html')

# 회원가입에서 기관/일반회원을 고를수 있는 선택 페이지
def select(request):
    return render(request, 'select.html')

# 기관 회원가입 페이지
def organ_signup(request):
    return render(request, 'organ_signup.html')

# 일반 회원가입 페이지
def user_signup(request):
    # if request.method == "POST":
    #     form = UserForm(request.POST)
    #     if form.is_valid():
    #         new_user = CUser.objects.create_User(email=form.cleaned_data["email"],
    #                                              password=form.cleaned_data["password"],
    #                                              username=form.cleaned_data["username"],
    #                                              codeNum=form.cleaned_data["codeNum"],
    #                                              phoneNum=form.cleaned_data["phoneNum"],
    #                                              job=form.cleaned_data["job"],
    #                                              license=form.cleaned_data["license"],
    #                                              area=form.cleaned_data["area"],
    #                                              another=form.cleaned_data["another"],
    #                                              image=form.cleaned_data["image"]
    #                                              )
    #         login(request, new_user)
    #         return redirect('main')
    # else:
    #     form = UserForm()
    #     return render(request, 'user_signup.html', {'form':form})
    return render(request,'user_signup.html' )

# 로그인 페이지
def login(request):
    # if request.method == "POST":
    #     form = LoginForm(request.POST)
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = quthenticate(email = email, password = password)
    #     if user is not None:
    #         login(request, user)
    #         return redirect('main')
    #     else:
    #         return HttpResponse('로그인 실패')
    # else:
    #     form = LoginForm()
    #     return render(request, 'login.html', {'form', form})
    return render(request,'login.html' )


# 일반 회원 마이페이지
def mypage(request):
    return render(request, 'mypage.html')
# 일반 회원 마이페이지-나의현황
def situation(request):
    return render(request, 'situation.html')

# 일반 회원 마이페이지-개인정보 수정
def modify(request):
    return render(request, 'modify.html')

# 기관용 마이페이지
def organ_mypage(request):
    return render(request, 'organ_mypage.html')

# 기관에서 봉사 등록 페이지
def register(request):
    return render(request, 'register.html')

# 봉사활동을 선택할 수 있는 페이지
def quest(request):
    return render(request, 'quest.html') 

# 선택한 봉사활동 *설명* 페이지
def quest_what(request):
    return render(request, 'quest_what.html')

# 회원이 상품선택하는 페이지-브랜드 선택
def brands(request):
    return render(request, 'brands.html')

# 회원이 상품선택하는 페이지-상품!!! 선택
def goods(request):
    return render(request, 'goods.html')
 
# 회원이 포인트를 사용 후 잔여포인트 페이지
def point(request):
    return render(request, 'point.html')

def signup_thank(request):
    return render(request, 'signup_thank.html')



