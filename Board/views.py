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

chunk_size = 4

# Create your views here.
def main_page(request):
    post_list = Post.objects.all()
    post_list_chunks = list(chunks(post_list, chunk_size)) # Split the post list into smaller 'chunks' of a few posts
    split_post_list = list(chunks(post_list_chunks[0], 2)) # Split the chunks further into 2 parts to fit the GUI
    context = {
        'title': "Big Text Notes by 5hwb",
        'post_list': post_list,
        'split_post_list': split_post_list,
    }
    return render(request, 'home.html', context)

def update_posts(request):
    post_list = Post.objects.all()
    post_list_chunks = list(chunks(post_list, chunk_size))
    #print("post_list_chunks: {}".format(post_list_chunks))

    increment = int(request.GET['append_increment'])
    increment_to = (increment + 1) % len(post_list_chunks)
    #print("Increment: {}".format(increment))

    split_post_list = list(chunks(post_list_chunks[increment_to], 2))
    context = {
        'split_post_list': split_post_list,
    }
    return render(request, 'post_subtable.html', context)

def add_post(request):
    if request.method == 'POST':
        text = request.POST.get("post_text","")
        c = Post(text=text)
        c.save()
        return HttpResponseRedirect(reverse_lazy('main_page'))

    else:
        post_list = Post.objects.all()
        context = {
            'title': "Add a new post - Big Text Notes by 5hwb",
            'post_list': post_list,
        }
        return render(request, 'add_post.html', context)

def edit_post(request, post_pk):
    if request.method == 'POST':
        form_value = request.POST.get("save", "")
        existing_post = Post.objects.get(id=post_pk)
        if (form_value == "Edit"):
            text = request.POST.get("post_text","")
            existing_post.text = text
            existing_post.save()
        elif (form_value == "Delete"):
            existing_post.delete()

        return HttpResponseRedirect(reverse_lazy('main_page'))

    else:
        post_list = Post.objects.all()
        existing_post = Post.objects.get(id=post_pk)
        context = {
            'title': "Edit post - Big Text Notes by 5hwb",
            'post_list': post_list,
            'existing_post': existing_post,
        }
        return render(request, 'edit_post.html', context)
