from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import UserRegisterForm, UserLoginForm, ProfileUpdateForm, UserRoleUpdateForm
from .decorators import moderator_required, admin_required

def register_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Вітаємо, {user.username}! Ваш акаунт успішно створено.")
            return redirect('accounts:profile')
    else:
        form = UserRegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('accounts:profile')

    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"З поверненням, {user.username}!")
            return redirect('accounts:profile')
    else:
        form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Ви успішно вийшли з системи.")
    return redirect('accounts:login')


@login_required
def profile_view(request, pk=None):
    if pk:
        profile_user = get_object_or_404(CustomUser, pk=pk)
    else:
        profile_user = request.user
    return render(request, 'accounts/profile_detail.html', {'profile_user': profile_user})


@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Ваш профіль успішно оновлено!")
            return redirect('accounts:profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'accounts/profile_edit.html', {'form': form})


@moderator_required
def user_list_view(request):
    queryset = CustomUser.objects.all().order_by('-date_joined')
    role_filter = request.GET.get('role')
    search_query = request.GET.get('q')

    if role_filter:
        queryset = queryset.filter(role=role_filter)
    if search_query:
        queryset = queryset.filter(
            username__icontains=search_query
        ) | queryset.filter(
            first_name__icontains=search_query
        ) | queryset.filter(
            last_name__icontains=search_query
        )

    return render(request, 'accounts/user_list.html', {'users': queryset})


@admin_required
def user_role_edit_view(request, pk):
    target_user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = UserRoleUpdateForm(request.POST, instance=target_user)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Роль користувача {user.username} змінено на '{user.get_role_display()}'.")
            return redirect('accounts:user_list')
    else:
        form = UserRoleUpdateForm(instance=target_user)
    return render(request, 'accounts/user_role_edit.html', {'target_user': target_user, 'form': form})
