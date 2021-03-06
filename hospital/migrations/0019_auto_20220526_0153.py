from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='department',
            field=models.CharField(choices=[('Терапевт', 'Терапевт'), ('Невропатолог', 'Невропатолог'), ('Детский Невропатолог', 'Детский Невропатолог'), ('Кардиолог', 'Кардиолог'), ('Гинеколог', 'Гинеколог'), ('Пульманолог', 'Пульманолог'), ('Уролог', 'Уролог'), ('Педиатр', 'Педиатр'), ('Нефролог', 'Нефролог'), ('Дерматолог-Косметолог', 'Дерматолог-Косметолог'), ('ЭКГ, УЗИ', 'ЭКГ, УЗИ'), ('Физиотерапия', 'Физиотерапия'), ('Иглоукалывание', 'Иглоукалывание'), ('Фитобочка', 'Фитобочка')], default='Cardiologist', max_length=50),
        ),
    ]
