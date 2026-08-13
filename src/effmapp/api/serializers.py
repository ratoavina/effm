# /home/runner/work/effm/effm/src/effmapp/api/serializers.py
from rest_framework import serializers
from effmapp.models.User import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, required=True)

    class Meta:
        model = User
        fields = (
            "id", "name", "email", "password",
            "prenom", "sexe", "dtn", "phone", "adresse",
            "ville", "pays", "region", "profession", "date_embauche"
        )
        extra_kwargs = {
            "name": {"required": True},
            "email": {"required": True},
            "prenom": {"required": False, "allow_null": True, "allow_blank": True},
            "sexe": {"required": False, "allow_null": True, "allow_blank": True},
            "dtn": {"required": False, "allow_null": True},
            "phone": {"required": False, "allow_null": True},
            "adresse": {"required": False, "allow_null": True, "allow_blank": True},
            "ville": {"required": False, "allow_null": True, "allow_blank": True},
            "pays": {"required": False, "allow_blank": True},
            "region": {"required": False, "allow_null": True, "allow_blank": True},
            "profession": {"required": False, "allow_null": True, "allow_blank": True},
            "date_embauche": {"required": False, "allow_null": True},
        }

    def create(self, validated_data):
        # On extrait les champs obligatoires qui ont un traitement spécifique
        password = validated_data.pop("password")
        email = validated_data.pop("email")
        name = validated_data.pop("name")
        
        # On utilise le manager personnalisé pour créer l'utilisateur
        return User.objects.create_user(
            email=email,
            name=name,
            password=password,
            **validated_data    # Le reste des champs optionnels (prenom, sexe, etc.)
        )


class UserReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id", "name", "email", "prenom", "sexe", "phone", "adresse",
            "ville", "pays", "region", "profession", "is_active", "is_staff", "is_admin"
        )


class UserUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, min_length=8)

    class Meta:
        model = User
        fields = (
            "name", "email", "password", "prenom", "sexe", "phone",
            "adresse", "ville", "pays", "region", "profession", "is_active"
        )

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
