from django.shortcuts import render, redirect
# from django.http import HttpResponseRedirect
from .models import MyTodo
from .forms import TodoForm
from django.core.paginator import Paginator


# Create your views here.
def allTodos(request):      # Retrieve, Create
    tasks = MyTodo.objects.all()
    form = TodoForm()

    tasksNum = len(tasks)  # dict length/ total num of row in db

    #for paging
    tasksList = tasks
    paginator = Paginator(tasksList, 5)         # display per page = 5
    page = request.GET.get('page')              # get the page num from the URL
    tasks = paginator.get_page(page)     # append all the linked pages to "tasks" queryset

    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todoApp:alltodos')  # avoid request resubmission in case of page reload

    context = {
        'title': 'Home',
        'tasks': tasks,
        'form': form,
        'totalTasksNum': tasksNum,
    }
    return render(request, 'todo/alltodos.html', context)


def deleteTodos(request, pk):   # Delete
    task = MyTodo.objects.get(id=pk)
    task.delete()
    return redirect('todoApp:alltodos')  # redirect to the all todos page, uses the alias name from the urlpatterns ("alltodos")


def editTodos(request, pk):     # Edit
    task = MyTodo.objects.get(id=pk)
    updateForm = TodoForm(instance=task)
    if request.method == 'POST':
        updateForm = TodoForm(request.POST, instance=task)  # avoid creating new task in the db
        if updateForm.is_valid():
            updateForm.save()
            return redirect('todoApp:alltodos')  # redirect to the all todos page using alias name from the urlpatterns

    context = {
        'title': 'Update',
        'task': task,
        'updateForm': updateForm,
    }
    return render(request, 'todo/edittodo.html', context)
