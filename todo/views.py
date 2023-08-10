from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem

# Create your views here.

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request, 'todo.html',{'all_items': all_todo_items})

def addTodo(request):
    # create a new todo all_items
    a = request.POST['content']
    new_item = TodoItem(content = a)
    
    # save
    new_item.save()

    # Redirect the broswer to main page
    return HttpResponseRedirect('/todo/')

