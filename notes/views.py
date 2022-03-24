from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        print(request)
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        add_nota(title, content)
        return redirect('index')
        
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        deletar_nota(id)
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def editar(request, id):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        editar_nota(id, title, content)
        return redirect('index')
    else:
        nota = Note.objects.get(id=id)
        return render(request, 'notes/editar.html', {'nota': nota})

def add_nota(title, content):
    note = Note(title=title, content=content)
    note.save(note)

def deletar_nota(id):
    Note.objects.get(id=id).delete()

def editar_nota(id, title, content):
    note = Note.objects.get(id=id)
    note.title = title
    note.content = content
    note.save()    

