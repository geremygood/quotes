from django.contrib import admin
from api.models import Quote, Author, Topic 

class QuoteAdmin(admin.ModelAdmin):
    fields = [ 'quote_text', 'slug', 'pub_date','author','topic' ]

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Author)
admin.site.register(Topic)

