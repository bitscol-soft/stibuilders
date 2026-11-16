# STI Builders — Website Redesign

A complete front-end redesign of the STI Builders Limited website, built as a new
Django app (`website`) on top of the existing project. The legacy CMS/dashboard
(`realstateapp`, `property`) is untouched and still reachable under `/cms/`.

## What is included

**Information architecture**
| Route | Page |
|---|---|
| `/` | Home — hero carousel, quick search, stage tabs, suburb insights, map, testimonials, journal |
| `/projects/` | Advanced project listing: stage, budget, size, beds, type, suburb, amenities, ownership, availability + sorting, grid/list, map |
| `/projects/<slug>/` | Project detail with 11 anchored sections (see below) |
| `/projects/compare/` | Side-by-side comparison of up to four projects |
| `/suburbs/`, `/suburbs/<slug>/` | Suburb analytics & insights, landmarks, local projects |
| `/booking/` | Three-step booking wizard (visit, reserve, call back, brochure) |
| `/saved/` | Session-based shortlist |
| `/land-sharing/` | Land-sharing model, split donut, FAQ |
| `/investors/` | Yield & growth table, NRI support |
| `/about/`, `/services/`, `/services/<slug>/` | Corporate |
| `/news/`, `/news/<slug>/`, `/gallery/`, `/contact/`, `/faq/` | Editorial & contact |
| `/sitemap.xml`, `/robots.txt` | SEO |

**Project detail sections**
Overview · Building information · Apartments & flats (layout cards + full inventory
table) · Amenities · Location & landmarks (Google Maps + categorised distances) ·
Design & drawings (floor plans, elevations, site plan) · Project milestones/stages ·
Land-sharing breakdown (owner/developer split + delivery schedule) · Project videos ·
Project profile & brochure · Social channels & sharing (Facebook, WhatsApp, X,
LinkedIn, Pinterest, email, copy link).

## Design language

Warm editorial architectural theme, no CSS framework and no external CDN calls
(works fully offline):

* Ink `#0c1f26`, paper `#fbf9f5`, copper `#b3742f`, moss `#3d5a4c`.
* Instrument-Serif-style display type with an italic copper accent for the hero;
  a Manrope-style geometric sans for UI and body.
* Full inline SVG icon sprite (`templates/website/partials/_icons.html`) — 80+ icons.
* Motion: hero pan, scroll reveal, counters, hover cross-fade project images,
  marquee trust strip, sticky section nav. All disabled under
  `prefers-reduced-motion`.
* Fully responsive from 320 px up, mobile filter drawer, mobile sticky booking bar.

## Running locally

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_website          # realistic demo content
python manage.py runserver 0.0.0.0:8000
```

Optional admin account for the CMS:

```bash
python manage.py createsuperuser
```

Admin panel: `/admin/` — projects, gallery, drawings, milestones, apartments,
bookings, enquiries, suburbs, services, team, testimonials, news, FAQs, settings.
Booking requests can be exported to CSV from the admin list view.

## Configuration

Settings are environment-driven:

| Variable | Default | Notes |
|---|---|---|
| `DJANGO_DEBUG` | `true` | set `false` in production |
| `DATABASE_ENGINE` | `sqlite` | set `mysql` to use MySQL |
| `DB_NAME`, `DB_USER`, `DB_PASSWORD`, `DB_HOST`, `DB_PORT` | — | used when `DATABASE_ENGINE=mysql` |
| `MEDIA_ROOT`, `MEDIA_URL` | app static tree, `/media/` | point at object storage in production |
| `STATIC_ROOT` | `staticfiles/` | run `collectstatic` before deploy |
| `CSRF_TRUSTED_ORIGINS` | `https://*.e2b.app,…` | add the production domain |

## Tests

```bash
python manage.py test website
```

16 tests cover page rendering, filters, detail sections, booking/enquiry
submission, shortlist toggling, JSON feeds, sitemap and money formatting.

## Notes

* Demo imagery is bundled under `website/static/website/img/` and copied into
  `MEDIA_ROOT` by the seeder so media URLs match production behaviour.
* Legacy build (`realstateapp`, `property`) data is untouched; the old public URL
  patterns 301-redirect into the new information architecture.
* The proposal PDF referenced Laravel/React; this repository is Django, so the
  redesign ships as a Django app with server-rendered templates, zero build step.
