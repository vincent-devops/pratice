"""定义learning_logs的URL模式"""
from django.conf.urls import url  # 需要此函数来讲URL映射到视图
from . import views  # 导入app内的views模块

app_name = 'learning_logs'
urlpatterns = [  # urlpatterns：包含可在应用程序learning_logs中请求的网页
    # 主页
    url(r'^$', views.index, name='index', )  # Django在urlpatterns中查找与请求的URL字符串匹配的正则表达式
]
