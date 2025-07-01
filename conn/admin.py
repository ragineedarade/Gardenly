from django.contrib import admin
from .models import savecontact  # Import your model
from .models import submitreview
admin.site.register(savecontact)  # Register the model
# Register your models here.
admin.site.register(submitreview)