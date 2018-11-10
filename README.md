## Development Notes

 - Start dev containers with `./dc up`
 - Load dev fixtures by downloading latest DB backup file from S3 and put in the app container at
   path `/data/sqlite/keithvaluation.db`.
 - Sync media from latest backup and put in `/media` of the app container.
 - Run `./dc exec app ./manage.py collectstatic`.
 - Run `./dc exec admin ./manage.py collectstatic`.
 - Run app Django dev server with `make run-app-dev`.
 - Make sure dev domains `dev.keithvaluation.com`, `dev-admin.keithvaluation.com` and
   `www.dev.keithvaluation.com` are aliased to `127.0.7.1` in `/etc/hosts`.
 - Go to `www.dev.keithvaluation.com` in browser.
 - Admin is at `dev-admin.keithvaluation.com`.
