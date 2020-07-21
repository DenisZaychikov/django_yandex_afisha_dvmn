from django.contrib import admin
from .models import Excursion, Image
from django.utils.safestring import mark_safe
from adminsortable2.admin import SortableInlineAdminMixin

IMAGE_WIDTH = 200


@admin.register(Image)
class AdminImage(admin.ModelAdmin):
    readonly_fields = ['get_preview']

    def get_preview(self, obj):
        return mark_safe('<img src="{url}" height=200 />'.format(
            url=obj.image.url, ))


class AdminImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = Image
    list_display = ('image', 'get_preview',)
    readonly_fields = ['get_preview']
    extra = 0

    def get_preview(self, obj):
        return mark_safe('<img src="{url}" width={width} />'.format(
            url=obj.image.url,
            width=IMAGE_WIDTH, ))


@admin.register(Excursion)
class AdminExcursion(admin.ModelAdmin):
    inlines = [AdminImageInline]
