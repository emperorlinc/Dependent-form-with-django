from django.db import models

class Country(models.Model):
    country = models.CharField(max_length=45)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.country

class City(models.Model):
    city = models.CharField(max_length=45)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city


class Person(models.Model):
    name = models.CharField(max_length=25)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
