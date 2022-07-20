from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import CommentForm

# Create your views here.
# @login_required(login_url='/auth/login/')
def show(request,slug):
    #  current_user = request.user
    data = get_object_or_404(Post,slug=slug)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = data
            comment.save()
            return redirect('show.post',slug=slug)
    else:
        form = CommentForm()
    context = {'data':data,'form':form}
    return render(request,template_name='show.html',context=context)
