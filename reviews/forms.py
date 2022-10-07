from tkinter import Widget
from django import forms
from .models import Review
from django.utils.translation import gettext_lazy as _


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "title": _("리뷰 제목"),
            "content": _("리뷰 내용"),
            "movie_name": _("영화 이름"),
            "grade": _("영화 평점"),
            "imgfile": _("이미지 파일 첨부"),
        }
        # text = '제목을 입력해주세요.'
        # widgets = {
        #     'title': forms.CharField(attrs={'placeholder': text})
        # }
