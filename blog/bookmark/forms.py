from django import forms
from bookmark.models import Answer, Reply


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer  # 사용할 모델
        fields = ['title', 'content']  # QuestionForm에서 사용할 Question 모델의 속성
        labels = {
            'title': '제목',
            'content': '내용',
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        labels = {
            'contnet': '답변내용',
        }
