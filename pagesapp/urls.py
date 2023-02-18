from django.urls import path
from .views import HomePageView, AboutHomeView, PrivacyPolicyView, ContactPageView

urlpatterns = [
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('privacy/',PrivacyPolicyView.as_view(),name='privacy'),
    path('about/',AboutHomeView.as_view(),name='about'),
    path('',HomePageView.as_view(),name='homepage'),


]
