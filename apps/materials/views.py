from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.urls import reverse_lazy
from django.views import generic

from .forms import MaterialForm
from .models import Material


class MaterialListView(generic.ListView):
    model = Material
    template_name = 'materials/list.html'
    context_object_name = 'materials'
    paginate_by = 12


class MaterialDetailView(generic.DetailView):
    model = Material
    template_name = 'materials/detail.html'


class MaterialCreateView(LoginRequiredMixin, generic.CreateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/form.html'
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Матеріал додано.')
        return super().form_valid(form)


class AuthorOrModeratorMixin(UserPassesTestMixin):
    def test_func(self):
        material = self.get_object()
        user = self.request.user
        return user.is_authenticated and (material.author == user or user.is_superuser or user.role in ('admin', 'moderator'))

    def handle_no_permission(self):
        raise Http404('Матеріал не знайдено')


class MaterialUpdateView(LoginRequiredMixin, AuthorOrModeratorMixin, generic.UpdateView):
    model = Material
    form_class = MaterialForm
    template_name = 'materials/form.html'

    def get_success_url(self):
        messages.success(self.request, 'Матеріал оновлено.')
        return reverse_lazy('materials:detail', kwargs={'pk': self.object.pk})


class MaterialDeleteView(LoginRequiredMixin, AuthorOrModeratorMixin, generic.DeleteView):
    model = Material
    template_name = 'materials/confirm_delete.html'
    success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        messages.success(self.request, 'Матеріал видалено.')
        return super().form_valid(form)
