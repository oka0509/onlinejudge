from django.shortcuts import render, get_object_or_404
from .models import Problem

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, 'onlinejudge/problem_list.html', {'problems':problems})

def problem_detail(request, pk):
    problem = get_object_or_404(Problem, pk=pk)
    return render(request, 'onlinejudge/problem_detail.html', {'problem': problem})