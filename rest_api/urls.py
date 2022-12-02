from django.urls import path
# from django.conf.urls import include
# from .views import postView, createView, post_details
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PostView, CreateView, PostDetails


urlpatterns = [
    # path('', postView),
    # path('create/', createView),
    # path('details/<int:pk>', post_details)    

    path('', PostView.as_view()),
    path('create/', CreateView.as_view()),
    path('details/<int:pk>', PostDetails.as_view())  

]

urlpatterns = format_suffix_patterns(urlpatterns)
