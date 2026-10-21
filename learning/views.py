from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# home関数を定義、HTTPリクエストを受け取りレスポンスを返す
def home(request):
    # 文字列を返す
    return HttpResponse("Python学習アプリへようこそ！")