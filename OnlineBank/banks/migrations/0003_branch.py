# Generated by Django 3.0.7 on 2021-07-18 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('banks', '0002_auto_20210718_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branchName', models.CharField(blank=True, max_length=255, null=True, verbose_name='Branch name')),
                ('branchCode', models.CharField(blank=True, max_length=255, null=True, verbose_name='Branch code')),
                ('bankid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.Bank')),
            ],
            options={
                'db_table': 'branches',
            },
        ),
    ]