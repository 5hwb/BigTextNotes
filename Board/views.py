from django.shortcuts import render

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
