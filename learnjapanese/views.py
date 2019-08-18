from django.shortcuts import render
from django.views.generic import CreateView,DetailView,ListView
from .models import Verb
from .forms import NewVerbForm
# Create your views here.


class VerbListView(ListView):
    model = Verb

    def get_queryset(self):
        return Verb.objects.all().order_by('?')[:1]

class VerbCreateView(CreateView):
    redirect_field_name = 'jp/newverb.html'

    model = Verb
    form_class = NewVerbForm
class VerbDetailView(DetailView):
    model = Verb
