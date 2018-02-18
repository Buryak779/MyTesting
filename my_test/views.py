from django.shortcuts import render
from .models import Vote, MyTest
from my_test.forms import AnswerForm

def my_test_all(request):
    return render(request, "my_test/tests_all.html", {"test": MyTest.objects.all})

def my_test_single(request, pk):
    questions = Vote.objects.filter(my_test__id=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)

    else:
        form = AnswerForm()
    return render(request, "my_test/test_single.html", {"questions": questions, "form": form})

