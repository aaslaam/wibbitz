from django.db import models

CONTENT_TYPE = (
    ("webinar","Webinar"),
    ("report","Report"),
    ("blog_post","Blog Post"),
)

class Subscribe(models.Model):
    Email = models.EmailField(max_length=255,null=True, blank=True)
def __str__(self):
        return self.Email

class Customer(models.Model):
    product = models.ForeignKey("web.Product",on_delete=models.CASCADE)
    Logo = models.FileField(upload_to="customers/")

def __str__(self):
        return str(self.id)



class Feature(models.Model):
    Logo = models.FileField(upload_to="Features/images")
    Icon = models.FileField(upload_to="Features/icons")
    icon_background = models.CharField(max_length=255,null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    testimonial_description  = models.TextField(max_length=255)
    testimonial_author = models.CharField(max_length=255)
    author_designation = models.CharField(max_length=255)
    testimonial_logo = models. FileField(upload_to="Features/logos")


def __str__(self):
    return self.title()


class VideoBlog(models.Model):
    image = models.ImageField(upload_to="video_blog/")
    title = models.CharField(max_length=255)
    logo = models.FileField(upload_to="video_blog/logos")

    def __str__(self):
        return self.title

class Testimonial(models.Model):	
    image = models.ImageField(upload_to="testimonial/images")
    logo = models.FileField(upload_to="testimonial/logo", blank=True, null=True)
    description = models.TextField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    designation = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    is_featured = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.name

class Marketing_features(models.Model):
    image = models.FileField(upload_to="Marketing_features/")
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title

class Product(models.Model):
    image = models.FileField(upload_to="products/images")
    hero_image = models.FileField(upload_to="products/hero_images",blank=True,null=True)
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    colour = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(max_length=255)
    logo = models.FileField(upload_to="products/logos")

    def __str__(self):
        return self.title

class Blog(models.Model):
    Image = models.FileField(upload_to="blog/images")
    Title = models.CharField(max_length=255)
    Content_type = models.CharField(max_length=255, choices=CONTENT_TYPE)

    def __str__(self):
        return self.Title  
