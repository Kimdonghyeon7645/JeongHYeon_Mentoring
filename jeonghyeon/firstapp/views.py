from django.shortcuts import render
from django.utils import timezone
from .models import Post


def post_list(request):
    posts = Post.objects.all().order_by('created_date')
    print(posts)
    return render(request, 'firstapp/post_list.html', {'posts': posts})
