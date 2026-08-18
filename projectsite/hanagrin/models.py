from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Priority(BaseModel):
    priority_name = models.CharField(max_length=150)

    class Meta:
        verbose_name = "Priority"
        verbose_name_plural = "Priorities"

    def __str__(self):
        return self.priority_name

class Category(BaseModel):
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    category_name = models.CharField(max_length=150)

    def __str__(self): return self.category_name



class Task(BaseModel):
    task_title = models.CharField(max_length=150)
    task_description = models.CharField(max_length=150)
    task_deadline = models.DateField()
    status = models.CharField (max_length=50, choices=[
    ("Pending", "Pending"),
    ("In Progress ", "In Progress"),
    ("Completed", "Completed"),
    ], default="pending")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priority, on_delete=models.CASCADE)

    def __str__(self):
        return self.task_title
    

class Note(BaseModel):
    note_content = models.TextField(max_length=255)

    def __str__(self):
        return self.note_content
    
class SubTask(BaseModel):
    subTask_title = models.CharField(max_length=150)
    subTask_description = models.CharField(max_length=150)
    parent_task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField (max_length=50, choices=[
        ("Pending", "Pending"),
        ("In Progress ", "In Progress"),
        ("Completed", "Completed"),], default="Pending")

    def __str__(self):
        return self.subTask_title
    