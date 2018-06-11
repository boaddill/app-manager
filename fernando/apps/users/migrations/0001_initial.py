<<<<<<< HEAD
# Generated by Django 2.0.5 on 2018-05-31 18:18
=======
# Generated by Django 2.0.5 on 2018-05-31 18:53
>>>>>>> a0f9c3ab29d1283bd7a1af1a9b8d0fa19c3b3c91

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(help_text='Introduce a valid email please', max_length=254, unique=True, verbose_name='email address')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_client', models.BooleanField(default=False)),
                ('is_visitor', models.BooleanField(default=True)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_provider', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Users',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.CreateModel(
            name='Profile_Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, default='Introduce company name', max_length=30)),
                ('physical_address', models.CharField(blank=True, max_length=200)),
                ('postal_address', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(blank=True, max_length=30)),
                ('gst_registered', models.BooleanField(default=True)),
                ('company_director', models.CharField(blank=True, default='Introduce company director', max_length=30)),
                ('company_email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Client Profile',
                'verbose_name_plural': 'Client Profiles',
            },
        ),
        migrations.CreateModel(
            name='Profile_Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars/')),
                ('employee_name', models.CharField(blank=True, max_length=30)),
                ('employee_email', models.EmailField(blank=True, default='email', max_length=30, verbose_name='email')),
                ('position', models.CharField(blank=True, default='position', max_length=30)),
                ('hour_price_int', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('hour_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('postal_Code', models.CharField(blank=True, max_length=4)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Employee Profile',
                'verbose_name_plural': 'Employee Profiles',
            },
        ),
        migrations.CreateModel(
            name='Profile_Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(blank=True, default='Introduce company name', max_length=30)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=30)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('postal_Code', models.CharField(blank=True, max_length=4)),
                ('gst_registered', models.BooleanField(default=True)),
                ('company_director', models.CharField(blank=True, default='Introduce company director', max_length=30)),
                ('company_email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('contact_phone', models.CharField(blank=True, max_length=30)),
                ('contact_person1', models.CharField(blank=True, max_length=30)),
                ('contact_person2', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Email')),
            ],
            options={
                'verbose_name': 'Provider Profile',
                'verbose_name_plural': 'Provider Profiles',
            },
        ),
    ]
