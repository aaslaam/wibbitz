import json

from django.shortcuts import render, get_object_or_404

from django.http.response import HttpResponse

from web.models import Customer,Subscribe,Feature,VideoBlog,Testimonial,Marketing_features,Product,Blog
def index (request):
   customers = Customer.objects.all()
   features = Feature.objects.all()
   video_blogs = VideoBlog.objects.all()
   testimonials  = Testimonial.objects.filter(is_featured=True)[:2] 
   marketing_features = Marketing_features.objects.all()
   product = Product.objects.all()
   blogs = Blog.objects.all()
   context = {
      "customers": customers,
      "features": features,
      "video_blogs":video_blogs,
      "testimonials": testimonials,
      "marketing_features": marketing_features,
      "products" : product,
      "blogs": blogs


   }
   return  render(request,'index.html',context=context)

def subscribe(request):
    Email = request.POST.get('Email') 
    Subscribe.objects.create(
      Email=Email
      )
    if Subscribe.objects.filter(Email=Email).exists():
        response_data = {
      "status":"success",
      "tittle": "Successfully Registered",
      "message": "You have successfully subscribed to our newsletter"
   }
    else:
          response_data = {
      "status":"error",
      "tittle": "You are already Subscribed",
      "message": "You have already a memeber"
   }
    return HttpResponse(json.dumps(response_data),content_type="application/javascript")     


def product(request, pk):
    product = get_object_or_404(Product.objects.filter(pk=pk))
    customers = Customer.objects.filter(product=product)
    context = {
        "product": product,
        "customers": customers
    }
    return render(request, 'product.html', context=context)