from django.shortcuts import render, redirect
from .models import *


def index(request):
    if request.method == 'POST':
        print(request)
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')

        if Tag.objects.filter(tag=tag).exists() == False:
            tagNova = Tag(tag=tag)
            tagNova.save(tagNova)

        tag = Tag.objects.get(tag=tag)

        if title != "" and content != "" and tag != "":
            add_nota(title, content, tag)

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
        tag = request.POST.get('tag')

        if Tag.objects.filter(tag=tag).exists() == False:
            tagNova = Tag(tag=tag)
            tagNova.save(tagNova)

        tag = Tag.objects.get(tag=tag)
        
        if title != "" and content != "" and tag != "":
            editar_nota(id, title, content, tag)
        return redirect('index')
    else:
        nota = Note.objects.get(id=id)
        return render(request, 'notes/editar.html', {'nota': nota})

def add_nota(title, content, tag):
    note = Note(title=title, content=content, tag=tag)
    note.save()

def deletar_nota(id):
    Note.objects.get(id=id).delete()

def editar_nota(id, title, content, tag):
    note = Note.objects.get(id=id)
    note.title = title
    note.content = content
    note.tag = tag
    note.save()    

def indexTag(request):
    all_tags = Tag.objects.all()
    for i in all_tags:
        if Note.objects.filter(tag=i.id).exists() == False:
            Tag.objects.get(id=i.id).delete()
    return render(request, 'notes/listaTags.html', {'tags': all_tags})
    
def notasTag(request, idTag):
    all_notes = Note.objects.filter(tag=idTag)
    return render(request, 'notes/tag.html', {'notes': all_notes})
