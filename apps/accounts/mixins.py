from django.contrib.auth.mixins import UserPassesTestMixin

class ModeratorOrAdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.role in ['moderator', 'admin'] or user.is_superuser)


class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.role == 'admin' or user.is_superuser)
