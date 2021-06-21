from django.db import models
from django.core.validators import MinValueValidator

class Predictions(models.Model):
    locations = models.CharField(max_length=30)
    sqft = models.PositiveIntegerField(validators=[MinValueValidator(250)])
    bhk = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    bath = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    predicted_price = models.DecimalField(default=0.0,max_digits=5,decimal_places=2)

