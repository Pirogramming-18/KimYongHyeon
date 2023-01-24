from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comment, Like

def main(request, *args, **kwargs):
  comments = Comment.objects.all()
  like = Like.objects.get(id=1).like
  context = {'comments': comments,
             'like': like}
  return render(request, 'index.html', context = context)

@csrf_exempt
def create_comment(request, *args, **kwargs):
  req = json.loads(request.body)
  text = req['text']  
  newComment = Comment(comment = text)
  newComment.save()
  return JsonResponse({'id': newComment.pk, 'text': newComment.comment})

@csrf_exempt
def delete_comment(request, *args, **kwargs):
  req = json.loads(request.body)
  id = req['id']
  Comment.objects.all().get(id=id).delete()
  return JsonResponse({'id': id})

@csrf_exempt
def toggle_like(request, *args, **kwargs):
  data = Like.objects.all().get(id=1)
  data.like = not data.like
  data.save()
  return JsonResponse({'status': data.like})
  