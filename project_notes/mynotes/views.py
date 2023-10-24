from django.shortcuts import render, get_object_or_404, redirect
from .models import Note

def note_list(request):
    notes = Note.objects.all()
    return render(request, 'mynotes/note_list.html', {'notes': notes})

def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'mynotes/note_detail.html', {'note': note})

def note_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        return redirect('mynotes:note_list')
    return render(request, 'mynotes/note_edit.html')

def note_edit(request, pk):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        note = get_object_or_404(Note, pk=pk)
        note.title = title
        note.content = content
        note.save()
        return redirect('mynotes:note_list')
    note = get_object_or_404(Note, pk=pk)
    return render(request, 'mynotes/note_edit.html', {'note': note})

def note_delete(request, pk):
    if request.method == 'POST':
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return redirect('mynotes:note_list')
    return render(request, 'mynotes/note_delete.html')