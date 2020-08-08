from django.shortcuts import render, redirect
from blog.forms import BlogForm
from blog.models import Blog
import uuid


# Create your views here.
def blogging(request):
    if request.method == "POST":
        data = {
                    'bid': uuid.uuid1(),
                    'uname': request.user.username,
                    'bname': request.POST['bname'],
                    'bcontent': request.POST['bcontent']
                }
        form = BlogForm(data)
        if form.is_valid():
            try:
                form.save()
                return redirect("/home")
            except:
                pass
    else:
        print("Not valid form")
        form = BlogForm()
    return render(request, 'index.html', {'form': form})


def show(request):
    blogs = Blog.objects.
    return render(request, "show.html", {'blogs': blogs})


def update(request):
    if request.method == "POST":
        bid = request.POST['bid']
        blog = Blog.objects.get(bid=bid)
        blog.bcontent = request.POST['bcontent']
        blog.save()
        return redirect("/home")


def destroy(request):
    print(id)
    if request.method == "POST":
        print("hello world")
        print(request.POST['bid'])
        blog = Blog.objects.get(bid=request.POST['bid'])
        print(blog)
        blog.delete()
        return redirect("/home")
        form = BlogForm()
        print(form)

    else:
        print("Not valid form")
        form = BlogForm()
    return render(request, 'index.html', {'form': form})
