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
        print(data)
        form = BlogForm(data)

        if form.is_valid():
            print("Form----->", form)
            try:
                form.save()
            except:
                pass

    else:
        print("Not valid form")
        form = BlogForm()

    return render(request, 'index.html', {'form': form})


def show(request):
    blogs = Blog.objects.all()
    # return render(request, "show.html", {'blogs': blogs})


def update(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("/show")
    # return render(request, 'edit.html', {'blog': blog})


def destroy(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("/show")
