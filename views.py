from django.shortcuts import render, redirect, get_object_or_404

from .models import Blog

# Create your views here.
def index(req):
    return render(req, 'index.html')


def blog(req):
    blogs = Blog.objects #HTML에 나타날 객체 blogs라는 변수를 지정
    return render(req, 'blog.html', {'blogs' : blogs})

#어떤 게시물의 data를 가져올지 id값을 view의 detail함수가 받아온다
def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    #get_object_or_404()
    #id값에 해당하는 객체를 가져오고, 없으면 404창 띄운다
    #(): 원하는 data형식의 model 이름과 게시글의 id값    

    return render(request, 'detail.html', {'blog': blog})


def new(req):
    return render(req, 'new.html')

def create(req):
    if req.method == "POST":
        #form을 통해 받은 data를 POST에 넣어준다
        #POST에 저장한 data를 DB에 저장하도록

        blog = Blog()
        blog.title = req.POST['title']
        blog.body = req.POST['body']
        blog.save()
    return redirect('/blog/') #redirect는 위에서 import해주자

#수정하기 버튼
def edit(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    return render(req, 'edit.html' ,{'blog' : blog})

#수정반영(update)
def update(req, blog_id):
    if req.method == "POST":
        edit = get_object_or_404(Blog, pk = blog_id)
        edit.title = req.POST['title']
        edit.body = req.POST['body']
        edit.save()
    return redirect('/detail/'+str(blog_id))

def delete(req, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()
    return redirect('/blog/')