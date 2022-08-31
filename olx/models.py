from django.db import models




class Product(models.Model):
    TASHKENT_CITY = "Toshkent shahar"
    TASHKENT_REGION = "Toshkent viloyati"
    ANDIJAN = "Andijon viloyati"
    BUXORO = "Buxoro viloyati"
    FERGANA = "Farg'ona viloyati"
    JIZZAKH = 'Jizzax viloyati'
    KHOREZM = 'Xorazm viloyati'
    NAMANGAN = 'Namangan viloyati'
    NAVAI = 'Navoiy viloyati'
    KASHKADARYA = "Qashqadaryo viloyati"
    KARAKALPAKISTAN = "Qoraqalpogʻiston Respublikasi"
    SAMARKAND = "Samarqand viloyati"
    SIRDARYA = 'Sirdaryo viloyati'
    SURKHANDARYA = 'Surxandaryo viloyati'
    REGION_CHOICES = (
        ()
    )
    created_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    region = models.CharField(max_length=200, choices=REGION_CHOICES, null=True, blank=True)
    price = models.CharField(max_length=15)

    def __str__(self):
        return self.title