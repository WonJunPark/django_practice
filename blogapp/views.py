from django.shortcuts import render
from .forms import CreateBlog

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blogMain(request):
    return render(request, 'blogMain.html')


def createBlog(request):
    form = CreateBlog()

    return render(request, 'createBlog.html', {'form': form})