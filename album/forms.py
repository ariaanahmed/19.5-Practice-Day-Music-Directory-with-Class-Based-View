from django import forms
from .models import Album


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            "album_title": forms.TextInput(attrs={"placeholder": "Album"}),
            "release_date": forms.DateInput(
                attrs={"type": "date", "placeholder": "Release date"}
            ),
            "musician": forms.Select(attrs={"default": 1, "required": False}),
            "rating": forms.Select(attrs={"default": 1}),
        }

        labels = {
            "album_title": "",
            "release_date": "",
            "musician": "",
            "rating": "",
        }
