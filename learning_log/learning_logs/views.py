from django.shortcuts import render
from django.http import HttpResponseRedirect  # 重定向
from django.urls import reverse  # 此函数根据指定的URL模型确定URL
from .models import Topic, Entry  # 导入与所需数据相关联的模型
from .forms import TopicForm, EntryForm


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


def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据：创建一个空表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)  # 使用用户输入的数据创建一个TopicForm实例，form将包含用户提交的信息
        if form.is_valid():  # 核实用户是否填写了所有必不可少的字段，且输入的数据与要求的字段类型一致
            form.save()  # 保存数据到数据库
            return HttpResponseRedirect(reverse('learning_logs:topics'))  # 跳转到指定的topics url
    context = {'form': form}  # 上下文字典
    return render(request, 'learning_logs/new_topic.html', context)


def new_entry(request, topic_id):
    """在特定的主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)  # 将提交的数据存储到new_entry中，但不不将它保存到数据库。
            new_entry.topic = topic  # 关联对应的主题
            new_entry.save()  # 保存到数据库
            # 重定向到显示相关主题的页面
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)  # 获取用户要修改的条目对象
    topic = entry.topic  # 获得与该条目相关联的主题
    if request.method != 'POST':
        # GET请求，使用当前条目填充表单
        form = EntryForm(instance=entry)  # 这个实参让Django创建一个表单，并使用条目对象中的信息填充它
    else:
        # POST提交的数据，对数据进行处理
        # 让Django根据既有对象创建一个表单实例，并根据request.POST中的相关数据对其进行修改
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',
                                                args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
