# Generated by Django 5.1.6 on 2025-02-19 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ilmiy daraja nomi')),
            ],
            options={
                'verbose_name': 'Ilmiy daraja',
                'verbose_name_plural': 'Ilmiy darajalar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AcademicSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ilmiy yo‘nalish nomi')),
            ],
            options={
                'verbose_name': 'Ilmiy yo‘nalish',
                'verbose_name_plural': 'Ilmiy yo‘nalishlar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='AcademicTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ilmiy unvon nomi')),
            ],
            options={
                'verbose_name': 'Ilmiy unvon',
                'verbose_name_plural': 'Ilmiy unvonlar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Tuman nomi')),
            ],
            options={
                'verbose_name': 'Tuman',
                'verbose_name_plural': 'Tumanlar',
                'ordering': ['region', 'name'],
            },
        ),
        migrations.CreateModel(
            name='EducationLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Ta’lim darajasi')),
            ],
            options={
                'verbose_name': 'Ta’lim darajasi',
                'verbose_name_plural': 'Ta’lim darajalari',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='LanguageProficiency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_name', models.CharField(max_length=255, verbose_name='Til nomi')),
                ('proficiency_level', models.CharField(choices=[('A1', 'A1 - Boshlang‘ich'), ('A2', 'A2 - Boshlang‘ich+'), ('B1', 'B1 - O‘rta'), ('B2', 'B2 - O‘rta+'), ('C1', 'C1 - Yuqori'), ('C2', 'C2 - Mukammal')], max_length=2, verbose_name='Bilish darajasi')),
            ],
            options={
                'verbose_name': 'Til bilish darajasi',
                'verbose_name_plural': 'Til bilish darajalari',
                'ordering': ['language_name', 'proficiency_level'],
            },
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Millat nomi')),
            ],
            options={
                'verbose_name': 'Millat',
                'verbose_name_plural': 'Millatlar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Viloyat nomi')),
            ],
            options={
                'verbose_name': 'Viloyat',
                'verbose_name_plural': 'Viloyatlar',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='StateAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Mukofot nomi')),
                ('year', models.IntegerField(verbose_name='Berilgan yili')),
            ],
            options={
                'verbose_name': 'Davlat mukofoti',
                'verbose_name_plural': 'Davlat mukofotlari',
                'ordering': ['-year', 'name'],
            },
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(max_length=255, verbose_name='Ish joyi')),
                ('position', models.CharField(max_length=255, verbose_name='Lavozimi')),
                ('start_date', models.DateField(verbose_name='Ishga kirgan sanasi')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Ishdan ketgan sanasi')),
            ],
            options={
                'verbose_name': 'Ish tajribasi',
                'verbose_name_plural': 'Ish tajribalari',
                'ordering': ['-start_date'],
            },
        ),
    ]
