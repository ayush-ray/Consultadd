from django.shortcuts import render, redirect
from blog.forms import BlogForm
from blog.models import Blog


# Create your views here.
def blogging(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        print(form)
        print("hello")
        if form.is_valid():
            print("world")
            bname = form.cleaned_data.get("bname")
            bcontent = form.cleaned_data.get("bcontent")
            uname = request.user.username
            print(bname)
            print(bcontent)
            print(uname)
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
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
