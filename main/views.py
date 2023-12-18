# main/views.py
from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render


def vulnerable_view(request):
    user_input = request.GET.get('input', '')
    return render(request, 'main/vulnerable_template.html', {'user_input': user_input})


def insecure_query_view(request):
    user_input = request.GET.get('input', '')
    query = f"SELECT * FROM main_examplemodel WHERE name = '{user_input}'"
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchone()
    return HttpResponse(f"Query Result: {result}")
