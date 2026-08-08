from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import AnnouncementForm
from .models import Announcement


class ModeratorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_superuser or user.role in ('admin', 'moderator'))


class AnnouncementListView(generic.ListView):
    model = Announcement
    template_name = 'announcements/list.html'
    context_object_name = 'announcements'
    paginate_by = 10


class AnnouncementDetailView(generic.DetailView):
    model = Announcement
    template_name = 'announcements/detail.html'


class AnnouncementCreateView(LoginRequiredMixin, ModeratorRequiredMixin, generic.CreateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcements/form.html'
    success_url = reverse_lazy('announcements:list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Оголошення опубліковано.')
        return super().form_valid(form)


class AnnouncementUpdateView(LoginRequiredMixin, ModeratorRequiredMixin, generic.UpdateView):
    model = Announcement
    form_class = AnnouncementForm
    template_name = 'announcements/form.html'

    def get_success_url(self):
        messages.success(self.request, 'Оголошення оновлено.')
        return reverse_lazy('announcements:detail', kwargs={'pk': self.object.pk})


class AnnouncementDeleteView(LoginRequiredMixin, ModeratorRequiredMixin, generic.DeleteView):
    model = Announcement
    template_name = 'announcements/confirm_delete.html'
    success_url = reverse_lazy('announcements:list')

    def form_valid(self, form):
        messages.success(self.request, 'Оголошення видалено.')
        return super().form_valid(form)
