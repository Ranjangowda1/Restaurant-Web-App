from django.db import models


class ItemList(models.Model):
    Item_Name = models.CharField(max_length=15)

    def __str__(self):
        return self.Item_Name

class Items(models.Model):
    Product = models.CharField(max_length=15)
    Description = models.TextField()
    Price = models.IntegerField()
    Category = models.ForeignKey(ItemList, on_delete=models.CASCADE, related_name='Name')
    Image = models.ImageField(upload_to='Items/')

    def __str__(self):
        return self.Product

class AboutUs(models.Model):
    # Image = models.ImageField(upload_to='About/')
    Description = models.TextField()

class Feedback(models.Model):
    Name = models.CharField(max_length=15)
    Description = models.TextField()
    Rating = models.DecimalField(max_digits=5,decimal_places=1)
    Image = models.ImageField(upload_to='Items/',blank=True)

    def __str__(self):
        return self.Name
    
class BookTable(models.Model):
    Name = models.CharField(max_length=15)
    Phone_number = models.IntegerField()
    Email = models.EmailField()
    Total_persons = models.IntegerField() 
    Booking_Date = models.DateField()

    def __str__(self):
        return self.Name