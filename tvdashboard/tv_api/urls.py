from django.urls import path
from .views import *



urlpatterns = [
    path('line', LinePhase.as_view()),
    path('single', SinglePhase.as_view()),
    path('sm', SmallMediumPhase.as_view()),
    path('large', LargePhase.as_view()),
    path('industrial', IndustrialPhase.as_view()),
]
