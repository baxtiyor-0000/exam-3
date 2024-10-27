# Generated by Django 5.0.8 on 2024-08-11 18:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0007_category'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['-updated'],
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-updated']},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-updated']},
        ),
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['-uploaded_at']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated']},
        ),
        migrations.RemoveIndex(
            model_name='comment',
            name='exam_commen_created_b0350c_idx',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='user',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='posts', to='exam.category'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['-updated'], name='exam_catego_updated_f7c273_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-updated'], name='exam_commen_updated_15d784_idx'),
        ),
        migrations.AddIndex(
            model_name='comment',
            index=models.Index(fields=['-publish'], name='exam_commen_publish_d8ee3e_idx'),
        ),
        migrations.AddIndex(
            model_name='image',
            index=models.Index(fields=['-uploaded_at'], name='exam_image_uploade_9328fd_idx'),
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-updated'], name='exam_post_updated_37824e_idx'),
        ),
        migrations.AddIndex(
            model_name='about',
            index=models.Index(fields=['-updated'], name='exam_about_updated_c00241_idx'),
        ),
    ]
