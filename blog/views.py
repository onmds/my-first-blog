from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm, UploadFileForm
from django.utils import timezone

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
	form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def upload_file(request):
	if request.method == 'POST':
		forms = UploadFileForm(request.POST, request.FILES)
		if forms.is_valid():
			forms.save()
			return HttpResponseRedirect('/success/url/')
	else:
		forms = UploadFileForm()
	return render(request, 'blog/upload.html', {'forms': forms})


