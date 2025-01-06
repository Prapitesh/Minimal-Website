from django.contrib import admin

# Register your models here.
from .models import Post
admin.site.register(Post)
# Patient.objects.create(
#     name="Test Patient",
#     age=30,
#     gender="Male",
#     contact_number="1234567890",
#     aadhar_or_kyc="1234-5678-9012",
#     medical_concern="Test Concern",
#     treatment_advice="Test Advice"
# )
