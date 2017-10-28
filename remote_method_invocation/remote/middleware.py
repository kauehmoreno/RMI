#coding:utf-8
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from views import rmi_post

def proxy_rmi_middleware(get_response):

    def middleware(request):
        #before

        if request.method == 'POST':
            redirect_url = '{}/{}/'.format(settings.BASE_URL, 'post')
            request.META['REMOTE_ADDR'] = redirect_url
            request.META['PATH_INFO'] = redirect_url
            request.META['RMI'] = ('post')
            # return HttpResponsePermanentRedirect(reverse('post'))
        response = get_response(request)
        rmi_response = rmi_post(request)

        return rmi_response

    return middleware
