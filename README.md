# 社員名簿システム

Djangoで作成した社員情報を管理するWebアプリケーションです。

## 機能

- 社員一覧表示（入社日の新しい順）
- 社員詳細表示
- 社員の新規登録
- 社員情報の編集
- 社員の削除

## 使用技術

- Python 3.12
- Django 6.0
- PostgreSQL 15
- Docker / Docker Compose

## 起動方法

```bash
docker compose up
```

ブラウザで `http://127.0.0.1:8000/portal/list/` にアクセス。

## 管理画面

`http://127.0.0.1:8000/admin/` からスーパーユーザーでログインして社員データを管理できます。

```bash
python manage.py createsuperuser
```

## URL一覧

| URL | 内容 |
|---|---|
| `/portal/list/` | 社員一覧 |
| `/portal/new/` | 新規登録 |
| `/portal/<id>/` | 社員詳細 |
| `/portal/edit/<id>/` | 社員編集 |
| `/portal/delete/<id>/` | 社員削除 |
| `/admin/` | 管理画面 |