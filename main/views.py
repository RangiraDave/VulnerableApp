# main/views.py
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from .models import ExampleModel
from main.forms import InsecureForm
from django.contrib.auth.decorators import login_required


def vulnerable_view(request):
    user_input = request.GET.get('input', '')
    return render(request, 'main/vulnerable_template.html', {'user_input': user_input})


def secure_query_view(request):
    user_input = request.GET.get('input', '')
    query = "SELECT * FROM main_examplemodel WHERE name = %s"
    with connection.cursor() as cursor:
        cursor.execute(query, [user_input])
        result = cursor.fetchone()
    return HttpResponse(f"Query Result: {result}")


def secure_object_query_view(request):
    user_input = request.GET.get('input', '')
    result = ExampleModel.objects.filter(name=user_input).first()
    return HttpResponse(f"Query Result: {result}")


def insecure_form_view(request):
    form = InsecureForm(request.POST or None)
    return render(request, 'main/insecure_form_template.html', {'form': form})

@login_required
def home(request):
    return render(request, 'main/home.html')
