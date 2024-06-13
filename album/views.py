from django.views.generic import CreateView, DeleteView
from . import models
from . import forms
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from album .forms import Album


@method_decorator(login_required(login_url=reverse_lazy("home")), name="dispatch")
class AddAlbum(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    template_name = "album.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Add Album"
        return context


# delete post
class DeletePost(DeleteView):
    model = Album
    template_name = 'album_delete.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'id'