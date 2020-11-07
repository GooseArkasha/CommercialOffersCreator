from django.db import models
from django.shortcuts import reverse

class PriceGroup(models.Model):
    denomination = models.CharField(max_length=150, db_index=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.denomination

    def get_absolut_url(self):
        return reverse('price_group_ditail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('price_group_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('price_group_delete_url', kwargs={'id': self.id})



class PriceGroupDiscount(models.Model):
    price_group = models.ForeignKey(PriceGroup, on_delete = models.CASCADE, blank=True)
    id = models.AutoField(primary_key=True)
    discount = models.DecimalField(decimal_places=3, max_digits=3)

    def __str__(self):
        return self.price_group.denomination + " " + str(self.discount)

    def get_absolut_url(self):
        return reverse('price_group_discount_ditail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('price_group_discount_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('price_group_discount_delete_url', kwargs={'id': self.id})



class Customer(models.Model):
    denomination = models.CharField(max_length=150, db_index=True)
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=150)
    index = models.CharField(max_length=6)
    telephone = models.CharField(max_length=11)
    contactPersonPhoneNumber = models.CharField(max_length=11, blank=True)
    contactPersonEmail = models.CharField(max_length=50, blank=True)
    price_group_discounts = models.ManyToManyField('PriceGroupDiscount', blank=True)


    def __str__(self):
        return self.denomination

    def get_absolut_url(self):
        return reverse('customer_ditail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('customer_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('customer_delete_url', kwargs={'id': self.id})



class Product(models.Model):
    denomination = models.CharField(max_length=150, db_index=True)
    id = models.AutoField(primary_key=True) #id==articul
    description = models.TextField(blank=True)
    box_quantity = models.IntegerField()    #количество в упаковке
    min_order_quantity = models.IntegerField()  #минимаьлное количество товара для заказа
    price_group = models.ForeignKey(PriceGroup, on_delete = models.CASCADE, blank=True)
    cost = models.DecimalField(decimal_places=2, max_digits=10) #Себестоимость
    list_price = models.DecimalField(decimal_places=2, max_digits=10) #Прейскурантная цена

    def __str__(self):
        return self.denomination

    def get_absolut_url(self):
        return reverse('product_ditail_url', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('product_update_url', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('product_delete_url', kwargs={'id': self.id})
