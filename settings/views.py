from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

import json

@csrf_exempt
def setting(request):

    if request.method == "POST":
        print "POST Received"
        print request.body
    
    ret = {"id":1, "backup" : True}
    
    return HttpResponse(json.dumps(ret))
