from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post

# Create your views here.
def mainPage(request):
    #to_message_list = Message.objects.filter(to_user=username).all()
    #post = Post.objects.get(pk=postId)
    context = {
        'title': "Home Whiteboard by 5hwb",
    #    'to_message_list': to_message_list,
    #    'username': username,
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
