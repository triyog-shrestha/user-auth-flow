from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User,Group
from .models import Post

# Create your views here.
@login_required(login_url='/login')
def home(request):
    posts = Post.objects.select_related('author').prefetch_related('author__groups').order_by('-created_at')

    if request.method == 'POST':
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")
        unban_user_id = request.POST.get("unban-user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        
        elif user_id and request.user.is_superuser:
            user = User.objects.filter(id=user_id).first()
            if user and user != request.user and not user.is_superuser:
                user.groups.clear()

        elif unban_user_id and request.user.is_superuser:
            user = User.objects.filter(id=unban_user_id).first()
            if user and user != request.user and not user.is_superuser:
                group, created = Group.objects.get_or_create(name='default')
                group.user_set.add(user)

        return redirect('home')

    return render(request, 'main/home.html', {'posts' : posts})

def logout_user(request):
    logout(request)
    return redirect('login')

def sign_up(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home/')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign-up.html', {'form':form})

@login_required(login_url='/login')
@permission_required("main.add_post", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home/')
    else:
        form = PostForm()
    
    return render(request, 'main/create_post.html' , {'form':form})
