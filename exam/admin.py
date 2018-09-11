from django.contrib import admin
from exam.models import Subject

# Register your models here.
from exam.models import Lac,Subject

class LacAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Lac._meta.fields]
admin.site.register(Lac,LacAdmin)

class SubjectAdmin(admin.ModelAdmin):
	list_display= [f.name for f in Subject._meta.fields]
admin.site.register(Subject,SubjectAdmin)
	

