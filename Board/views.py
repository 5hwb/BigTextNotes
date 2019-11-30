from itertools import zip_longest
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
def mainPage(request):
    post_list = Post.objects.all()
    num_of_posts = len(post_list)
    post_list1 = post_list[0:num_of_posts - int(num_of_posts/2)]
    post_list2 = post_list[int(num_of_posts/2)+1:num_of_posts]
    print(post_list1)
    print(post_list2)

    split_post_list = list(zip_longest(post_list1, post_list2))
    context = {
        'title': "Home Whiteboard by 5hwb",
        'post_list': post_list,
        'split_post_list': split_post_list,
    }
    return render(request, 'home.html', context)

def addPost(request):
    if request.method == 'POST':
        text = request.POST.get("postText","")
        c = Post(text=text)
        c.save()
        return HttpResponseRedirect(reverse_lazy('mainPage'))

    else:
        post_list = Post.objects.all()
        context = {
            'title': "Home Whiteboard by 5hwb",
            'post_list': post_list,
        }
        return render(request, 'add_post.html', context)

def editPost(request, post_pk):
    if request.method == 'POST':
        formValue = request.POST.get("save", "")
        existingPost = Post.objects.get(id=post_pk)
        if (formValue == "Edit"):
            text = request.POST.get("postText","")
            existingPost.text = text
            existingPost.save()
        elif (formValue == "Delete"):
            existingPost.delete()

        return HttpResponseRedirect(reverse_lazy('mainPage'))

    else:
        post_list = Post.objects.all()
        existingPost = Post.objects.get(id=post_pk)
        context = {
            'title': "Home Whiteboard by 5hwb",
            'post_list': post_list,
            'existingPost': existingPost,
        }
        return render(request, 'edit_post.html', context)
