# Generated by Django 3.0.8 on 2020-07-22 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bootcamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('name_ar', models.CharField(max_length=240)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('name', models.CharField(max_length=240)),
                ('name_ar', models.CharField(max_length=240)),
                ('bootcamp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cohorts', to='bootcamps.Bootcamp')),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('name_ar', models.CharField(max_length=240)),
                ('bio', models.CharField(max_length=240)),
                ('bio_ar', models.CharField(max_length=240)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('name_ar', models.CharField(max_length=240)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='bootcamps.Cohort')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='bootcamps.Instructor')),
                ('topics', models.ManyToManyField(to='bootcamps.Topic')),
            ],
        ),
        migrations.AddField(
            model_name='cohort',
            name='instructors',
            field=models.ManyToManyField(related_name='cohorts', through='bootcamps.Role', to='bootcamps.Instructor'),
        ),
    ]
