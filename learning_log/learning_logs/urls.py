"""定义learning_logs的URL模式"""
from django.conf.urls import url  # 需要此函数来将URL映射到视图
from . import views  # 导入app内的views模块

app_name = 'learning_logs'
urlpatterns = [  # urlpatterns：包含可在应用程序learning_logs中请求的网页
    # 主页
    url(r'^$', views.index, name='index', ),  # Django在urlpatterns中查找与请求的URL字符串匹配的正则表达式
    # 显示所有的主题
    url(r'^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),  # 当URL与模式匹配时，Django将会把topic_id中的值传递给views.topic()函数，并调用此函数。
        # r让Django将这个字符串视为原始字符串，并指出正则表达式包含在引号内。
        # /(?P<topic_id>\d+)/ 与包含在两个斜杠内的整数匹配，并把这个整数存储在一个名为topic_id的实参中;
        # 表达式\d+与包含在两个斜杠内的任何数字都匹配，不管这个数字为多少位；
]
