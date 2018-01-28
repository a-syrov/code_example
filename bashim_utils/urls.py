from django.urls import path
from .views import create_bash_quote, create_abyss_quote, set_comics,set_current_rating, bash_utils
from .views import set_comics_url, set_img_comics_from_url

urlpatterns = [
	path('', bash_utils, name='bash_utils'),
    path('create_quotes/', create_bash_quote, name='create_quotes'), # Create BashQuotes objects from file
    path('create_quotes_abyss/', create_abyss_quote, name='create_quotes_abyss'), # Create BashAbyssQuotes objects from file
    path('set/', set_comics, name='set_comics'), # Check field 'comics' and set 'is_comics' to True or False
    path('set_current_rating/', set_current_rating, name='set_current_rating'), # Check Quote obj field rating and set to 1 if value not numeric  

    path('set_comics_url/', set_comics_url, name='set_comics_url'), # Set for all is_comics BashQuote field url from comics xpath  
    path('set_img_comics_from_url/', set_img_comics_from_url, name='set_img_comics_from_url'), # Set for all BashQuote.comics_image image from URL  

]