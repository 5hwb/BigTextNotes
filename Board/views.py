from itertools import zip_longest
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post

def chunks(lst, n):
    '''Yield successive n-sized chunks from lst.'''
    '''From here: https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks'''
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

# Number of posts to show in home page
chunk_size = 4

# Web app title
app_title = "Big Text Notes by 5hwb"

def main_page(request):
    '''
    Show the home page
    '''
    post_list = Post.objects.all()
    post_list_chunks = list(chunks(post_list, chunk_size)) # Split the post list into smaller 'chunks' of a few posts
    split_post_list = list(chunks(post_list_chunks[0], 2)) # Split the chunks further into 2 parts to fit the GUI
    context = {
        'title': app_title,
        'post_list': post_list,
        'split_post_list': split_post_list,
    }
    return render(request, 'home.html', context)

def update_posts(request):
    '''
    Show the post update page
    '''
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
    '''
    Show the post creation page
    '''
    if request.method == 'POST':
        text = request.POST.get("post_text","")
        text_colour = request.POST.get("post_text_colour","")
        bg_colour = request.POST.get("post_bg_colour","")
        c = Post(
            text=text,
            text_colour=text_colour,
            bg_colour=bg_colour)
        c.save()
        return HttpResponseRedirect(reverse_lazy('main_page'))

    else:
        post_list = Post.objects.all()
        context = {
            'title': "Add a new post - " + app_title,
            'post_list': post_list,
            'TEXT_COLOUR_CHOICES': Post.TEXT_COLOUR_CHOICES,
            'BG_COLOUR_CHOICES': Post.BG_COLOUR_CHOICES,
        }
        return render(request, 'add_post.html', context)

def edit_post(request, post_pk):
    '''
    Show the post editing page
    '''
    if request.method == 'POST':
        form_value = request.POST.get("save", "")
        existing_post = Post.objects.get(id=post_pk)
        if (form_value == "Edit"):
            text = request.POST.get("post_text","")
            text_colour = request.POST.get("post_text_colour","")
            bg_colour = request.POST.get("post_bg_colour","")
            existing_post.text = text
            existing_post.text_colour = text_colour
            existing_post.bg_colour = bg_colour
            existing_post.save()
        elif (form_value == "Delete"):
            existing_post.delete()

        return HttpResponseRedirect(reverse_lazy('main_page'))

    else:
        post_list = Post.objects.all()
        existing_post = Post.objects.get(id=post_pk)
        context = {
            'title': "Edit post - " + app_title,
            'post_list': post_list,
            'existing_post': existing_post,
            'TEXT_COLOUR_CHOICES': Post.TEXT_COLOUR_CHOICES,
            'BG_COLOUR_CHOICES': Post.BG_COLOUR_CHOICES,
        }
        return render(request, 'edit_post.html', context)

def show_all_posts(request):
    '''
    Show the 'all posts' page
    '''
    post_list = Post.objects.all()
    context = {
        'title': "All posts - " + app_title,
        'post_list': post_list,
    }
    return render(request, 'show_all_posts.html', context)
