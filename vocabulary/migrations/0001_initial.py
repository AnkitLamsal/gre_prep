# Generated by Django 2.1.15 on 2024-05-23 03:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('meaning', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('connotation', models.CharField(choices=[('positive', 'Positive'), ('negative', 'Negative'), ('neutral', 'Neutral')], max_length=100)),
                ('definition', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='WordFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabulary.Family')),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vocabulary.Word')),
            ],
        ),
    ]