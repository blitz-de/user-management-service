from django_countries.serializer_fields import CountryField
from rest_framework import fields, serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    profile_photo = serializers.SerializerMethodField()
    username = serializers.CharField(source="user.username")
    # first_name = serializers.CharField(source="user.first_name")
    # last_name = serializers.CharField(source="user.last_name")
    is_active = serializers.CharField(source="user.is_active")
    email = serializers.EmailField(source="user.email")
    full_name = serializers.SerializerMethodField(read_only=True)
    # first_name = serializers.SerializerMethodField(read_only=True)
    # last_name = serializers.SerializerMethodField(read_only=True)
    country = CountryField(name_only=True)
    # reviews = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model = Profile
        fields = [
            'pkid',
            "username",
            # "first_name",
            # "last_name",
            "full_name",
            'is_active',
            "email",
            # "id",
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            "age",
            "country",
            "city",
            "region",
            "zip_code",
            "game_type",
            "skill_level",
            "rating",
            "num_reviews",
        ]

    def get_full_name(self, obj):
        first_name = obj.user.first_name.title()
        last_name = obj.user.last_name.title()
        return f"{first_name} {last_name}"

    # def get_reviews(self, obj):
    #     # opponent_review: in ratings.models, related_name
    #     reviews = obj.opponent_review.all()
    #     serializer = RatingSerializer(reviews, many=True)
    #     return serializer.data

    def get_profile_photo(self, obj):
        return obj.profile_photo.url


    # because i am reviewing the opponent
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(instance.id)
        if instance.is_opponent:
            representation["is_opponent"] = True
        return representation


class UpdateProfileSerializer(serializers.ModelSerializer):
    country = CountryField(name_only=True, required=False)
    zip_code = serializers.CharField(required=False)
    profile_photo = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = [
            "phone_number",
            "profile_photo",
            "about_me",
            "gender",
            "country",
            "city",
            "region",
            "zip_code",
            "game_type",
            "skill_level",
            "is_opponent",
            # maybe: is_opponent (Gesucht), is_looking (sucher)
        ]

    #validate
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_opponent:
            representation["is_opponent"] = True
        return representation

    def get_profile_photo(self, obj):
        return obj.profile_photo.url

