from django.db import models


class IslandPhoto(models.Model):
    image = models.ImageField()
    island = models.ForeignKey(
        "islands.Island", on_delete=models.CASCADE, related_name="photos"
    )

    def __str__(self):
        return f"Photo for {self.island.name}"


class Island(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
