# Generated by Django 4.2.16 on 2024-11-13 05:37

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание файла')),
                ('file', models.FileField(blank=True, null=True, upload_to='audios', verbose_name='Аудио файл')),
            ],
            managers=[
                ('obj_audio', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя автора', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Введите фамилию автора', max_length=100, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату рождения', null=True, verbose_name='Дата рождения')),
                ('about', models.TextField(help_text='Введите сведения об авторе', verbose_name='Сведения об авторе')),
                ('photo', models.ImageField(blank=True, help_text='Введите фото автора', null=True, upload_to='images', verbose_name='Фото автора')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=200, verbose_name='Название книги')),
                ('year', models.CharField(help_text='Введите год издания', max_length=4, verbose_name='Год издания')),
                ('summary', models.TextField(help_text='Введите краткое описание книги', max_length=1000, verbose_name='Аннотация книги')),
                ('isbn', models.CharField(help_text='Должно содержать 13 символов', max_length=13, verbose_name='ISBN книги')),
                ('price', models.DecimalField(decimal_places=2, help_text='Введите цену книги', max_digits=7, verbose_name='Цена (руб.)')),
                ('photo', models.ImageField(help_text='Введите изображение обложки', upload_to='images', verbose_name='Изображение обложки')),
                ('author', models.ManyToManyField(help_text='Выберите автора (авторов) книги', to='catalog.author', verbose_name='Автор (авторы) книги')),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание файла')),
                ('file', models.FileField(blank=True, null=True, upload_to='files', verbose_name='Файл PDF')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' Введите жанр книги', max_length=200, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание изображения')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='Файл с изображением')),
            ],
            managers=[
                ('obj_img', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' Введите язык книги', max_length=20, verbose_name='Язык книги')),
            ],
        ),
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field_name', models.CharField(help_text='Не более 20 символов', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя клиента')),
                ('age', models.IntegerField(verbose_name='Возраст клиента')),
            ],
            managers=[
                ('object_person', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text=' Введите наименование издательства', max_length=20, verbose_name='Издательство')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите статус экземпляра книги', max_length=20, verbose_name='Статус экземпляра книги')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='VideoFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Описание файла')),
                ('file', models.FileField(blank=True, null=True, upload_to='videos', verbose_name='Видео файл')),
            ],
            managers=[
                ('obj_video', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('login', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='catalog.user')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('courses', models.ManyToManyField(to='catalog.course')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.IntegerField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.company')),
            ],
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_nom', models.CharField(help_text='Введите инвентарный номер экземпляра', max_length=20, null=True, verbose_name='Инвентарный номер')),
                ('due_back', models.DateField(blank=True, help_text='Введите конец срока статуса', null=True, verbose_name='Дата окончания статуса')),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book')),
                ('status', models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Статус экземпляра книги')),
            ],
            options={
                'ordering': ['due_back'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text=' Выберите жанр для книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Жанр книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Выберите язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Язык книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(help_text='Выберите издательство', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.publisher', verbose_name='Издательство'),
        ),
    ]
