from django.shortcuts import render, get_object_or_404
from .models import News_post

# Create your views here.
def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def news_detail(request, pk):
    news = get_object_or_404(News_post, pk=pk)
    return render(request, 'news/news_detail.html', {'news': news})