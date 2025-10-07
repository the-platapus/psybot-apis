from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .services import create_chat_head_service, list_chat_heads_service, get_chat_head_service, delete_chat_head_service
from bson.objectid import ObjectId

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
def create_chat_head(request):
    try:
        payload = json.loads(request.body.decode('utf-8'))
        user_id = payload.get('user_id')
        user_message = payload.get('user_message')
        if not user_id or not user_message:
            return JsonResponse({"error": "user_id and user_message are required"}, status=400)
    except Exception:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    try:
        data = create_chat_head_service(user_id, user_message)
        return JsonResponse(_stringify_objectids(data), status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@require_http_methods(["GET"]) 
def list_chat_heads(request):
    try:
        user_id = request.GET.get('user_id')
        data = list_chat_heads_service(user_id=user_id) if user_id else list_chat_heads_service()
        return JsonResponse(_stringify_objectids(data), safe=False, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@require_http_methods(["GET"]) 
def get_chat_head(request):
    try:
        chat_head_id = request.GET.get('chat_head_id')
        if not chat_head_id:
            return JsonResponse({"error": "chat_head_id is required"}, status=400)
        data = get_chat_head_service(chat_head_id)
        return JsonResponse(_stringify_objectids(data), status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)

@csrf_exempt
@require_http_methods(["DELETE"]) 
def delete_chat_head(request):
    try:
        payload = json.loads(request.body.decode('utf-8')) if request.body else {}
        chat_head_id = payload.get('chat_head_id') or request.GET.get('chat_head_id')
        if not chat_head_id:
            return JsonResponse({"error": "chat_head_id is required"}, status=400)
        data = delete_chat_head_service(chat_head_id)
        return JsonResponse(data, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=400)