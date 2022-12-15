from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # プロフ画像てきなもの
    image = models.ImageField('画像1', blank=True, null=True)

    # いいねしている人達を表現しているフィールド
    # 通常のManyToManyでは、自分がいいねすると相手も自分をいいねする仕様になるため
    # symmetrical=Falseが必要
    likes = models.ManyToManyField('self', blank=True, symmetrical=False, verbose_name='お気に入りの人達')
