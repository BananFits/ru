from django import forms


class AddPostForm(forms.Form):
    title = forms.CharField(max_length=255 , label='заголовок')
    slug = forms.SlugField(max_length=255, label='URl')
    content = forms.CharField(widget=forms.Textarea(), required=False, label='Контент')
    is_published = forms.BooleanField(required=False, label='Статус')

