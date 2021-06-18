from django import forms
from .models import Post

class ScheduleForm(forms.Form):
    class Meta:
        model = Post
        fields = ['name', 'title', 'pub_date']

    widgets = {
        'pub_date': forms.DateInput(attrs={'class': 'form-control'}),
    }

    # 입력받을 값 두개
    username = forms.CharField(error_messages={'required': '작성자를 입력하세요.'}, max_length=100, label="작성자")
    title = forms.CharField(error_messages={'required': '일정을 입력하세요.'}, max_length=100, label="일정 내용")
    pub_date = forms.DateField(error_messages={'required': '일시를 입력하세요.'}, label="일시")

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)