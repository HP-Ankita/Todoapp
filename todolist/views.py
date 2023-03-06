from django.shortcuts import render
#imports data from todolist
from .models import Todolist
# Create your views here.

def index(request):
    todo_items = Todolist.objects.order_by('id') #shows items in Todolist
    context = {'todo_items' : todo_items}
    return render(request,'todolist/index.html', context)