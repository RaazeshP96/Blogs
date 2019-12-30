from django.shortcuts import redirect, render
from .models import Post
from django.views.generic import ListView, DeleteView, CreateView, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def about_view(request):
    return render(request, 'blogs/about.html')


class PostList(LoginRequiredMixin, ListView):
    queryset = Post.objects.all()
    template_name = 'blogs/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetail(LoginRequiredMixin, DetailView):
    model = Post


class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
