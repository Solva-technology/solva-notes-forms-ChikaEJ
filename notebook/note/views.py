from django.shortcuts import get_object_or_404, redirect, render

from .forms.form import NoteForm
from .models import Note


def all_notes(request):
    all_notes = (Note
                 .objects
                 .select_related('author', 'status')
                 .prefetch_related('categories')
                 .order_by('-created_at')
                 )
    context = {'all_notes': all_notes}
    return render(request, 'notes/all_notes.html', context)


def note_detail(request, note_id):
    note = get_object_or_404(
        Note
        .objects
        .select_related('author', 'status')
        .prefetch_related('categories'),
        pk=note_id
    )
    context = {'note': note}
    return render(request, 'notes/note_detail.html', context)


def note_create_update(request, note_id=None):

    note = get_object_or_404(Note, pk=note_id) if note_id else None

    if request.method == 'POST':
        note_form = NoteForm(request.POST, instance=note)
        if note_form.is_valid():
            saved_note = note_form.save()
            return redirect('notes:note_detail', note_id=saved_note.id)
    else:
        note_form = NoteForm(instance=note)

    return render(
        request,
        'notes/note_form.html',
        {'form': note_form, 'note': note}
    )


def note_delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:all_notes')
