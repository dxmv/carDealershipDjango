from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from .models import News
from .forms import NewsForm
def all_news(request):
    news=News.objects.all().order_by("-date")
    paginator=Paginator(news,2)
    page_number=request.GET.get("page")
    page_obj=paginator.get_page(page_number)
    return render(request,"news/all_news.html",{"page_obj":page_obj,"news":news})

def add_news(request):
    if request.method=="POST":
        form=NewsForm(request.POST,request.FILES)
        if form.is_valid():
            article=form.save(commit=False)
            article.author=request.user
            article.save()
            return redirect("/news/")
    else:
        form=NewsForm()
    return render(request,"news/add.html",{"form":form})

def article(request,article_id):
    article=News.objects.get(id=article_id)
    is_liked=article.likes.filter(id=request.user.id).exists()
    return render(request,"news/article.html",{"article":article,"is_liked":is_liked})

def like(request,article_id):
    article = News.objects.get(id=article_id)
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        article.likes_number-=1
        article.save()
    else:
        article.likes.add(request.user)
        article.likes_number+=1
        article.save()
    return redirect(f"/news/{article_id}")

def delete(request,article_id):
    article = News.objects.get(id=article_id)
    if request.method=="POST":
        article.delete()
        return redirect("/news/")
    return render(request,"news/delete.html",{"article":article})

def edit(request,article_id):
    article = News.objects.get(id=article_id)
    if request.method=="POST":
        form=NewsForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            form.save()
            return redirect(f"/news/{article_id}")
    else:
        form=NewsForm(instance=article)
    return render(request,"news/edit.html",{"form":form,"article":article})