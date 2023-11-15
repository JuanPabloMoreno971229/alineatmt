# Generated by Django 4.2.6 on 2023-11-10 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_logos_project_remove_how_name_remove_what_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='project_images/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='logos',
            options={'ordering': ['created'], 'verbose_name': 'Logo', 'verbose_name_plural': 'Logo'},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-created'], 'verbose_name': 'Proyecto', 'verbose_name_plural': 'Proyectos'},
        ),
        migrations.AlterModelOptions(
            name='what',
            options={'ordering': ['created'], 'verbose_name': 'Que es', 'verbose_name_plural': 'Que es'},
        ),
        migrations.RemoveField(
            model_name='project',
            name='image',
        ),
        migrations.AlterField(
            model_name='how',
            name='text',
            field=models.TextField(blank=True, max_length=200, verbose_name='Información'),
        ),
        migrations.AddField(
            model_name='project',
            name='images',
            field=models.ManyToManyField(to='core.image', verbose_name='Imágenes'),
        ),
    ]