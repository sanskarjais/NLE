from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from django.http import HttpResponseRedirect, HttpResponse
from .forms import TaskForm, AppForm
from rest_framework import permissions
from django.contrib import messages
from .models import Task, App, UserDownloads
from rest_framework import viewsets
from .serializers import AppSerializer

class AppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [permissions.IsAuthenticated]

    
def Home_view(request):
    context = {}
    context['items'] = App.objects.all()
    if request.user.is_superuser:
        return render(request,'admin_home.html', context)
    if request.user.is_authenticated:
        return render(request, 'home.html', context)
    return HttpResponse('<h2><a href="accounts/login">LOGIN REQUIRED</a></h2>')
    
def Delete(request, pk, template_name='delete.html'):
    book = get_object_or_404(App, pk=pk)    
    if request.method=='POST':
        book.delete()
        return HttpResponseRedirect('/')
    return render(request, template_name, {})


def add_new(request):
    if request.method == 'POST':
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit = False)
            form.save()
            return HttpResponseRedirect('/')

    else:
        form = AppForm()
    return render(request, 'add_app.html', {
        'form': form
    })

def add_app(request, pk):
    item = get_object_or_404(App, pk = pk)
    query_set = UserDownloads.objects.filter(user = request.user, visited = True)
    if query_set.exists(): 
        cn = 0
        for i in range(0,len(query_set)):
            # print(pk)
            # print(query_set[i].apps.pk, 'pkss')
            if(pk == query_set[i].apps.pk):
                messages.success(request, 'Task Already Completed')
                cn = 1
                break
        if cn == 0:
            UserDownloads.objects.create(user = request.user, apps = item, visited = True)
    
    else:
        UserDownloads.objects.create(user = request.user, apps = item, visited = True)
    return HttpResponseRedirect('/')

def complete_task(request, pk):
    item = get_object_or_404(UserDownloads, pk = pk)
    query_set = Task.objects.filter(user = request.user, task_completed = True)
    key = item.apps.pk
    if query_set.exists():
        cn = 0
        for i in range(len(query_set)):
            if key == query_set[i].apps.pk:
                messages.success(request, 'Task Already Completed')
                cn = 1
                break
        if cn == 0:
            if request.method == 'POST':
                form = TaskForm(request.POST, request.FILES)
                if form.is_valid():
                    obj = form.save(commit = False)
                    obj.user = request.user
                    obj.apps = item.apps
                    obj.points =  item.apps.points
                    obj.task_completed = True
                    form.save()
                    return HttpResponseRedirect('/')
            # Task.objects.create(user = request.user, apps = item.apps, points = item.apps.points, task_completed = True)
            else:
                form = TaskForm()
        else:
            HttpResponseRedirect('/')

    else:
        # Task.objects.create(user = request.user, apps = item.apps, points = item.apps.points, task_completed = True)
        if request.method == 'POST':
            form = TaskForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit = False)
                obj.user = request.user
                obj.apps = item.apps
                obj.points =  item.apps.points
                obj.task_completed = True
                form.save()
                return HttpResponseRedirect('/')
            # Task.objects.create(user = request.user, apps = item.apps, points = item.apps.points, task_completed = True)
        else:
            form = TaskForm()
        return render(request, 'file.html',{'form' : form})

    return HttpResponseRedirect('/')




class MyApp_View(ListView):
    model = UserDownloads
    template_name = 'my_apps.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = UserDownloads.objects.filter(user = self.request.user)

        return context

class Task_View(TemplateView):
    model = Task
    template_name = 'task.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Task.objects.filter(user = self.request.user)
        total = 0
        for i in context['items']:
            total = total + i.points
        context['total'] = total
 
        return context

def points(request):
    total = 0
    for i in Task.objects.filter(user = request.user):
        total+=i.points
    context = {}
    context['t'] = total
    return render(request, 'po.html', context)

