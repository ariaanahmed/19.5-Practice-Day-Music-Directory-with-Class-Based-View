from django.views.generic import CreateView
from . import models
from . import forms
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(login_required(login_url=reverse_lazy("home")), name="dispatch")
class AddMusician(CreateView):
    model = models.Musician
    form_class = forms.MusicianForm
    template_name = "musician.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "Add Musician"
        return context
