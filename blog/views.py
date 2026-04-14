from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CommentForm
from .models import Comment

# from .forms import PostForm
# Create your views here.
# def home(request):
#     return HttpResponse("Hello Shubham")


# def home(request):
#     return render(request, 'blog/home.html')

def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f"Welcome, {user.username}")
        return redirect('/')
    return render(request, 'blog/register.html', {'form' : form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        messages.error(request, 'Invalid username or password')
    return render(request, 'blog/login.html')

def logout_view(request):
    logout(request)
    return redirect('/login/')

@login_required
def profile_view(request):
    # user_posts = Post.objects.filter(created_by=request.user.username).order_by('-created_at')
    # user_posts = Post.objects.filter(created_by=request.user).order_by('-created_at')
    user_posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/profile.html', {'user_posts': user_posts})
 

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html',{
        'posts': posts
    })


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-created_at')
    form = CommentForm()
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('/login/')
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect(f"/post/{pk}")
        
    return render(request, 'blog/post_detail.html', {
        'post': post,
        'comments' : comments,
        'comment_form' : form,
        })


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


def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance = post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
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
    
