from django.db import models

# Create your models here.
class User(models.Model):
    UserId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=200)
    LastName = models.CharField(max_length=200)
    Email = models.CharField(max_length=200)
    Password = models.CharField(max_length=200)
    Currency = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Users"

    def __str__(self):
        return ( str(self.UserId) + "=>" +self.FirstName + self.LastName)


class Category(models.Model):
    CategoryId = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    CategoryName = models.CharField(max_length=200)
    Level = models.IntegerField()

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        txt = "N/A"
        if self.Level == 1:
            txt = "Assets"
        elif self.Level == 2:
            txt = "Bills"
        return (str(self.CategoryId) + "=> UserId :"+ str(self.UserId) + " , Type:" + txt + ", CategoryName:"+ self.CategoryName)




class Account(models.Model):
    AccountId = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    AccountName = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Accounts"

    def __str__(self):
        return (str(self.AccountId) + "=> UserId :"+ str(self.UserId) + ", AccountName:" + self.AccountName)



class Budget(models.Model):
    BudgetId = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    CategoryId = models.IntegerField()
    Dates = models.DateField(auto_now=True)
    Amount = models.IntegerField()

    class Meta:
        verbose_name_plural = "Budgets"

    def __str__(self):
        return (str(self.BudgetId) + "=> UserId :"+ str(self.UserId) + ", CategoryId:" + str(self.CategoryId) + ", Amount:" + str(self.Amount))


class Total(models.Model):
    TotalId = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    AccountId = models.IntegerField()
    Dates = models.DateField(auto_now=True)
    Totals = models.IntegerField()

    class Meta:
        verbose_name_plural = "Totals"

    def __str__(self):
        return (str(self.TotalId) + "=> UserId :" + str(self.UserId) + ", AccountId:" + str(self.AccountId) + ", Total :"+ str(self.Totals))


class Bill(models.Model):
    Id = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    Title = models.CharField(max_length=200)
    Dates = models.DateField(auto_now=True)
    CategoryId = models.IntegerField()
    AccountId = models.IntegerField()
    Amount = models.IntegerField()
    Description = models.TextField()

    class Meta:
        verbose_name_plural = "Bills"

    def __str__(self):
        return (str(self.Id) + "=> UserId :" + str(self.UserId) + ", AccountId:" + str(self.AccountId) + ", Amount :"+ str(self.Amount) + ", Title:"+self.Title)


class Asset(models.Model):
    Id = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    Title = models.CharField(max_length=200)
    Dates = models.DateField(auto_now=True)
    CategoryId = models.IntegerField()
    AccountId = models.IntegerField()
    Amount = models.IntegerField()
    Description = models.TextField()

    class Meta:
        verbose_name_plural = "Assets"

    def __str__(self):
        return (str(self.Id) + "=> UserId :" + str(self.UserId) + ", AccountId:" + str(self.AccountId) + ", Amount :"+ str(self.Amount) + ", Title:"+self.Title)


