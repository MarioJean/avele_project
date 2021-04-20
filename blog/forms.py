from django import forms
from.models import Comment

class NewCommentForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": " (will not be published)"}
        ),
    )
    class Meta:
        model = Comment
        fields = ("name", "email", "comment")
        