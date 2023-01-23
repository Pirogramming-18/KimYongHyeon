from django import forms
from .models import Idea, Tool

class IdeaForm(forms.ModelForm):
    devtool = forms.ChoiceField(choices=Tool.objects.values_list('name', 'name'), required=True, label='개발 도구')
    class Meta:
        model = Idea
        fields = ("title", "image", "content", "interest")
        labels = {'title': '제목',
                 'image': '이미지',
                 'interest': '관심도',                 
                 'content': '내용'}
    
    def save(self, **kwargs):
        inst = super().save(commit=False)
        inst.devtool = Tool.objects.all().get(name=kwargs.get('devtool'))
        inst.save()
        return inst
        
class ToolForm(forms.ModelForm):
  class Meta:
    model = Tool
    fields = ("__all__")
    labels = {'name': '이름',
              'kind': '종류',
              'content': '내용'}
        
class OrderForm(forms.Form):
  order_list = [('-idea_star', '찜한순'), ('title', '이름순'), ('created_at', '등록순'), ('-created_at', '최신순')]
  order = forms.ChoiceField(choices = order_list, label='정렬')

