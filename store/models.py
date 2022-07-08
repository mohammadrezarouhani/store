from django.db import models

class Customer(models.Model):
    BRONZE_MEMBER_SHIP='B'
    SILVER_MEMBER_SHIP='S'
    GOLD_MEMEBR_SHIP='G'

    MEMBER_SHIP=(
        (BRONZE_MEMBER_SHIP,'BRONZE'),
        (SILVER_MEMBER_SHIP,'SILVER'),
        (GOLD_MEMEBR_SHIP,'GOLD')
    )

    first_name=models.CharField(55)
    last_name=models.CharField(55)
    email=models.EmailField()
    phone=models.CharField(max_length=25)
    birth_date=models.DateField()
    memeber_ship=models.CharField(max_length=15,choices=MEMBER_SHIP,default=BRONZE_MEMBER_SHIP)


class Product(models.Model):
    name=models.CharField(max_length=155)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    inventory=models.PositiveSmallIntegerField()
    date_added=models.DateField(auto_now=True)
    discription=models.TextField()


class Cart(models.Model):
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)


class CartItem(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    item=models.ForeignKey(Product,on_delete=models.SET_NULL)
    date_added=models.DateField(auto_now=True)