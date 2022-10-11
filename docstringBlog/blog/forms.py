from dataclasses import fields
from django.forms import ModelForm
from .models import Tag
from django import forms
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
        
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )