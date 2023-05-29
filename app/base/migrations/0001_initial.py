# Generated by Django 4.2 on 2023-05-29 10:49

import app.base.forms.fields
import datetime
from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', app.base.forms.fields.CurrencyField(decimal_places=2, default=Decimal('0'), max_digits=10, verbose_name='Guthaben')),
                ('locked', models.BooleanField(default=False, verbose_name='Gesperrt')),
            ],
            options={
                'verbose_name': 'Konto',
                'verbose_name_plural': 'Konten',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('begin_time', app.base.forms.fields.DateTimeField(default=datetime.datetime.now, verbose_name='Beginn')),
                ('end_time', app.base.forms.fields.DateTimeField(blank=True, null=True, verbose_name='Ende')),
                ('comment', app.base.forms.fields.TextField(blank=True, verbose_name='Kommentar')),
            ],
            options={
                'verbose_name': 'Buchung',
                'verbose_name_plural': 'Buchungen',
            },
        ),
        migrations.CreateModel(
            name='BookingType',
            fields=[
                ('key', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='UUID')),
                ('label', models.CharField(max_length=200, verbose_name='Bezeichnung')),
                ('price', app.base.forms.fields.CurrencyField(decimal_places=2, default=Decimal('0'), max_digits=10, verbose_name='Preis (€)')),
                ('interval', models.IntegerField(default=60, verbose_name='Intervall (Min)')),
                ('is_checkin', models.BooleanField(default=False, verbose_name='Ist Eincheck-Option')),
            ],
            options={
                'verbose_name': 'Buchungsart',
                'verbose_name_plural': 'Buchungsarten',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=280, verbose_name='Titel')),
                ('mandatory', models.BooleanField(default=False, verbose_name='Braucht jeder?')),
                ('description', app.base.forms.fields.TextField(blank=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Einweisung',
                'verbose_name_plural': 'Einweisungen',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.CharField(blank=True, max_length=200, verbose_name='Karten-ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='Vorname')),
                ('last_name', models.CharField(max_length=200, verbose_name='Nachname')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Telefon')),
                ('birth_date', app.base.forms.fields.DateField(verbose_name='Geburtsdatum')),
                ('zip_code', models.CharField(max_length=10, verbose_name='PLZ')),
                ('city', models.CharField(max_length=200, verbose_name='Stadt')),
                ('street', models.CharField(max_length=200, verbose_name='Straße')),
                ('house_nr', models.CharField(max_length=10, verbose_name='Hausnummer')),
                ('identified', models.BooleanField(default=False, verbose_name='Ausweis vorgezeigt')),
                ('agreed_to_terms_of_service', models.BooleanField(default=False, verbose_name='Nutzungsbedingungen zugestimmt')),
            ],
            options={
                'verbose_name': 'Werkstattnutzer:in',
                'verbose_name_plural': 'Werkstattnutzer:innen',
            },
        ),
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('key', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='UUID')),
                ('label', models.CharField(max_length=200, verbose_name='Label')),
                ('description', app.base.forms.fields.TextField(blank=True, verbose_name='Beschreibung')),
            ],
            options={
                'verbose_name': 'Attribut',
                'verbose_name_plural': 'Attribute',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', app.base.forms.fields.CurrencyField(decimal_places=2, default=Decimal('0'), max_digits=10, verbose_name='Betrag')),
                ('description', models.CharField(max_length=500, verbose_name='Beschreibung')),
                ('time_stamp', app.base.forms.fields.DateTimeField(auto_now_add=True, verbose_name='Datum / Uhrzeit')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.account', verbose_name='Konto')),
                ('booking', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.booking', verbose_name='Zugehörige Zeitbuchung')),
            ],
            options={
                'verbose_name': 'Transaktion',
                'verbose_name_plural': 'Transaktionen',
            },
        ),
        migrations.CreateModel(
            name='TraitMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', app.base.forms.fields.DateField(default=datetime.date.today, verbose_name='Gültig von')),
                ('valid_until', app.base.forms.fields.DateField(blank=True, null=True, verbose_name='Gültig bis')),
                ('trait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.trait', verbose_name='Attribut')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='traits', to='base.person', verbose_name='Werkstattnutzer:in')),
            ],
            options={
                'verbose_name': 'Attributzuweisung',
                'verbose_name_plural': 'Attributzuweisungen',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', app.base.forms.fields.TextField(blank=True, verbose_name='Notiz')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.person')),
            ],
            options={
                'verbose_name': 'Notiz',
                'verbose_name_plural': 'Notizen',
            },
        ),
        migrations.CreateModel(
            name='CourseVisit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', app.base.forms.fields.DateField(default=datetime.date.today, verbose_name='Datum')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='base.course', verbose_name='Einweisung')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='base.person', verbose_name='Wer wurde eingewiesen?')),
                ('teacher', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='instructed', to='base.person', verbose_name='Durchgeführt von')),
            ],
            options={
                'verbose_name': 'Teilnahme',
                'verbose_name_plural': 'Teilnahmen',
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base.bookingtype', verbose_name='Art'),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.person', verbose_name='Nutzer:in'),
        ),
        migrations.AddField(
            model_name='account',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.person'),
        ),
    ]
