from django.contrib import admin
from .models import BashQuote, BashAbyssQuote

# Register your models here.
class BashQuoteAdmin(admin.ModelAdmin):
	list_display = ( 'link', 'comics', 'quote_id', 'date', 'rating')
	list_filter = ('date', 'is_comics')

class BashAbyssQuoteAdmin(admin.ModelAdmin):
	list_display = ('quote_id', 'date')
	list_filter = ('date', )


admin.site.register(BashQuote, BashQuoteAdmin)
admin.site.register(BashAbyssQuote, BashAbyssQuoteAdmin)
