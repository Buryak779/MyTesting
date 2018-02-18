from django.db import models


class MyTest(models.Model):
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    created = models.DateTimeField("Дата создания",auto_now_add=True)
    moderation = models.BooleanField("Модерация", default=False)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тесты"

    def __str__(self):
        return self.title


class Vote(models.Model):
    my_test = models.ForeignKey(MyTest, on_delete=models.CASCADE)
    question = models.TextField("Вопрос", max_length=270)
    answer_1 = models.CharField("Вариант1", max_length=100)
    answer_2 = models.CharField("Вариант2", max_length=100)
    answer_3 = models.CharField("Вариант3", max_length=100)
    answer_true = models.IntegerField("Правильный ответ", default=1)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.question

