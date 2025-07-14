from .models import WheelSpecification
from rest_framework import serializers

class WheelSpecificationSerialer(serializers.ModelSerializer):
    form_number=serializers.CharField(
        required=True,
        error_messages={
            "required":"Form number is required.",
            "blank": "Form number is required.",
            "unique": "This form number already exists. Please use a different one."
        }
    )

    submitted_by=serializers.CharField(
        required=True,
        error_messages={
            "required":"User ID is required.",
            "blank": "User ID is required."
        }
    )

    submitted_date=serializers.DateField(
        required=True,
        error_messages={
            "invalid": "Date must be in the format YYYY-MM_DD.",
            "required":"Date is required."
            
        }
    )
    condemning_dia=serializers.CharField(
        required=True,
        error_messages={
            "required":"Condemning Dia is required.",
            "blank": "Condemning Dia is required."
            
        }
    )

    last_shop_issue_size=serializers.CharField(
        required=True,
        error_messages={
            "required":"Last shop size is required.",
            "blank": "Last shop size is required."
            
        }
    )
    tread_diameter_new=serializers.CharField(
        required=True,
        error_messages={
            "required":"New Tread Diameter is required.",
            "blank": "New Tread Diameter is required."
            
        }
    )
    wheel_gauge=serializers.CharField(
        required=True,
        error_messages={
            "required":"Wheel Gauge is required.",
            "blank": "Wheel Gauge is required."
            
        }
    )

    class Meta:
        model=WheelSpecification
        fields="__all__"

       