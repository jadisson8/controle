from django.contrib import admin
from cadastro.models import discente, emprestimo

# Register your models here.


class emprestimoInline(admin.TabularInline):
    model = emprestimo
    extra = 0


@admin.register(discente)
class discenteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'periodo', 'turno']
    search_fields = ['nome']

    inlines = [emprestimoInline]
