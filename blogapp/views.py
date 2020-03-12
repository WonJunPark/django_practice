from django.shortcuts import render, redirect
from .forms import CreateBlog

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blogMain(request):
    return render(request, 'blogMain.html')


def createBlog(request):
    if request.method == 'POST':
        form = CreateBlog(request.POST)

        if form.is_valid():
            form.save()
            return redirect('blogMain')
        else:
            return redirect('index')
    else:
        form = CreateBlog()
        return render(request, 'createBlog.html', {'form': form})
