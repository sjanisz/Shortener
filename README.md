# Shortener - for longer links shortening - NOT READY YET

Still TODO's for app:
	- go to mapped URL for shortened link;
	- think about that form and prevent re-generation of shortened link on page refresh with result.

<pre>
Project setup steps:
1. Create apache2 http website
	1.1. touch /etc/apache2/sites-available/shortener.conf
	1.2. vi /etc/apache2/sites-available/shortener.conf:
		&#60;virtualhost *:80=""&#62;
		ServerAdmin webmaster@localhost
		ServerName shortener
		ServerAlias shortener
		DocumentRoot /var/www/html/shortener
		ErrorLog ${APACHE_LOG_DIR}/error.log
		CustomLog ${APACHE_LOG_DIR}/access.log combined
		&#60;/virtualhost&#62;
	1.3. mkdir /var/www/html/shortener
	1.4. touch /var/www/html/shortener/index.html
	1.5. vi /var/www/html/shortener/index.html:
		add some HTML
	1.6. sudo systemctl restart apache2
	1.7. access website: localhost/shortener
2. Database: SQLite (+ sqlitebrowser (snap install sqlitebrowser))
	2.1. Model:
3. Flask installation: https://flask.palletsprojects.com/en/2.0.x/installation/
	3.1. Go to project dir
	3.2. Create virtual env: python3 -m venv venv
	3.3. Activate venv: . venv/bin/activate
	3.4. Install Flask: pip install Flask
4. Start http server:
	4.1. go to project directory
	4.2. python Shortener.py
5. 
</pre>
