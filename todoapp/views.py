from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import MyTodo
from .forms import TodoForm


# Create your views here.
def allTodos(request):
    tasks = MyTodo.objects.all()
    form = TodoForm()

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('')  # avoid request resubmission in case of page reload

    context = {
        'title': 'Home',
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'todo/alltodos.html', context)


def deleteTodos(request, pk):
    task = MyTodo.objects.get(id=pk)
    task.delete()
    return redirect('alltodos')  # redirect to the all todos page, uses the alias name from the urlpatterns ("alltodos")


def editTodos(request, pk):
    task = MyTodo.objects.get(id=pk)
    updateForm = TodoForm(instance=task)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance=task)  # avoid creating new task in the db
        if updateForm.is_valid():
            updateForm.save()
            return redirect('alltodos')  # redirect to the all todos page using alias name from the urlpatterns

    context = {
        'title': 'Update',
        'task': task,
        'updateForm': updateForm,
    }
    return render(request, 'todo/edittodo.html', context)
