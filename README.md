# Django Restaurant Site

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?logo=django&logoColor=white)

One of my early Django projects, built in 2024 while I was learning the framework.

A small multi-page website for a fictional restaurant, "King's Restora". It has a landing page, a menu page showing food categories as cards, a page for each category, and an About Us page. The site has no database models: the menu is rendered from a Python data structure (shaped like [TheMealDB](https://www.themealdb.com/) category data) passed to the templates.

While building it I practised:

- Django apps and URL routing with `include()` and named URLs
- template inheritance from a shared `base.html`
- built-in template filters such as `truncatewords`
- project-level and app-level static files

This repository also contains two smaller practice projects (see [Practice projects](#practice-projects)).

## Features

- Shared `base.html` with a Bootstrap 5 navbar (the current page is highlighted) and a footer, extended by every page
- Landing page with an introduction and an image served from the project's `static/` folder
- Menu page that loops over six food categories and shows each one as a card with image, name, ID and a shortened description
- A page per menu category with the full description
- About Us page with its own app-level CSS and image (`about_us/static/`)
- Two apps (`meal`, `about_us`) wired into the root URLconf

| URL | Page |
| --- | --- |
| `/` | Landing page (also at `/meal/index/`) |
| `/show_meals/` | Menu categories (also at `/meal/`) |
| `/show_meals/<id>/` | One menu category |
| `/about_us/` | About Us |

## Practice projects

| Folder | Apps | What it covers |
| --- | --- | --- |
| `practice-10.5/practice_10_5` | `firstapp` | Function views and URL routing for home, about and contact pages; passing context to templates; built-in template filters such as `date`, `join`, `add`, `cut`, `slice`, `random` and `truncatechars` |
| `practice-11.5/practice_11_5` | `mealapp` | Template inheritance; meal cards rendered from a list of dictionaries |

## Tech stack

| | |
| --- | --- |
| Language | Python 3.10+ |
| Framework | Django 5.0 |
| Database | SQLite (used only by Django's built-in apps) |
| Front end | Django templates, Bootstrap 5.3 and Font Awesome 6 (CDN) |

## Project structure

```
django-restaurant-site/
├── requirements.txt
├── assignment-3/
│   └── restu/
│       ├── manage.py
│       ├── restu/        # settings, root URLconf
│       ├── meal/         # landing page, menu and menu category views, tests
│       ├── about_us/     # About Us view, app-level CSS and image
│       ├── static/       # project-level images
│       └── templates/    # base.html
├── practice-10.5/
│   └── practice_10_5/
└── practice-11.5/
    └── practice_11_5/
```

## Getting started

```bash
git clone https://github.com/ratulhasan001/django-restaurant-site.git
cd django-restaurant-site

python3 -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cd assignment-3/restu
python manage.py migrate
python manage.py createsuperuser   # optional, only needed for /admin/
python manage.py runserver
```

Then open http://127.0.0.1:8000/. The apps define no models, so `migrate` only creates Django's built-in tables.

No environment variables are required. For anything other than local use, set `DJANGO_SECRET_KEY`, `DJANGO_DEBUG=False` and `DJANGO_ALLOWED_HOSTS` (comma-separated).

## Running the tests

```bash
cd assignment-3/restu
python manage.py test
```

The tests check that every page renders, that the menu lists all categories and links to each category page, and that unknown categories return a 404.

To run a practice project, `cd` into its folder (for example `practice-11.5/practice_11_5`) and run the same `migrate` and `runserver` commands.

## Later improvements

The original assignment version was tidied up later. Changes made then (main project only):

- `/` used to show an empty page (just the navbar); it now shows the landing page. The old `/meal/index/` URL still works.
- Removed a duplicate `about_us/` route and gave every page a named URL.
- Added a page per menu category, so the full description can be read; the About Us "Read More" button, which did nothing, now links to the menu.
- Fixed the "King's Resotra" typo, added page titles, an active navbar link, a footer and responsive image sizes.
- The template directory is resolved from the project folder, and `SECRET_KEY`, `DEBUG` and `ALLOWED_HOSTS` can be set through environment variables.
- Added a test suite.

## Author

Ratul Hasan · [ratulhasan.dev](https://ratulhasan.dev)
