from django.contrib import admin
from .models import Registration, EventRegistration
# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ("event", "user")

class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ("event", "registrations")

    @admin.display(empty_value='0')
    def event(self, obj):
        name = obj.event.split()
        event = ""
        for i in name:
            event += i.lower().capitalize()
            event += " "
        event = event.rstrip()
        return event

admin.site.register(Registration, RegistrationAdmin)
admin.site.register(EventRegistration, EventRegistrationAdmin)