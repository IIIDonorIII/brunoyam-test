from django.db import models
from django.contrib.auth.models import User


class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class HouseVisit(models.Model):  # Убедитесь, что у вас есть этот класс
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)
    house_address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.username} - {self.house_address}"
