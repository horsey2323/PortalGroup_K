from django.contrib.auth.decorators import user_passes_test

def moderator_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and (u.role in ['moderator', 'admin'] or u.is_superuser),
        login_url='accounts:login'
    )
    return actual_decorator(view_func)


def admin_required(view_func):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and (u.role == 'admin' or u.is_superuser),
        login_url='accounts:login'
    )
    return actual_decorator(view_func)
