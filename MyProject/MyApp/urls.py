from django.urls import path
from .import views


urlpatterns = [
    path('' , views.home.as_view() , name='home'),
    path('all_candidates/' , views.all_candidates.as_view() , name='all_candidates'),
    path('candidate_info/<int:pk>' , views.candidate_info.as_view() , name='candidate_info'),
    path('about/' , views.about.as_view() , name='about'),
    path('contact/' , views.contact.as_view() , name='contact'),

]