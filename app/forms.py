from django.forms import ModelForm
from app.models import Todo

class TodoForm(ModelForm):
    class  Meta:
        model = Todo
        fields = ['titel', 'status', 'priority']