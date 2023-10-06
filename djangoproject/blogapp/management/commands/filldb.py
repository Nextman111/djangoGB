from django.core.management.base import BaseCommand

from django.utils import timezone

from blogapp.models import Author, Article


class Command(BaseCommand):
    help = "Комана заполнит базу данных авторами и статьями, введите количество"

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Count')

    def handle(self, *args, **kwargs):
        count = kwargs['count']

        for i in range(1, count+1):
            author = Author(
                name=f"AuthorName{i}",
                surname=f"AuthorSurname{i}",
                email=f'author{i}@mail.ru',
                biography=f"Author{i} biography",
                birthday=timezone.now(),
            )

            author.save()
            self.stdout.write(f"Добавлен новый автор {author.name}")

            for j in range(1, count + 1):
                article = Article(
                    author=author,
                    title=f"Article{j}",
                    content=f"ArticleContent{j}",
                    category=f"Cat{j}",
                    published_date=timezone.now()
                )

                article.save()
                self.stdout.write(f'Статья {article.title} добавлена')

        self.stdout.write("База успешно заполнена")
