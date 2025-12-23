# Import the path function to define URL patterns
from django.urls import path  

# Import views from the current app (the dot means "this directory")
from . import views  

# Define the list of URL patterns for this app
urlpatterns = [
    # Map the URL 'blogs/' to the view function 'blogs' in views.py
    # 'name="blogs"' gives this route a name so it can be referenced in templates or reverse lookups
    path('blog/', views.blogs, name='blogs'),
    path('', views.home, name='home'),

]
