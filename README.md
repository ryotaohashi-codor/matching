# マッチングアプリのデモ

## 必要ライブラリ

django
django-allauth
pillow

```
pip install -r requirements.txt
```

## 動かし方

### 開発環境で動かす

```
python manage.py migrate
python manage.py runserver
```

### 本番環境で動かす

pro_manage.py や pro_wsgi.py を使うことで、本番環境用の設定ファイル(pro_settings.py)が自動的に読み込まれます。

```
python pro_manage.py migrate
python pro_manage.py collectstatic
gunicorn --workers 3 --bind 127.0.0.1:8000 project.pro_wsgi:application
```

上は、gunicorn で実行していますが、実際は systemd(/etc/systemd/system/mydjango.service)を使って次のように記述して起動しています。

```
[Unit]
Description=gunicorn
After=network.target
[Service]
WorkingDirectory=/home/ubuntu/matching
ExecStart=/usr/local/bin/gunicorn --workers 3 --bind 127.0.0.1:8000 project.pro_wsgi:application
[Install]
WantedBy=multi-user.target

```
