from django.db import models


class UserActivity(models.Model):
    user_id = models.IntegerField()
    date = models.DateField()
    used = models.BooleanField()

    def __str__(self):
        return f'{self.user_id} - {self.date}'
