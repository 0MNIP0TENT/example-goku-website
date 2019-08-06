from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

from .forms import VideoCommentForm
from .models import Videos as VideoModel
from .models import Comment as CommentModel

class Videos(ListView):
    template_name = 'videos/videos.html'
    model = VideoModel

class Comment(LoginRequiredMixin,CreateView):
    template_name = 'videos/comment.html'
    model = CommentModel
    success_url = reverse_lazy('videos')
    fields = ('comment',)

    def form_valid(self,form):
        form.instance.author = self.request.user
        self.object = Comment(comment=self.get_form_kwargs())
        self.object = form.save(commit=False)
        self.object.video_id  = self.kwargs['pk']
        return super().form_valid(form)
     
class Submit(LoginRequiredMixin,CreateView):
    template_name = 'videos/submit.html'
    model = VideoModel
    success_url = reverse_lazy('videos')
    fields = ('name','videofile',)

    def form_valid(self,form):
        form.instance.author = self.request.user
        self.object = Videos(videfileo=self.get_form_kwargs().get('files')['videofile'])
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())
