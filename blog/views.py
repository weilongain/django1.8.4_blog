from django.shortcuts import render
from django.views import generic
from . import models
from .models import Tag,MyBlog

# Create your views here.


def index(request):
    return render(request, 'blog/index.html', )

class BlogIndex(generic.ListView):
    queryset = models.MyBlog.objects.filter(publisher="True").order_by("-pub_date")
    template_name = "blog/index.html"
    paginate_by = 2


class BlogPost(generic.DetailView):
    model = MyBlog
    template_name = "blog/blogpost.html"




def blogTag(request,pk):
    queryset=models.Tag.objects.get(id=pk).myblog_set.all().filter(publisher="True").order_by("-pub_date")
    context = {"queryset":queryset}
    return render(request,"blog/blogtag.html",context)

