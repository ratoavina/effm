import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from effmapp.models.User import User


@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
    except Exception:
        return JsonResponse({"ok": False, "message": "JSON invalide"}, status=400)

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return JsonResponse(
            {"ok": False, "message": "name, email et password sont obligatoires"},
            status=400
        )

    if User.objects.filter(email=email).exists():
        return JsonResponse(
            {"ok": False, "message": "Cet email existe déjà"},
            status=409
        )

    user = User.objects.create_user(
        email=email,
        name=name,
        # ******
    )

    return JsonResponse(
        {
            "ok": True,
            "message": "Utilisateur créé",
            "data": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        },
        status=201
    )

@require_http_methods(["GET"])
def get_users(request):
    users = User.objects.all().values(
        "id", "name", "email", "prenom", "sexe", "phone",
        "adresse", "ville", "pays", "region", "profession",
        "is_active", "is_staff", "is_admin"
    )
    return JsonResponse({
        "ok": True,
        "count": len(users),
        "data": list(users)
    }, status=200)
