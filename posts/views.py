from django.shortcuts import render, redirect  
from .forms import ProfileForm  
from .models import Post  

def post_list(request):  
    posts = Post.objects.all()  
    return render(request, 'posts/list.html', {'posts': posts}) 


def upload_profile(request):  
    if request.method == 'POST':  
        form = ProfileForm(request.POST, request.FILES)  # Include request.FILES!  
        if form.is_valid():  
            form.save()  
            return redirect('PostList')  
    else:  
        form = ProfileForm()  
    return render(request, 'posts/upload.html', {'form': form})  