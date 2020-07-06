from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post, Author
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic


def post_list(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'learning_form/post_list.html', context)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('learning_form:post_detail', args=(post.pk, )))
    else:
        form = PostForm()
    return render(request, 'learning_form/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('learning_form:post_detail', args=(post.pk, )))
    else:
        form = PostForm(instance=post)
    return render(request, 'learning_form/post_edit.html', {'form': form})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    return render(request, 'learning_form/post_detail.html', context)


class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'
    initial = {'date_of_death': '05/01/2018'}


class AuthorUpdate(UpdateView):
    model = Author
    fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']


class AuthorDelete(DeleteView):
    model = Author
    success_url = reverse_lazy('learning_form:author_list')


class AuthorDetailView(generic.DetailView):
    def get_queryset(self):
        return Author.objects


class AuthorListView(generic.ListView):
    def get_queryset(self):
        return Author.objects.all()
