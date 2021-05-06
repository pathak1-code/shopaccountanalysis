from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse


class LoginRequiredMiddleware():
    def __init__(self,get_response):
        self.get_response=get_response
        #print(self.get_response)


    def __call__(self,request):
        response=self.get_response(request)
        return response
    
    def process_view(self,request,view_func,view_args,view_kwargs):
        if request.path.startswith(reverse('login')) or request.path.startswith(reverse('home')):
            return None

        assert hasattr(request,'user')

        if not request.user.is_authenticated:
            if True:
                return redirect(settings.LOGIN_URL)