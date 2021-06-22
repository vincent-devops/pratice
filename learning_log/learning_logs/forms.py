from django import forms  # 导入forms表单模块
from .models import Topic, Entry


class TopicForm(forms.ModelForm):
    class Meta:  # 定义根据哪个模型创建表单，以及表单中包含哪些字段。
        model = Topic  # 根据Topic模型创建表单
        fields = ['text']  # 定义表单中包含的字段
        labels = {'text': ''}  # 让Django不要为字段text生成标签


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        # 定义属性widgets
        # widget小部件是一个HTML表单元素，如单行文本框、多行文本区域或下拉列表。可通过参数指定表单类型，此处为多行文本区域。
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}  # 将文本区域的宽度设置为80列
