from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages

# from .forms import PostForm
# Create your views here.
# def home(request):
#     return HttpResponse("Hello Shubham")


# def home(request):
#     return render(request, 'blog/home.html')


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{
        'posts': posts
    })


def post_detail(request, id):
    posts = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': posts})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post published successfully!')
            return redirect('post_list')
    else:
        form = PostForm()
        
    return render(request, 'blog/post_form.html', {'form': form})


def edit_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form' : form})


def delete_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    messages.success(request, 'Post deleted.')
    return render(request, 'blog/delete_confirm.html', {
        'post' : post
    })