# Generated by Django 2.1a1 on 2018-06-16 14:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=100)),
                ('nazwisko', models.CharField(max_length=200)),
                ('data_urodzenia', models.DateField(blank=True, null=True)),
                ('data_smierci', models.DateField(blank=True, null=True, verbose_name='Zmarl')),
            ],
            options={
                'ordering': ['nazwisko', 'imie'],
            },
        ),
        migrations.CreateModel(
            name='Gatunek',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(help_text='Gatunek, kategoria', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InstancjaKsiazki',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='ID', primary_key=True, serialize=False)),
                ('wydawca', models.CharField(max_length=200)),
                ('data_zwrotu', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('n', 'Naprawa'), ('w', 'Wypozyczona'), ('d', 'Dostepna'), ('z', 'Zarezerwowana')], default='n', help_text='Dostepnosc', max_length=1)),
            ],
            options={
                'ordering': ['data_zwrotu'],
            },
        ),
        migrations.CreateModel(
            name='Ksiazka',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tytul', models.CharField(max_length=200)),
                ('opis', models.TextField(help_text='opis', max_length=1000)),
                ('isbn', models.CharField(help_text='ISBN', max_length=13, verbose_name='ISBN')),
                ('autor', models.ForeignKey(help_text='Autor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.Autor')),
                ('gatunek', models.ManyToManyField(help_text='gatunek', to='katalog.Gatunek')),
            ],
        ),
        migrations.AddField(
            model_name='instancjaksiazki',
            name='ksiazka',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='katalog.Ksiazka'),
        ),
    ]