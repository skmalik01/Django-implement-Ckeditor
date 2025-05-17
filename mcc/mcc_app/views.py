from django.shortcuts import render, redirect
from .forms import ArticleForm
from .models import Article

def create_article(request):
    form = ArticleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('form_list')
    return render(request, 'blog/form.html', {'form': form})

def article_list(request):
    articles = Article.objects.all().order_by('-created_at')
    return render(request, 'blog/form_list.html', {'articles': articles})
