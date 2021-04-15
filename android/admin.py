from django.contrib import admin
from .models import App, Task, UserDownloads

admin.site.register(App)
admin.site.register(Task)
admin.site.register(UserDownloads)
