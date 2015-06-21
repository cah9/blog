from django.shortcuts import render, render_to_response
from .models import Post
from .forms import AddPost
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView



class PostDetailView(DetailView):
    model = Post


def posts(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')
    try:
        posts_pag = paginator.page(page)
    except PageNotAnInteger:
        posts_pag = paginator.page(1)
    except EmptyPage:
        posts_pag = paginator.page(paginator.num_pages)
    context = {'posts': posts_list,
               'pag': posts_pag, }
    return render_to_response('posts/posts.html', context)


def edit(request):
    form = AddPost()
    return render(request, 'posts/edit.html', {'form': form})


def add(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            p = Post()
            p.title = form.cleaned_data['title']
            p.content = form.cleaned_data['content']
            p.save()
            return HttpResponseRedirect(reverse('posts:posts'))
    else:
        form = AddPost()
    return render(request, 'posts/edit.html', {'form': form})


def custom_404(request):
    return render(request, '404.html')


def custom_500(request):
    return render(request, '500.html')


def publish(post_id):
    p = Post.objects.get(id=post_id)
    p.published = True
    p.save()

