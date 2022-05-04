# Generated by Django 4.0.4 on 2022-05-04 06:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('username', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=15)),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='category', max_length=30)),
                ('bill_name', models.CharField(default='bill name', max_length=30)),
                ('amount_paid', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.users')),
            ],
        ),
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('transaction', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.transaction')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.users')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income_name', models.CharField(blank=True, max_length=20)),
                ('deposit', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('current_user', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='dashboard.users')),
            ],
        ),
        migrations.CreateModel(
            name='Goals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_name', models.CharField(default='goal_name', max_length=30)),
                ('amount_to_save', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('amount_saved', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.users')),
            ],
        ),
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='Category', max_length=30)),
                ('amount_saved', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('budget_goal', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.users')),
            ],
        ),
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='category', max_length=30)),
                ('bill_name', models.CharField(default='bill name', max_length=30)),
                ('amount_due', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('isPaid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.users')),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('difference', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('date_bal', models.DateTimeField(auto_now=True, verbose_name='balance_date')),
                ('income', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.income')),
                ('transaction', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='dashboard.transaction')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='dashboard.users')),
            ],
        ),
    ]
