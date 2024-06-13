from django.views.generic import ListView
from album.models import Album, Musician
from django.views.generic import UpdateView
from album.forms import AlbumForm
from django.urls import reverse_lazy


class home(ListView):
    template_name = "home.html"
    model = Album

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        musician_data = Musician.objects.all()
        album_data = Album.objects.all()
        combined_data = []
        counter = 1

        for musician in musician_data:
            for album in album_data:
                if album.musician_id == musician.id:
                    combined_data.append(
                        {"counter": counter, "musician": musician, "album": album}
                    )
                    counter += 1

        context["combined_data"] = combined_data
        print(combined_data)

        for i in combined_data:
            print(i)
        return context
    

# update
class EditPost(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = "album.html"
    pk_url_kwarg = 'id'
    def get_success_url(self):
        return reverse_lazy("home")
