from django import forms
from .models import Comment

class VideoCommentForm(forms.Form):
    comment = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Comment
        fields = ('comment')
