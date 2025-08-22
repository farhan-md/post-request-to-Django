from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def echo_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body or {})
            return JsonResponse({"ok": True,"You sent": data},status = 200)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"},status = 400)
    
    return JsonResponse({"error": "Only POST allowed"},status = 405)
    
