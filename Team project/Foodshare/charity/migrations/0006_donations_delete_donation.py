# Generated by Django 4.2.3 on 2023-07-19 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0005_alter_donation_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('donor_name', models.CharField(max_length=255)),
                ('donor_address', models.CharField(max_length=255)),
                ('donor_mobile', models.IntegerField()),
                ('Donation_type', models.CharField(max_length=255)),
                ('request', models.TextField(blank=True)),
                ('accepted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(related_name='item', to='charity.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='Donation',
        ),
    ]
