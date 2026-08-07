from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm

def album_list(request):
    albums = Album.objects.all()
    return render(request, 'gallery/album_list.html', {'albums': albums})

def album_detail(request, pk):
    album = get_object_or_404(Album, pk=pk)
    photos = album.photos.all()
    return render(request, 'gallery/album_detail.html', {'album': album, 'photos': photos})

@login_required
def album_create(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)
            album.author = request.user
            album.save()
            return redirect('gallery:album_detail', pk=album.pk)
    else:
        form = AlbumForm()
    return render(request, 'gallery/album_form.html', {'form': form})

@login_required
def photo_upload(request, album_pk):
    album = get_object_or_404(Album, pk=album_pk)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.album = album
            photo.uploaded_by = request.user
            photo.save()
            return redirect('gallery:album_detail', pk=album.pk)
    else:
        form = PhotoForm()
    return render(request, 'gallery/photo_form.html', {'form': form, 'album': album})
