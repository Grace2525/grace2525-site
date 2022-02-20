from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Blog

def index(request):
    blogs = Blog.objects.order_by('-date_added')[:3]
    content = {'blogs': blogs}
    return render(request,'blog/index.html',content)

def blogShow(request,blogid):
    blog = get_object_or_404(Blog,pk=blogid)
    content = {'blog':blog}
    return render(request,'blog/blogShow.html',content)
