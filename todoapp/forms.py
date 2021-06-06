from django import forms
from .models import MyTodo


class TodoForm(forms.ModelForm):
    class Meta:
        model = MyTodo
        fields = ['task']
        labels = {'task': 'Task'}

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        self.fields['task'].widget.attrs['style'] = 'width: 650px; height: 48px;'
