# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from blog.models import Post


def post_list(request):
    # cur_file_path = os.path.abspath(__file__)
    # parent_file_path = os.path.dirname(os.path.dirname(cur_file_path))
    # target_file_path = os.path.join(parent_file_path, 'templates', 'post_list.html')
    #
    # with open(target_file_path, 'rt') as f:
    #     html = f.read()
    #
    # return HttpResponse(html)

    posts = Post.objects.order_by('-pk')
    context = dict(posts=posts)
    return render(request, 'post_list.html', context)


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        context = dict(post=post)
        return render(request, 'post_detail.html', context)
    except Post.DoesNotExist:
        return HttpResponse(f'<h1>{request.path}값을 가지는 페이지가 없습니다</h1>')


def post_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        text = request.POST['text']
        Post.objects.create(
            author=request.user,
            title=title,
            text=text
        )

        return redirect('url_name_post_list')

    else:
        return render(request, 'post_add.html')
