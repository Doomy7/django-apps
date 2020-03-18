from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .models import toDoListItems

# Create your views here.
def index(request):
    # query for tasks and sending it to html index
    to_do_list = toDoListItems.objects.all()
    return render(request, 'toDoSticker/index.html', {'to_do_list': to_do_list})

# for deletion
def delete(request, id):
    item_to_delete = toDoListItems.objects.get(pk=id)
    item_to_delete.delete()
    return HttpResponseRedirect('../../')

# for adding a new item get from POST the [task, time]
# and add them to the database. then redirect to index
def add(request):
    task = request.POST.get('task')
    time = request.POST.get('time')
    new_item = toDoListItems(listItem=task, time_limit=time)
    new_item.save()
    return HttpResponseRedirect('../')