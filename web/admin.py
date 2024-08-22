
from django.contrib import admin
from web.models import Subscribe,Customer,Feature,Testimonial,VideoBlog,Product,Marketing_features,Blog


admin.site.register(Subscribe)
admin.site.register(Customer)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ["title","testimonial_author","author_designation"]
admin.site.register(Feature,FeatureAdmin)

class TestimonialAdmin(admin.ModelAdmin):
        list_display = ["name","description","designation"]

admin.site.register(Testimonial)
admin.site.register(VideoBlog)
admin.site.register(Product)
admin.site.register(Marketing_features)
admin.site.register(Blog)