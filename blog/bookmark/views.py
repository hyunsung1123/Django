from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark, Answer
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .forms import AnswerForm,ReplyForm
from django.http import HttpResponseNotAllowed

class BookmarkLV(ListView) :
    model = Bookmark

class BookmarkDV(DetailView) :
    model = Bookmark

class AnswerLV(ListView) :
    model = Answer

class AnswerDV(DetailView) :
    model = Answer

def reply_create(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.create_date = timezone.now()
            reply.Answer = answer
            reply.save()
            return redirect('detail', pk=answer_id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'answer': answer, 'form': form}
    return redirect('detail', pk=answer_id)

def answer_create(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('index')
    else:
        form = AnswerForm()
    context = {'form': form}
    return render(request, 'bookmark/answer_form.html', context)