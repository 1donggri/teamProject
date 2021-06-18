from django.contrib.auth.hashers import check_password

from django import forms
from .models import Board

class BoardForm(forms.Form):
    class Meta:
        model = Board
        fields = ['name', 'title', 'file']

    # 입력받을 값 두개
    name = forms.CharField(error_messages={'required': '작성자를 입력하세요.'}, max_length=100, label="작성자")
    title = forms.CharField(error_messages={'required': '제목을 입력하세요.'}, max_length=100, label="제목")
    file = forms.FileField(error_messages={'required': '파일을 업로드하세요.'}, label="파일")


    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        # self.fields['file'].required = False