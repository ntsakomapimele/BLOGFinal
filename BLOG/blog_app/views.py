from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Topic, Post, Comment
from . import forms

# Create your views here.


def homepage(request):
    return render(request, 'Blog.html')

def AI(request):
    return render(request,'AI.html')

def AR(request):
    return render(request, 'AR.html')

def cyberSecurity(request):
   return render (request, 'cyberSecurity.html')

def QuantumComp(request):
    return render(request, 'QuantumComp.html')

def Robotics(request):
    return render(request, 'robotics.html')

def VR(request):
    return render(request, 'VR.html')

def display_topic(request):
    topics = Topic.objects.all()
    
    return render(request,'topics.html', {'topics': topics})




def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    
    prev_p = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    
    next_p = Post.objects.filter(id__gt=post.id).order_by('id').first()

    context = {
        'post': post,
        'previous_post': prev_p,
        'next_post': next_p
    }

    return render(request, 'post_detail.html', context)


def comment_post(request):
    comments = Comment.objects.all()
    return render(request, 'comments/comment_list.html', {'comments': comments})

def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = forms.CommentForm()
    return render(request, 'comments/add_comment.html', {'form': form, 'post': post})



