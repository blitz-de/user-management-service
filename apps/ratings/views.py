from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from apps.profiles.models import Profile

from .models import Rating

User = get_user_model()


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def create_opponent_review(request, profile_id):
    opponent_profile = Profile.objects.get(id=profile_id, is_opponent=True)
    data = request.data

    profile_user = User.objects.get(pkid=opponent_profile.user.pkid)
    if profile_user.email == request.user.email:
        formatted_response = {"message": "You can't rate yourself"}
        return Response(formatted_response, status=status.HTTP_403_FORBIDDEN)

    #opponent_profile.opponent_review.filter(opponent__username=opponent.username).exists
    # check if the review id is already assigned the profiles username. Each user can review one user
    alreadyExists = opponent_profile.opponent_review.filter(
        opponent__pkid=profile_user.pkid
    ).exists()

    if alreadyExists:
        formatted_response = {"detail": "Profile already reviewed"}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

    elif data["rating"] == 0:
        formatted_response = {"detail": "Please select a rating"}
        return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

    else:
        review = Rating.objects.create(
            rater=request.user,
            opponent=opponent_profile,
            rating=data["rating"],
            comment=data["comment"],
        )
        reviews = opponent_profile.opponent_review.all()
        opponent_profile.num_reviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        opponent_profile.rating = round(total / len(reviews), 2)
        opponent_profile.save()
        return Response("Review Added")
