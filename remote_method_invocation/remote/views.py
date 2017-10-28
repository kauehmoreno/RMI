# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import date
import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def rmi(request):
    payload = dict(
        zip(
            [
                'data_consulta', 'faculdade', 'materia', 'trabalho', 'method',
                'Professor'
            ],
            [
                date.today().strftime('%Y-%m-%d'), 'Universidade Veiga de Almeida',
                'Sistemas Distribuidos', 'RMI(Remote Project Invocation)',
                'get', 'Marcelo Costa'
            ]
        )
    )
    payload.update(request.COOKIES)
    return HttpResponse(content=json.dumps(payload), content_type='application/json')

@csrf_exempt
def rmi_post(request):
    if request.method == 'GET':
        payload = {
            'method': 'get',
            'status': 200
        }
        return HttpResponse(content=json.dumps(payload), content_type='application/json')

    body = json.loads(request.body)
    payload = dict(
        zip(
            [
                'data_consulta', 'faculdade', 'materia', 'trabalho', 'method',
                'Professor'
            ],
            [
                date.today().strftime('%Y-%m-%d'), 'Universidade Veiga de Almeida',
                'Sistemas Distribuidos', 'RMI(Remote Project Invocation)',
                'POST', 'Marcelo Costa'
            ]
        )
    )
    payload.update({'additional_information': body})
    return HttpResponse(content=json.dumps(payload), content_type='application/json')
