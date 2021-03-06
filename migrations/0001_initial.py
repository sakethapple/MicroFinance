# Generated by Django 2.1.3 on 2018-11-28 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('Emp_id', models.IntegerField()),
                ('Name', models.CharField(max_length=20)),
                ('contact_number', models.IntegerField()),
                ('Email_id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Email_id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contact_number', models.IntegerField()),
                ('password', models.CharField(max_length=10)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Microfinance.City')),
            ],
        ),
        migrations.CreateModel(
            name='Investment_scheme',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Scheme_Name', models.CharField(max_length=15)),
                ('Investment_amt', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Investment_Tenure', models.IntegerField()),
                ('Returns', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('Name', models.CharField(max_length=20)),
                ('Email_id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('contact_number', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Microfinance.City')),
            ],
        ),
        migrations.CreateModel(
            name='Loan_Scheme',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('Scheme_Name', models.CharField(max_length=15)),
                ('Loan_amt', models.DecimalField(decimal_places=2, max_digits=8)),
                ('Loan_Tenure', models.IntegerField()),
                ('Rate_of_Intrest', models.IntegerField()),
                ('Total_amt', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Suggetion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=20)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Microfinance.State'),
        ),
    ]
