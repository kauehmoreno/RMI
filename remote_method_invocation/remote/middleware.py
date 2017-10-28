#coding:utf-8
from django.conf import settings
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from views import rmi_post

def proxy_rmi_middleware(get_response):

    def middleware(request):
        #before

        if request.method == 'POST':
            request.META['RMI'] = ('post')
            # return HttpResponsePermanentRedirect(reverse('post'))
        response = get_response(request)
        try:
            request.META['RMI']
        except KeyError:
            try:
                request.META['HTTP_RMI']
            except KeyError:
                return response
        rmi_response = rmi_post(request)
        return rmi_response

    return middleware
