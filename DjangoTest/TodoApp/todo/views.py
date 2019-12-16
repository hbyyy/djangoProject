# Create your views here.

from django.shortcuts import render, redirect

from todo.models import Todo


def todoView(request):
    all_todo_items = Todo.objects.all()
    context = dict(items=all_todo_items)
    return render(request, 'todo.html', context)


def addTodo(request):
    if request.method == 'POST':
        content = request.POST['content']
        Todo.objects.create(
            content=content
        )
        return redirect('/todo/')


def deleteTodo(request, todo_id):
    if request.method == 'POST':
        get_choice_item = Todo.objects.get(id=todo_id)
        get_choice_item.delete()
        return redirect('/todo/')
