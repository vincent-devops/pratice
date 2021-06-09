from django.shortcuts import render
from .models import Topic  # 导入与所需数据相关联的模型


def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')


def topics(request):  # request是Django从服务器那里收到的request对象
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):  # 这个函数接受正则表达式(?P<topic_id>\d+)捕获的值，并将其存储到topic_id中
    """显示单个主题及所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')  # 获取与该主题相关联的条目，并按date_added倒序排序
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
