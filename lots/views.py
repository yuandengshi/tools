from django.views.generic import ListView, TemplateView

from .models import Set


class SetListView(ListView):
    model = Set


class LotListView(TemplateView):
    template_name = "lots/lot_list.html"
