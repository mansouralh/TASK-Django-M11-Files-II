Time to purchase some islands!

## Setup

1. Fork and clone [this repository](https://github.com/malthunayan/TASK-Django-M11-Files-II).
2. Install the `requirements` using `pip install -r requirements/dev.lock`.
3. Run the `migrations`.

## Task

### Static & Media Files

1. Add the set up for static files in `settings.py`:

   ```python
   STATIC_URL = "static/"
   STATIC_ROOT = BASE_DIR / "static"
   ```

2. Add the set up for static files in `urls.py`:

   ```python
   ...

   from django.conf import settings
   from django.conf.urls.static import static


   urlpatterns = [
       ...
   ]

   if settings.DEBUG:
       urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   ```

3. Add the set up for media files in `settings.py`:

   ```python
   MEDIA_URL = "media/"
   MEDIA_ROOT = BASE_DIR / "media"
   ```

4. Add the set up for media files in `urls.py`:

   ```python
   ...


   urlpatterns = [
       ...
   ]

   if settings.DEBUG:
       ...
       urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   ```

5. Go the admin site and create some islands (if you do this step before setting up media files, the images will be in the root directory of the project).
6. Go to `http://localhost:8000/islands/` and see your beautiful islands!
7. Fix the image by adding a `src` (look [here](https://docs.djangoproject.com/en/4.1/topics/files/#using-files-in-models) for help).
8. Load your static file here and add a `static` folder inside of `islands`.
9. Add a stylesheet for your island list template and link it inside the template.
10. Add some CSS and prettify your list of island!
11. Commit your code.
12. Push your code.
