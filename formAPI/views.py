from django.shortcuts import render
from .models import WheelSpecification
from .serializers import WheelSpecificationSerialer
from rest_framework.generics import CreateAPIView, ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from django.db import IntegrityError
from rest_framework.response import Response


# Create your views here.
class AddDetials(CreateAPIView):
    queryset=WheelSpecification.objects.all()
    serializer_class=WheelSpecificationSerialer
    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"success": False, "message": "Duplicate form number not allowed."},
                status=status.HTTP_400_BAD_REQUEST
            )

class DisplayDetials(ListAPIView):
    queryset=WheelSpecification.objects.all()
    serializer_class=WheelSpecificationSerialer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['form_number', 'submitted_by', 'submitted_date']