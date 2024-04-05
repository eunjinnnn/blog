from django.shortcuts import render
from .models import Post #.model은 현재 파일에 있다의미
from django.utils import timezone

def post_list(request):
    posts = Post.objects.all()#쿼리셋
    return render(request, 'blog/post_list.html', {'posts': posts})
