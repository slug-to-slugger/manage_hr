# Generated by Django 2.1.5 on 2019-02-03 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BelongSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=256)),
                ('department', models.CharField(max_length=256)),
                ('concentration', models.CharField(max_length=256)),
                ('art_or_science', models.BooleanField(null=True)),
                ('deviation', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DesiredSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_hr_app.BelongSchool')),
            ],
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name="student's first name")),
                ('last_name', models.CharField(max_length=256, verbose_name="student's last name")),
                ('email', models.EmailField(max_length=256, unique=True, verbose_name='email address')),
                ('phone', models.SmallIntegerField(unique=True)),
                ('password', models.CharField(max_length=512, verbose_name='password')),
                ('school_id', models.PositiveSmallIntegerField()),
                ('grade', models.PositiveSmallIntegerField(unique=True)),
                ('age', models.PositiveSmallIntegerField()),
                ('bday', models.DateField(null=True)),
                ('chara', models.TextField(null=True)),
                ('flag', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_friend', to='manage_hr_app.Student'),
        ),
        migrations.AddField(
            model_name='friend',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='friend_student', to='manage_hr_app.Student'),
        ),
        migrations.AddField(
            model_name='desiredschool',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manage_hr_app.Student'),
        ),
    ]
