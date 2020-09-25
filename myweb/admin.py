from django.contrib import admin
from .models import Choice, Question, Signup, Feedback, Product
admin.site.site_title = 'Covid'
admin.site.site_header = 'Dullahan Administration'

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer_name', 'date', 'happy',)
    list_filter = ('product', 'date',)
    search_fields = ('product__name', 'details',)

    class Meta:
        model = Feedback

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Signup)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Product)
