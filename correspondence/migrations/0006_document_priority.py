# Generated manually to add the "أهمية الخطاب" (priority) field

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correspondence', '0005_document_is_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='priority',
            field=models.CharField(
                choices=[
                    ('normal', 'عادي'),
                    ('important', 'هام'),
                    ('urgent', 'عاجل'),
                    ('very_urgent', 'عاجل جداً'),
                ],
                default='normal',
                max_length=20,
                verbose_name='أهمية الخطاب',
            ),
        ),
    ]
