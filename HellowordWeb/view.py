#vim: set fileencoding=utf-8:
# from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from HellowordWeb import forms
from django.template import RequestContext
from TestModel.models import Blog
def blog_list(request):
    blog_list = Blog.objects.all()
    return render_to_response('blog_list.html',{'blog_list':blog_list})

def blog_form(request):
    if request.method == 'POST':
        form = forms.BlogForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if 'id' not in data:
                blog = Blog(title=data['title'],author=data['author'],content=data['content'])
                blog.save()
            else:
                blog = Blog.object.get(id=data.id)
                blog.title = data['title']
                blog.author = data['author']
                blog.content = data['content']
                blog.save()
            return HttpResponseRedirect('/blog/list')
    else:
        form = forms.BlogForm()
        return render_to_response('blog_form.html',{'form':form})
def blog_del(request):
    errors = []
    if 'id' in request.GET:
        bid_ = request.GET['id']
        Blog.objects.filter(id=bid_).delete()
        return HttpResponseRedirect('/blog/list')
    else:
        errors.append("参数异常请刷新后重试")
        return render_to_response('blog_list.html', {'errors': errors})
def blog_view(request):
    errors = []
    if 'id' in request.GET:
        bid_ = request.GET['id']
        blog = Blog.objects.get(id=bid_)
        return render_to_response('blog_view.html',{'blog':blog})
    else:
        errors.append("参数异常请刷新后重试")
        return render_to_response("blog_list.hmtl",{'errors':errors})
def blog_edit(request):
    errors = []
    if 'id' in request.GET:
        bid_ = request.GET['id']
        blog = Blog.objects.get(id=bid_)
        form = forms.BlogForm(
                initial = {'id':blog.id,'title':blog.title,'author':blog.author,'content':blog.content}
        )
        return render_to_response('blog_form.html',{'form':form},content_type=RequestContext(request))
    else:
        errors.append("参数异常请刷新后重试")
        return render_to_response("blog_list.html",{'errors':errors})
def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

