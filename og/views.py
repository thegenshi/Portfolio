from django.shortcuts import render
from og.models import Skill, Message, Project, About_me
from django.http import HttpResponseRedirect
# Create your views here.


def og(request):
    Skills = Skill.objects.all()
    Projects = Project.objects.all()
    About_mee = About_me.objects.all()
    return render(request, 'index.html', {'Skill':Skills, 'Project':Projects, 'About_me':About_mee})

def message(request):
    if request.method=="POST":
        message = Message()
        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.text = request.POST.get('message')
        message.save()
        return HttpResponseRedirect('/')
