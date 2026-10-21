# URLと処理を対応付けするためにpathを読み込み
from django.urls import path

# learning/views.pyを読み込み
from . import views

# このURL設定の基準一から追加パスかから文字列、views.homeを呼び出す、URL設定にhomeという名前を付ける
urlpatterns = [
    path("", views.home, name="home"),
]