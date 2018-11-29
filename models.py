from django.db import models


class State(models.Model):
    Id = models.IntegerField(primary_key=True)
    state = models.CharField(max_length=20)


class City(models.Model):
    Id = models.IntegerField(primary_key=True)
    state_name = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.CharField(max_length=10)


class Customer(models.Model):
    Name = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    Email_id = models.EmailField(primary_key=True)
    contact_number = models.IntegerField()
    password = models.CharField(max_length=10)


class Investor(models.Model):
    Name = models.CharField(max_length=20)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    Email_id = models.EmailField(primary_key=True)
    contact_number = models.IntegerField()
    password = models.CharField(max_length=20)


class Agent(models.Model):
    Emp_id = models.IntegerField()
    Name = models.CharField(max_length=20)
    contact_number = models.IntegerField()
    Email_id = models.EmailField(primary_key=True)
    password = models.CharField(max_length=20)


class Loan_Scheme(models.Model):
    Id = models.IntegerField(primary_key=True)
    Scheme_Name = models.CharField(max_length=15)
    Loan_amt = models.DecimalField(max_digits=8, decimal_places=2)
    Loan_Tenure = models.IntegerField()
    Rate_of_Intrest = models.IntegerField()
    Total_amt = models.DecimalField(max_digits=8, decimal_places=2)


class Investment_scheme(models.Model):
    Id = models.IntegerField(primary_key=True)
    Scheme_Name = models.CharField(max_length=15)
    Investment_amt = models.DecimalField(max_digits=8, decimal_places=2)
    Investment_Tenure = models.IntegerField()
    Returns = models.DecimalField(max_digits=8, decimal_places=2)


class Suggetion(models.Model):
    Title = models.CharField(max_length=20)
    Subject = models.CharField(max_length=50)
    Message = models.CharField(max_length=250)
