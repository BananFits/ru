import os

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from humster.forms import AddPostForm
from humster.models import Travel

menu = [{'title': 'главная', 'url_name': 'home'},
        {'title': 'добавить пост', 'url_name': 'addpost'},
        {'title': 'смотреть путешествия по  id', 'url_name': 'travelsid'},
        {'title': 'смотреть путешествия ', 'url_name': 'travels-slug'},
        ]

def addpost(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form,
    }

    return render(request, 'humster/addpost.html', context=data)


def show_travelid(request, id):
    id = get_object_or_404(Travel, pk=id)

    data = {
        'title': id.title,
        'menu': menu,
        'id': id,

    }

    return render(request, 'humster/travelid.html', context=data)


def show_travelsl(request, sl):
    id = get_object_or_404(Travel, slug=sl)
    data = {

        'menu': menu,
        'id': id,

    }
    return render(request, 'humster/travelid.html', context=data)


def travelsid(request):
    posts = Travel.objects.all()
    data = {
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'humster/travelsid.html', context=data)


def travelslug(request):
    posts = Travel.objects.filter(is_published=1)
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
    }
    return render(request, 'humster/travels-slug.html', context=data)


# Create your views here.
def index(request):
    return render(request, 'humster/index.html', {'menu': menu})



def category(request, cat_id):
    data = {'cat_id': cat_id}
    return render(request, 'humster/cat_id.html', data)
    # ,return HttpResponse(f'<h1>страница хомячки по категориям</h1> <p> Хомячок номер -<b>{cat_id}</b> </p>' )


def category_slug(request, cat_slug):
    data = {'cat_slug': cat_slug}
    return render(request, 'humster/cat_slug.html', data)
    # return HttpResponse(f'<h1>страница хомячки по категориям</h1> <p>  категория -<b>{cat_slug}</b> </p>' )
