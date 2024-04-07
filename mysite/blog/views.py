from django.shortcuts import render
from .models import Post #.model은 현재 파일에 있다의미
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
