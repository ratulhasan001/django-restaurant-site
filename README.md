# Django Restaurant Site

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?logo=django&logoColor=white)

A multi-page website for a fictional restaurant, "King's Restora", built with Django. It has a landing page, a menu page showing food categories as cards, and an About Us page. All pages share one base template with a Bootstrap navigation bar. The site has no database models: the menu is rendered from Python data structures (shaped like [TheMealDB](https://www.themealdb.com/) category data) passed to the templates. The project demonstrates Django apps, URL routing with `include()` and named URLs, template inheritance, template filters, and project-level and app-level static files.

This repository also contains two smaller practice projects (see [Practice projects](#practice-projects)).

## Features

- Shared `base.html` with a Bootstrap 5 navbar, extended by every page
- Landing page with an introduction and an image served from the project's `static/` folder
- Menu page that loops over six food categories and shows each one as a card with image, name, ID and a shortened description (`truncatewords`)
- About Us page with its own app-level CSS and image (`about_us/static/`)
- Two apps (`meal`, `about_us`) wired into the root URLconf

| URL | Page |
| --- | --- |
| `/meal/index/` | Landing page (the navbar's "Home" link) |
| `/show_meals/` | Menu categories |
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
│       ├── meal/         # landing page and menu views
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

Then open http://127.0.0.1:8000/meal/index/. The apps define no models, so `migrate` only creates Django's built-in tables. No environment variables are required.

To run a practice project, `cd` into its folder (for example `practice-11.5/practice_11_5`) and run the same `migrate` and `runserver` commands.

## Author

Ratul Hasan · [ratulhasan.dev](https://ratulhasan.dev)
