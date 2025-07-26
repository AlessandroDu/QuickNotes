from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404

from .models import Note
from .forms import UploadForm

def home(request):
    return render(request, 'QuickNotes/home.html')

def QuickNotes(request):
    data = Note.objects.all()
    return render(request, 'QuickNotes/quicknotes.html', {'notes': data, 'form': UploadForm})

def QuickNote(request, note_id):
    data = Note.objects.get(pk=note_id)
    form = UploadForm(instance=data)

    if data is not None:
        return render(request, 'QuickNotes/quicknote.html', {'note': data, 'form': form})
    else:
        raise Http404("Note does not exist")

def edit(request, note_id):
    data = get_object_or_404(Note, pk=note_id)

    form = UploadForm(request.POST)
    if form.is_valid():
        data.name = form.cleaned_data['name']
        data.content = form.cleaned_data['content']
        data.save()
    return redirect(QuickNotes)

def delete(request, note_id):
    data = Note.objects.get(pk=note_id)   
    if data:
        data.delete()
    return redirect(QuickNotes)

def add(request):
    if request.method == 'POST':
        note = Note.objects.create()
        return redirect(QuickNote, note_id=note.id)  # Redirect to the detail page

    return render(request, 'QuickNotes/quicknotes.html')
