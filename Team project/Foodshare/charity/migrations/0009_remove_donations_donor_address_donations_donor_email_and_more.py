# Generated by Django 4.2.3 on 2023-07-25 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0008_alter_donations_donor_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donations',
            name='donor_address',
        ),
        migrations.AddField(
            model_name='donations',
            name='donor_email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='donations',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]