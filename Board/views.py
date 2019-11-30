from itertools import zip_longest
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    '''From here: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks'''
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Create your views here.
def mainPage(request):
    post_list = Post.objects.all()
    split_post_list = list(chunks(post_list, 2))
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
