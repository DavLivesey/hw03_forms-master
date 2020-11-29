from django import forms
from django.db import models
from .models import Post, Group

'''Нижележащий код старался изменить согласно Вашим комментариям:
class PostForm(forms.ModelForm):   
    text = forms.CharField(widget= forms.Textarea)
    group = forms.ModelChoiceField(queryset=Group.objects.all(), required=False)
    class Meta:
        model = Post
        fields = ['text', 'group']
        labels = {'text':'Введите текст', 'group':'Выберите группу'}
        help_texts = {'text':'Любую абракадабру', 'group':'Из уже существующих'}

Но пока не получилось сделать его работающим. В дальнейшем буду еще с ним экспериментировать (например, постараюсь сделать без цикла в html),
а на данный момент куда важнее пройти ревью'''


class PostForm(forms.ModelForm):   
    text = forms.CharField(widget= forms.Textarea, label='Введите текст', help_text='Любую абракадабру') 
    group = forms.ModelChoiceField( 
        queryset=Group.objects.all(), required=False, label = 'Выберите группу', help_text='Из уже существующих' 
        ) 
    class Meta(): 
        model = Post
        fields = ['text', 'group']