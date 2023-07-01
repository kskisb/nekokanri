from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin

# index画面を表示
class IndexView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.order_by('-id')
        return render(request, 'app/index.html', {
            'post_data' : post_data
        })

# detail画面を表示
class PostDetailView(View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_detail.html', {
            'post_data' : post_data
        })

# create画面を表示
class CreatePostView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        return render(request, 'app/post_form.html', {
            'form' : form
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.owner = request.user
            post_data.name = form.cleaned_data['name']
            post_data.birthday = form.cleaned_data['birthday']
            post_data.sex = form.cleaned_data['sex']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.mated_at = form.cleaned_data['mated_at']
            post_data.days_to_conceive = form.cleaned_data['days_to_conceive']
            post_data.save()
            return redirect('post_detail', post_data.id)
        
        return render(request, 'app/post_form.html', {
            'form': form
        })

# edit画面を表示
class PostEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None,
            initial = {
                'name': post_data.name,
                'birthday': post_data.birthday,
                'sex': post_data.sex,
                'image': post_data.image,
                'mated_at': post_data.mated_at,
                'days_to_conceive': post_data.days_to_conceive,
            }
        )

        return render(request, 'app/post_form.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post.objects.get(id=self.kwargs['pk'])
            post_data.owner = request.user
            post_data.name = form.cleaned_data['name']
            post_data.birthday = form.cleaned_data['birthday']
            post_data.sex = form.cleaned_data['sex']
            if request.FILES:
                post_data.image = request.FILES.get('image')
            post_data.mated_at = form.cleaned_data['mated_at']
            post_data.days_to_conceive = form.cleaned_data['days_to_conceive']
            post_data.save()
            return redirect('post_detail', self.kwargs['pk'])
        
        return render(request, 'app/post_form.html', {
            'form': form
        })

# delete画面を表示
class PostDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        return render(request, 'app/post_delete.html', {
            'post_data': post_data
        })
    
    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')