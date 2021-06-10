from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

from .forms import PostForms
from django.shortcuts import redirect

from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count

from django.http import JsonResponse
from datetime import timedelta


# Create your views here.

def postList(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/postList.html', {'posts' : posts})

class SingUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/singUp.html'



def postNew(request):
    if request.method == "POST":
        form = PostForms(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.created_date = timezone.now()
            post.save()
            return redirect(('postList'))
    else:
        form = PostForms()
    return render(request, 'blog/postEdit.html', {'form': form,})

@staff_member_required
def numberOfPosts(request):
    users = User.objects.all().annotate(post_count=Count('post'))
    for creator in users:
        creator.post_count
    return render(request, 'blog/numberOfPosts.html',{'users':users})

def profile(request,username,id):
    User.objects.get(username=username,id=id)
    return render(request, 'blog/profile.html', {})

def postLastHour(request):
    response= []
    this_hour = timezone.now()
    one_hour_before = this_hour - timedelta(hours=1)
    posts = Post.objects.filter(published_date__range=(one_hour_before,this_hour))
    for post in posts:
        response.append(
            {
                'title':post.title,
                'author':post.author.username,
                'datetime':post.created_date,
                'text':post.text
            }
        )
    if not response:
        return JsonResponse('No post has been published during the last hour',safe=False)
    return JsonResponse(response,safe=False)

def index(request):
    return render(request, 'blog/index.html',{})

def search(request):
    user_string = request.GET['str1']
    posts = Post.objects.filter(text__icontains = user_string).order_by('-published_date')
    count = 0
    for post in posts:
        count = post.text.count(user_string)

#    flag = True
#    start = 0
#    count = 0
#    for post in posts:
#        while flag:
#            a = post.text.find(user_string,start)
#            if a == -1:
#                flag = False
#            else:
#                count += 1
#                start = a+1

    return render(request, 'blog/search.html',{'user_string':user_string,'posts':posts,'count':count})


def getClientIp(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
            return render(request, 'blog/getClientIp.html', {"ip": ip})
        else:
            ip = request.META.get('REMOTE_ADDR')
            return render(request, 'blog/getClientIp.html', {"ip": ip})






