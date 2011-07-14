from polls.models import Poll, Choice
from django.contrib import admin
#StackedInline can be changed to TabularInline depending upon users choice
class ChoiceInline(admin.TabularInline):
     model = Choice
     extra = 1

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
         (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('question', 'pub_date')
    inlines = [ChoiceInline]
    
admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)

