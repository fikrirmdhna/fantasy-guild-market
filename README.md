## TAUTAN APLIKASI ADAPTABLE
[Fantasy Guild Market](https://fantasy-guild-market.adaptable.app/main/)

## MEMBUAT PROYEK DJANGO BARU
1. Membuat direktori utama, yaitu FANTASY-GUILD-MARKET
2. Buka terminal, lalu cd ke direktori utama dan jalankan command **python -m venv env** untuk membuat virtual environment
3. Jalakan virtual environment dengan command **source env/bin/activate** (Mac/Linux). Jika sudah aktif, maka ditandai oleh (env), env ini berguna untuk mengisolasi *package* dan *dependencies* dari aplikasi agar tidak terjadi kendala antar versi lain.
4. Membuat file requirement.txt yang berisi django dan dependencies lain untuk diinstall ke dalam proyek dengan command **pip install -r requirements.txt**
5. Membuat project Django bernama fantasy_guild_market dengan command **django-admin startproject fantasy_guild_market .** Lalu subdirektori akan terbuat dengan file bawaan, yaitu: __init__.py, asgi.py, settings.py, urls.py, wsgi.py.
6. Tambahkan "*" ke dalam ALLOWED_HOSTS agar mendapatkan akses host dari aplikasi web sebagai keperluan deployment.
7. Jalankan berkas manage.py dengan menyalakan virtual environment terlebih dahulu (step 3), lalu menjalankan command **python3 manage.py runserver** (Mac/Linux).
8. Lalu buka [localhost](http://localhost:8000/main/).
    * Untuk mematikan server bisa dilakukan dengan menekan control + C dan command **deactivate** untuk mematikan env.
9. Membuat repositori GitHub baru bernama fantasy-guild-market dengan visibilitas public dan settings yang lain default.
10. Jalankan command **git init** di terminal dengan cd direktori utama file lokal, yaitu FANTASY-GUILD-MARKET.
11. Buat berkas .gitignore di dalam direktori utama dengan isi:
```
# Django
*.log
*.pot
*.pyc
__pycache__
db.sqlite3
media

# Backup files
*.bak 

# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf

# AWS User-specific
.idea/**/aws.xml

# Generated files
.idea/**/contentModel.xml

# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml

# Gradle
.idea/**/gradle.xml
.idea/**/libraries

# File-based project format
*.iws

# IntelliJ
out/

# JIRA plugin
atlassian-ide-plugin.xml

# Python
*.py[cod] 
*$py.class 

# Distribution / packaging 
.Python build/ 
develop-eggs/ 
dist/ 
downloads/ 
eggs/ 
.eggs/ 
lib/ 
lib64/ 
parts/ 
sdist/ 
var/ 
wheels/ 
*.egg-info/ 
.installed.cfg 
*.egg 
*.manifest 
*.spec 

# Installer logs 
pip-log.txt 
pip-delete-this-directory.txt 

# Unit test / coverage reports 
htmlcov/ 
.tox/ 
.coverage 
.coverage.* 
.cache 
.pytest_cache/ 
nosetests.xml 
coverage.xml 
*.cover 
.hypothesis/ 

# Jupyter Notebook 
.ipynb_checkpoints 

# pyenv 
.python-version 

# celery 
celerybeat-schedule.* 

# SageMath parsed files 
*.sage.py 

# Environments 
.env 
.venv 
env/ 
venv/ 
ENV/ 
env.bak/ 
venv.bak/ 

# mkdocs documentation 
/site 

# mypy 
.mypy_cache/ 

# Sublime Text
*.tmlanguage.cache 
*.tmPreferences.cache 
*.stTheme.cache 
*.sublime-workspace 
*.sublime-project 

# sftp configuration file 
sftp-config.json 

# Package control specific files Package 
Control.last-run 
Control.ca-list 
Control.ca-bundle 
Control.system-ca-bundle 
GitHub.sublime-settings 

# Visual Studio Code
.vscode/* 
!.vscode/settings.json 
!.vscode/tasks.json 
!.vscode/launch.json 
!.vscode/extensions.json 
.history
```
Berkas ini bertujuan untuk mengabaikan file - file dan direktori yang harus diabaikan oleh Git. 

12. Lakukan git add, commit, dan push dari direktori repositori lokal. 
13. Login/Signup ke akun [Adaptable.io](https://adaptable.io/) menggunakan akun GitHub.
14. Saat sudah login, klik New App, lalu pilih Connect an Existing Repository. Hal ini bertujuan agar semua repositori yang ada di akun GitHub kamu bisa terbaca. 
15. Lalu pilih direktori fantasy-guild-market atau repositori lain yang ingin di-deploy. 
16. Pilih branch yang ingin dijadikan sebagai deployment branch. 
17. Pilih Python App Template (template) dan PostgreSQL (basis data) yang akan digunakan.
18. Pilih versi python yang sesuai. Jika lupa, gunakan command **python3 --version** (Mac/Linux) untuk mengetahui versi python yang terinstall. 
19. Pada bagian Start Command, masukkan command **python3 manage.py migrate && gunicorn fantasy_guild_market.wsgi** (Mac/Linux).
20. Masukkan nama aplikasi yang diinginkan dan centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses app deployment.