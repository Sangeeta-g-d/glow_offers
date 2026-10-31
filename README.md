# AdVibe: skincare and beauty offers site

A small Django project with two pages:

- **User page** (`/`): cute pastel site that shows every offer as a card (image, title, description, link). Pinned offers appear at the top in their own "Pinned picks" section.
- **Admin page** (`/manage/`): login-protected dashboard where the admin can add an offer (image, title, 1 to 3 line description, link), pin or unpin it, and remove it when the offer ends.

## Setup

1. Install PostgreSQL and create an empty database:

```sql
-- open psql (or pgAdmin's query tool) and run:
CREATE DATABASE advibe;
```

2. Put your database details in `config/settings.py` (the `DATABASES` block), or set them as environment variables: `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT`.

3. Install and run:

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser   # this is your admin login
python manage.py runserver
```

Open:
- http://127.0.0.1:8000/ for the user page
- http://127.0.0.1:8000/manage/ for the admin page (log in with the superuser you created)

## Project layout

```
glow_offers/
  manage.py
  requirements.txt
  config/            settings, urls, wsgi/asgi
  offers/            model, form, views, urls
  templates/         base.html and offers/*.html
  static/css/        style.css (all the cute styling)
  media/             uploaded offer images (created automatically)
```

## Before going live

- Set `DEBUG = False`, set a new `SECRET_KEY`, and fill in `ALLOWED_HOSTS` in `config/settings.py`.
- Serve `/media/` with your web server (nginx, etc.) since Django only serves it in debug mode.
