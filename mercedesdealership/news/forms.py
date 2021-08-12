from django import forms
from .models import News
from django.core.exceptions import ValidationError
class NewsForm(forms.ModelForm):
    class Meta:
        model=News
        fields="__all__"
        exclude=["likes","author","likes_number"]

    def clean_title(self):
        title=self.cleaned_data["title"]
        if News.objects.all().filter(title=title).exists():
            raise ValidationError("There is already an article with that name")
        return title
