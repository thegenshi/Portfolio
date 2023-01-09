from django.contrib import admin
from og.models import Skill, Message, Project, About_me
# Register your models here.
admin.site.register(Message)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(About_me)