from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})
@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'blog/post_confirm_delete.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('posts')


@login_required
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'GET':
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'blog/post_form.html', context)

    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'The post has been updated successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form': form})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Set the author to the logged-in user
            post.save()
            messages.success(request, 'The post has been created successfully.')
            return redirect('posts')
        else:
            messages.error(request, 'Please correct the following errors:')
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'blog/post_form.html', context)

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts, 'user': request.user}
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html')





