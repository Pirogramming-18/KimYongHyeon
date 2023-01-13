from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields = ['title', 'director', 'actor', 'genre', 'stars', 'createDate', 'runtime', 'content']
        labels = {
            "title": "제목",
            "director": "감독",
            "actor": "배우",            
            "genre": "장르",
            "stars": "별점",
            "createDate": "개봉일",
            "runtime": "러닝타임",
            "content": "리뷰 내용",            
        }
        

    