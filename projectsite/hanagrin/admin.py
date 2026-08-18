from django.contrib import admin

from hanagrin.models import Priority, Category, Task, Note, SubTask

@admin.register(Priority)
class PriorityAdmin(admin.ModelAdmin):
    list_display = ("priority_name",)
    search_fields = ("priority_name",)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name",)
    search_fields = ("category_name",)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("task_title", "status", "task_deadline", "priority", "category",)
    list_filter = ("status","priority", "category",)
    search_fields = ("task_title", "task_description")
 
@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ("note_content",)
    
@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("subTask_title", "status", "parent_task",)
    list_filter = ("status",)
    search_fields = ("subTask_title",)



