from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from bson.objectid import ObjectId
from .services import create_user, login_user as login_user_service, update_profile as update_profile_service, delete_profile as delete_profile_service

# Helper to stringify BSON ObjectId in responses

def _stringify_objectids(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, dict):
        return {k: _stringify_objectids(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_stringify_objectids(v) for v in obj]
    return obj

@csrf_exempt
@require_http_methods(["POST"]) 
def register_user(request):
    try:
        payload = json.loads(request.body.decode('utf-8'))
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    try:
        data = create_user(payload)
        return JsonResponse(_stringify_objectids(data), status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@require_http_methods(["POST"]) 
def login_user(request):
    try:
        payload = json.loads(request.body.decode('utf-8'))
        email = payload.get('email')
        password = payload.get('password')
        if not email or not password:
            return JsonResponse({"error": "email and password are required"}, status=400)
        data = login_user_service(email, password)
        return JsonResponse(_stringify_objectids(data), status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@require_http_methods(["PUT"]) 
def update_profile(request):
    try:
        payload = json.loads(request.body.decode('utf-8'))
        user_id = payload.get('user_id')
        if not user_id:
            return JsonResponse({"error": "user_id is required"}, status=400)
        data = update_profile_service(user_id, payload)
        return JsonResponse(_stringify_objectids(data), status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"]) 
def delete_profile(request):
    try:
        payload = json.loads(request.body.decode('utf-8')) if request.body else {}
        user_id = payload.get('user_id') or request.GET.get('user_id')
        if not user_id:
            return JsonResponse({"error": "user_id is required"}, status=400)
        data = delete_profile_service(user_id)
        return JsonResponse(data, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)