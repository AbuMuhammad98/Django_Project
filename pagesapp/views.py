from django.views.generic import TemplateView





# Create your views here.
class HomePageView(TemplateView):
    template_name = 'homepage.html'

class AboutHomeView(TemplateView):
    template_name = 'about.html'

class PrivacyPolicyView(TemplateView):
    template_name = 'privacy.html'

class ContactPageView(TemplateView):
    template_name = "contact.html"