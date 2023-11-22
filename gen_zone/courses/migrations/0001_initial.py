# Generated by Django 4.2.7 on 2023-11-20 11:19

import courses.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('rating', models.IntegerField(default=0)),
                ('preview', models.ImageField(upload_to='courses/<django.db.models.fields.CharField>/preview/')),
                ('price', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson_num', models.IntegerField(unique=True)),
                ('lesson_title', models.CharField(max_length=255)),
                ('lesson_description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('step_num', models.IntegerField(unique=True)),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='steps', to='courses.lesson')),
            ],
            options={
                'unique_together': {('lesson', 'step_num')},
            },
        ),
        migrations.CreateModel(
            name='VideoContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_url', models.URLField()),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='video_contents', to='courses.step')),
            ],
        ),
        migrations.CreateModel(
            name='TextContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='text_contents', to='courses.step')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_num', models.IntegerField(unique=True)),
                ('module_title', models.CharField(max_length=255)),
                ('module_description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='courses.course')),
            ],
            options={
                'unique_together': {('course', 'module_num')},
            },
        ),
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.module'),
        ),
        migrations.CreateModel(
            name='ImageContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=courses.models.content_upload_path)),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_contents', to='courses.step')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='lesson',
            unique_together={('module', 'lesson_num')},
        ),
    ]