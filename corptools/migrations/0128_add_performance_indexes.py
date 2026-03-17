from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corptools', '0127_alter_corporationaudit_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characteraudit',
            name='last_update_pub_data',
            field=models.DateTimeField(blank=True, db_index=True, default=None, null=True),
        ),
        migrations.AddIndex(
            model_name='characteraudit',
            index=models.Index(fields=['active'], name='corptools_c_active_idx'),
        ),
        migrations.AddIndex(
            model_name='characteraudit',
            index=models.Index(fields=['active', 'last_update_pub_data'], name='corptools_c_active_pub_idx'),
        ),
    ]
