from django import forms
from .models import Comments

class CommentForms(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ("post",)
        labels = {
            'user_name' : 'Name',
            'user_email' : 'Email',
            'comments' : 'Comments'
         }
