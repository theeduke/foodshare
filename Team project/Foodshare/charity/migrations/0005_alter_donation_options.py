# Generated by Django 4.2.3 on 2023-07-19 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0004_alter_donation_donor_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'ordering': ['-created_at']},
        ),
    ]
