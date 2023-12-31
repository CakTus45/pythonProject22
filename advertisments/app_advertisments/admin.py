from django.contrib import admin
from .models import Advertisements

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ["id","title","description","price","created_date","created_update","auction"]
    list_filter = ["auction","updated_at"]
    actions = ["make_auction_as_false","make_auction_as_true"]
    fieldsets = (
        ("Общее",{
            "fields":("title","description","user")
        }),("Финансы",{
            "fields":("price","auction")
        }
    ))
    @admin.action(description="Убрать возможность торга")
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Добавить возможность торга")
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)
# Register your models here.
admin.site.register(Advertisements, AdvertisementAdmin)