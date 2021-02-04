from django.shortcuts import render
from django.views import generic

from .models import Post


def index(request): 
    return render(request, 'index.html')


class PostListView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created')
    template_name = 'index.html'


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "post_detail.html"


class PostCreateView(generic.CreateView):
    model = Post
    fields = ['title', 'content', 'due_date', 'status']

    def form_valid(self, form):
        form.instance.owner = self.rquest.user
        return super().form_valid(form)