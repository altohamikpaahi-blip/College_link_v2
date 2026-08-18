from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),  # ربطه بالترحيل الأول التابع لـ users
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='colleges/logos/', verbose_name='شعار الكلية'),
        ),
    ]
