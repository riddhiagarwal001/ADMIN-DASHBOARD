from django.db import models


# Vendor
class Vendor(models.Model):
    full_name=models.CharField(max_length=50)
    address=models.TextField()
    mobile=models.CharField(max_length=15)
    status=models.BooleanField()


#meta class used for removing or adding 's' in model names
    class Meta:
        verbose_name_plural='1.Vendors'

    def __str__(self):
        return self. full_name


# Unit
class Unit(models.Model):
    title=models.CharField(max_length=50)
    short_name=models.CharField(max_length=50)

    class Meta:
        verbose_name_plural='2.Units'
    

    def __str__(self):
        return self. title

# Product
class Product(models.Model):
    title=models.CharField(max_length=50)
    detail=models.TextField()
    unit=models.ForeignKey(Unit, on_delete=models.CASCADE)
    

    class Meta:
        verbose_name_plural='3.Products'

    def __str__(self):
        return self. title       

# Purchase=Inwarding=Recieving
class Inwarding(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    vendor=models.ForeignKey(Vendor,on_delete=models.CASCADE)
    quantity=models.FloatField()
    price=models.FloatField()
    total_amount=models.FloatField(editable=False,default=0)
    recieved_date=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural='4. Inwardings'

    def save(self,*args,**kwargs):
        self.total_amount=self.quantity*self.price
        super(Inwarding,self).save(*args,**kwargs)
        #inventory effect (we make inventory management code)
        inventory=Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            totalBal=inventory.total_balance_qty+self.quantity
        else:
            totalBal=self.quantity

        Inventory.objects.create(
            product=self.product,
            recieving=self,
            issue=None,
            recieved_quantity=self.quantity,
            issued_quantity=None,
            total_balance_qty=totalBal
            
            

            

          

           
         
         )    
# Sale=Issue=Distribution
class Distribution(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.FloatField()
    price=models.FloatField()
    total_amount=models.FloatField(editable=False)
    issued_date=models.DateTimeField(auto_now_add=True)

    shop_name=models.CharField(max_length=50,blank=False)
    shop_mobile_number=models.CharField(max_length=50)
    shop_address=models.TextField()

    class Meta:
        verbose_name_plural='5.Distribution'

    def save(self,*args,**kwargs):
        self.total_amount=self.quantity*self.price
        super(Distribution,self).save(*args,**kwargs)

        #inventory effect (we make inventory management code)
        inventory=Inventory.objects.filter(product=self.product).order_by('-id').first()
        if inventory:
            totalBal=inventory.total_balance_qty-self.quantity

        

        Inventory.objects.create(
            product=self.product,
            recieving=None,
            issue=self,
            recieved_quantity=None,
            issued_quantity=self.quantity,
            total_balance_qty=totalBal
            
            

            

          

           
         
         )    

      
 
            

#Inventory
class Inventory(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    recieving=models.ForeignKey(Inwarding,on_delete=models.CASCADE,default=0,null=True)
    issue=models.ForeignKey(Distribution,on_delete=models.CASCADE,default=0,null=True)
    recieved_quantity=models.FloatField(default=0,null=True)
    issued_quantity=models.FloatField(default=0,null=True)
    total_balance_qty=models.FloatField()
   


    

    class Meta:
        verbose_name_plural='6.Inventory'

    def product_unit(self):
            return self.product.unit.title

    
    def recieved_date(self):
        if self.recieving:
            return self.recieving.recieved_date

    def issued_date(self):
        if self.issue:
            return self.issue.issued_date



        

