from django.shortcuts import render
from .models import Post


def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    context = {
        # В словарь можно передать переменную
        'title': title,
    }
    # Третьим параметром передаём словарь context
    return render(request, template, context) 
