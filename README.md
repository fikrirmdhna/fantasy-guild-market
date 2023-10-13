# **Fantasy Guild Market**
## Tautan Aplikasi
* Tautan link Adaptable *(sebelum deactivate)*: [Fantasy Guild Market](https://fantasy-guild-market.adaptable.app/main/)
* Tautan link PaaS Fasilkom: [Fantasy Guild Market](http://fikri-dhiya21-tugas.pbp.cs.ui.ac.id)
<br>

# Tugas 2 
<details>
<summary>Expand</summary>

## Membuat Proyek Django Baru
1. Membuat direktori utama, yaitu FANTASY-GUILD-MARKET
2. Buka terminal, lalu cd ke direktori utama dan jalankan command `python3 -m venv env` (Mac/Linux) untuk membuat virtual environment
3. Jalakan virtual environment dengan command `source env/bin/activate` (Mac/Linux). Jika sudah aktif, maka ditandai oleh (env), env ini berguna untuk mengisolasi *package* dan *dependencies* dari aplikasi agar tidak terjadi kendala antar versi lain.
4. Membuat file requirement.txt yang berisi django dan dependencies lain untuk diinstall ke dalam proyek dengan command `pip install -r requirements.txt`
5. Membuat project Django bernama fantasy_guild_market dengan command `django-admin startproject fantasy_guild_market .` Lalu subdirektori akan terbuat dengan file bawaan, yaitu: __init__.py, asgi.py, settings.py, urls.py, wsgi.py.
6. Tambahkan "*" ke dalam ALLOWED_HOSTS agar mendapatkan akses host dari aplikasi web sebagai keperluan deployment.
7. Jalankan berkas manage.py dengan menyalakan virtual environment terlebih dahulu (step 3), lalu menjalankan command `python3 manage.py runserver` (Mac/Linux).
8. Lalu buka [localhost](http://localhost:8000/main/).
    * Untuk mematikan server bisa dilakukan dengan menekan control + C dan command `deactivate` untuk mematikan env.
9. Membuat repositori GitHub baru bernama fantasy-guild-market dengan visibilitas public dan settings yang lain default.
10. Jalankan command `git init` di terminal dengan cd direktori utama file lokal, yaitu FANTASY-GUILD-MARKET.
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

## Membuat aplikasi dengan nama main pada proyek FANTASY-GUILD-MARKET
1. Pastikan (env) sudah dinyalakan. 
2. Jalankan command `python3 manage.py startapp main` (Mac/Linux) di lokal direktori utama. 
3. Setelah main sudah muncul di dalam direktori, lalu tambahkan main list INSTALLED_APPS di dalam settings.py yang berada di subdirektori fantasy_guild_market, seperti: 
    ```python
    INSTALLED_APPS = [
        ...,
        'main',
        ...
    ]
    ```

## Melakukan routing pada proyek agar bisa menjalankan main
1. Buka file urls.py di dalam direktori fantasy_guild_market. 
2. Tambahkan isi dari urls.py dengan kode, yaitu:
    ```python
    from django.urls import path, include
    ```
    ```python
    urlpatterns = [
        ...
        path('main/', include('main.urls')),
        ...
    ]
    ```
3. include dibutuhkan karena kita akan me-routing main.urls yang dimana selain 'admin/' oleh karena itu dibutuhkan fungsi include.

## Membuat model pada aplikasi main dengan nama Item dan memiliki atribut
1. Pada step ini, kita perlu mengedit isi dari models.py dengan kode:
    ```python
    from django.db import models

    # Create your models here.
    class Items(models.Model):
        # name, amount, description merupakan komponen wajib yang berupa CharField, IntegerField, dan TextField
        name = models.CharField(max_length=255)          
        amount = models.IntegerField()                  
        description = models.TextField()             
        price = models.IntegerField()
        power = models.IntegerField()
        date_added = models.DateField(auto_now_add=True)
    ```
2. Jalankan perintah `python3 manage.py makemigrations` dan `python3 manage.py migrate` (Mac/Linux), kode ini bertujuan untuk menciptakan dan mengaplikasikan perubahan model ke dalam basis data.

## Membuat fungsi pada views.py di dalam direktori main
1. Buka file views.py dan tambahkan `from django.shortcuts import render` yang bertujuan agar data - data yang berada di dalam struktur data views.py dapat di-render dan ditampilkan di HTML.
    ```python
    def show_main(request):
        context = {
            'name': 'Fikri Dhiya Ramadhana',
            'class': 'PBP C',
            'amount': 0,
            'list_items' : [
                {
                    'item'  : "long sword",
                    'price' : 200,
                    'power' : 100,
                    'description': "long double-edged sword",
                },
                {
                    'item'  : "healing potion",
                    'price' : 50,
                    'power' : 0,
                    'description': "restore health by 50%",
                },
                {
                    'item'  : "shield",
                    'price' : 100,
                    'power' : 50,
                    'description': "block enemy atk",
                },
                {
                    'item'  : "armor",
                    'price' : 150,
                    'power' : 75,
                    'description': "increase def stat",
                }
            ]
        }
        return render(request, "main.html", context)
    ```
2. Untuk menampilkan data yang berada di dalam views.py, gunakan syntax {{ key }}, lalu HTML akan menampilkan value yang ada dari key yang dipanggil. 

## Membuat routing pada urls.py di dalam direktori main
1. Hal ini dilakukan untuk memetakan fungsi yang dibuat di dalam views.py.
2. Buat file di dalam direktori main dengan nama urls.py.
3. Isi file dengan kode: 
    ```python
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
4. urls.py yang berada di main bertanggung jawab untuk mengatur rute URL yang terkait dengan aplikasi main.

## Melakukan Deployment ke Adaptable
1. Login/SignUp ke akun [Adaptable.io](https://adaptable.io/) menggunakan akun GitHub.
2. Saat sudah login, klik New App, lalu pilih Connect an Existing Repository. Hal ini bertujuan agar semua repositori yang ada di akun GitHub kamu bisa terbaca. 
3. Lalu pilih direktori fantasy-guild-market atau repositori lain yang ingin di-deploy. 
4. Pilih branch yang ingin dijadikan sebagai deployment branch. 
5. Pilih **Python App Template** (template) dan **PostgreSQL** (basis data) yang akan digunakan.
6. Pilih versi python yang sesuai. Jika lupa, gunakan command `python3 --version` (Mac/Linux) untuk mengetahui versi python yang terinstall. 
7. Pada bagian Start Command, masukkan command `python3 manage.py migrate && gunicorn fantasy_guild_market.wsgi` (Mac/Linux).
8. Masukkan nama aplikasi yang diinginkan dan centang bagian HTTP Listener on PORT dan klik Deploy App untuk memulai proses app deployment.

## Bagan Client Request and Response Django
![](image/DjangoCRR.png)
### Penjelasan Bagan
1. Browser yang diakses oleh client akan me-request ke dalam Web Server.
2. Request dari client akan diproses oleh Web Server.
3. Server HTTP akan diproses oleh WSGI untuk web yang berbasis python.
4. Request client akan dilanjutkan ke middleware request yang menjadi penghubung proyek dalam memproses request. 
5. Alamat request dari client akan di-direct oleh URL Router ke dalam fungsi di dalam views.py.
6. Kemudian, views.py akan me-render data - data yang akan ditampilkan di dalam template HTML. Data yang diproses merupakan data yang sudah diatur oleh ORM dalam file models.py.
7. Lalu data - data dari views.py akan dikirimkan oleh context processor ke template HTML.
8. Data yang tampil di template HTML akan sesuai dengan logika dari template tags. 
9. Middleware Response akan memproses dan meneruskan response ke WSGI.
10. Server HTTP untuk web berbasis python akan diproses oleh WSGI.
11. Lalu, web server akan menerima dan meneruskan response ke client.
12. Response diterima oleh client.

## Mengapa kita menggunakan virtual environment?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Virtual environment sangat berguna untuk dependencies terhadap proyek satu dengan yang lain atau terisolasi. Dalam penggunaannya, virtual environment memudahkan kita untuk melihat semua dependencies dari proyek yang kita buat di dalam **requirements.txt**. Dan penggunaan virtual environment dapat meningkatkan portabilitas karena memungkinkan kita untuk menjalankan proyek Django kita secara konsisten dan independen di berbagai lingkungan.

## Apa kita tetap bisa membuat proyek Django tanpa menggunakan virtual environment?
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bisa, namun tidak disarankan karena memungkinkan terjadinya konflik terhadap proyek yang dibuat, contohnya konflik terhadap dependencies karena akan sulit dikelola, ketidakstabilan proyek karena suatu saat sistem konfigurasinya dapat berubah - ubah, dan hal ini juga bergantung pada versi Django saat membuat proyek dan penggunaan dependencies tertentu yang berbeda, jika tidak sesuai maka akan menimbulkan konflik terhadap sistem. 

## Apa itu MVC, MVT, MVVM dan apa perbedaannya?
Ketiga itu adalah pola bentuk arsitektur dalam sebuah proyek yang memberikan modularitas pada file proyek dan memastikan kode ter-cover dalam suatu uji testing yang memiliki persamaan:
* Model: untuk menyimpan data aplikasi yang terhubung dengan database. 
* View: menerima masukkan data dan menampilkan informasi ke client.

1. MVC (Model-View-Controller)
    * Controller: merupakan jembatan antara model dan view dalam mengelola permintaan client.

2. MVT (Model-View-Template)
    * Template: tempat untuk menampilkan atau me-render data dengan kode HTML yang bersifat *static* atau *dynamic*.

3. MVVM (Model-View-ViewModel)
    * ViewModel: merupakan perantara antar model dan view yang berperan sebagai stream data server sehingga data yang berada dimodel akan ditampilkan oleh view sesuai dengan format yang diperbolehkan.

* Perbedaan MVC, MVT, MVVM

    | MVC     | MVT    | MVVM   |
    | :--------: |:--------:| :-------:|
    | Input client diterima oleh Controller     |   Input client diterima oleh View        |  Input client diterima oleh View dan menjadi entry point dari aplikasi        |
    | Controller dan View memiliki relasi one-to-many  | Template dan View memiliki relasi one-to-one | View dan ViewModel memiliki relasi one-to-many |
    | Rumit untuk dimodifikasi  | Mudah untuk dimodifikasi | Mudah untuk dimodifikasi jika data binding tidak terlalu complex  |
    | Tidak mememerlukan URL Mapping | Memerlukan URL Mapping  | Tidak terlalu bergantung terhadap URL Mapping |
</details>
<br>

# Tugas 3
<details>
<summary>Expand</summary>

## Membuat input form untuk menambahkan object
1. Membuat file forms.py di direktori main untuk menampilkan page form baru yang berisi kode: 
    ```python
    from django.forms import ModelForm
    from main.models import Items

    class ProductForm(ModelForm):
        class Meta:
            model = Items
            fields = ["name", "price", "power", "description"]
    ```
    Model di sini adalah Items yang akan menyimpan item baru jika form sudah selesai diisi dengan isian fields yang diperlukan.

2. Lalu menambahkan beberapa import dan function untuk menambah item baru di views.py yang berada di direktori main, yaitu:
    ```python
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse
    ```
    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```
    `form = ProductForm(request.POST or None)` kode ini digunakan untuk membentuk sebuah form dan menyimpan data yang diisi sesuai dari fields yang ada di forms.py, lalu dicek apakah form valid dan request methodnya POST `if form.is_valid() and request.method == "POST":`, maka form akan di save `form.save()` dan `HttpResponseRedirect(reverse('main:show_main'))` akan men-direct page ke page main:show_main atau page utama. 

3. Menambahkan objects pada fungsi show_main yang ada di views.py menjadi:
    ```python
    def show_main(request):
        items = Items.objects.all()

        context = {
            'name': 'Fikri Dhiya Ramadhana',
            'class': 'PBP C',
            'amount': 0,
            'items' : items,
        }

        return render(request, "main.html", context)
    ```
    `items = Items.objects.all()` kode ini digunakan untuk mengambil semua objek yang berada di database.

4. Menambahkan import function dan path create_product ke urls.pt yang berada di direktori main dengan:
    ```python
    from main.views import show_main, create_product
    ```
    dan menambahkan path di bagian urlpatterns
    ```python
    ...
    path('create-product', create_product, name='create_product'),
    ...
    ```

5. Membuat berkas baru pada main/templates yang bernama create_product.html dengan isi:
    ```html
    {% extends 'base.html' %} 

    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
        {% csrf_token %} <!-- kode yang otomatis di generate untuk mencegah serangan bahaya -->
        <table>
            {{ form.as_table }} <!-- membuat fields form menjadi tabel -->
            <tr>
                <td></td>
                <td>
                     <input type="submit" value="Add Product"/> <!-- untuk men-submit dan mengirim request ke function create_product di views -->
                </td>
            </tr>
        </table>
    </form>

    {% endblock %}
    ```

6. Tambahkan `{% block content %}` dan `{% endblock content %}` di paling atas dan di paling bawah dalam main.html serta tambahkan tombol Add New Product, seperti:
    ```html
    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>
    ```

## Menambahkan 5 fungsi views.py untuk melihat object dalam format HTML, XML, JSON, XML_by_ID, dan JSON_by_ID 
* format HTML seperti step no. 2, 3, 4, 5, dan 6 di atas.
1. Di dalam views.py direktori main, tambahkan import:
    ```python
    from django.http import HttpResponse
    from django.core import serializers
    ```

2. Lalu, buatlah function:
    * format XML
    ```python
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    * format JSON
    ```python
    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
    * format XML_by_ID
    ```python
    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```
    * format JSON_by_ID
    ```python
    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

## Membuat routing URL masing - masing format
1. Tambahkan import pada urls.py direktori main menjadi:
    ```python
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
    ```

2. Kemudian tambahkan path di urlpatterns-nya dengan: 
    ```python
    ...
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    ...
    ```

## Perbedaan antaran form POST dan form GET di Django
* form POST: biasanya digunakan dalam pembuatan form login, register, atau add new product dalam tugas PBP ini karena POST method sendiri mengumpulkan data, lalu data akan dikodekan untuk transmisi yang akan dikirimkan ke server/database, kemudian menerima respon dari form tersebut.

* form GET: biasanya digunakan dalam form kolom pencarian atau search box karena method ini menggabungkan data lalu dikirim ke dalam string yang akan digunakan untuk membuat URL dan GET ini digunakan untuk menerima permintaan saja dan tidak mengubah keadaan database/sistem.

## Perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data
 | XML     | JSON    | HTML  |
| :--------: |:--------:| :-------:|
| digunakan untuk pertukaran data antara aplikasi yang berbeda yang berupa data berbasis teks dan data terstruktur dengan baik     |  data yang berbasis syntax key-value sebagai representasi dari objek array dan pertukaran data berjalan di Application Programming Interface (API)   |  bahasa markup untuk membuat tampilan dan struktur webpage, data yang ada akan dimuat untuk menampilkan tampilan webpage   |

## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern
JSON sering digunakan dalam pertukaran data karena: 
* bahasanya yang ringkas dan mudah dipahami
* data yang digunakan terstruktur 
* dapat diproses secara cepat
* sering digunakan dalam pengembangan API berbasis REST (Representational State Transfer)
* mendukung berbagai tipe data dan kompatibel dengan javascript

## Hasil akses URL pada Postman
1. HTML
![](image/Screenshot%202023-09-19%20at%2008.28.50.png)

2. XML
![](image/Screenshot%202023-09-19%20at%2008.29.12.png)

3. JSON
![](image/Screenshot%202023-09-19%20at%2008.29.39.png)

4. XML by ID
![](image/Screenshot%202023-09-19%20at%2008.29.54.png)

5. JSON by ID
![](image/Screenshot%202023-09-19%20at%2008.30.06.png)
</details>
<br>

# Tugas 4
<details>
<summary>Expand</summary>

## Mengimplementasikan fungsi registrasi, login, dan logout
1. Tambahkan import pada views.py:
    * untuk register
        ```python
        from django.shortcuts import redirect
        from django.contrib.auth.forms import UserCreationForm
        from django.contrib import messages
        ```
    * untuk login
        ```python
        from django.contrib.auth import authenticate, login
        ```
    * untuk logout
        ```python
        from django.contrib.auth import logout
        ```

2. Lalu tambahkan fungsi, masing - masing function:
    * untuk register
        ```python
        def register(request):
            form = UserCreationForm()

            if request.method == "POST":
                form = UserCreationForm(request.POST)
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Your account has been successfully created!')
                    return redirect('main:login')
            context = {'form':form}
            return render(request, 'register.html', context)
        ```
    * untuk login
        ```python
        def login_user(request):
            if request.method == 'POST':
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('main:show_main')
                else:
                    messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            context = {}
            return render(request, 'login.html', context)
        ```
    * untuk logout
        ```python
        def logout_user(request):
            logout(request)
            return redirect('main:login')
        ```

3. Buat berkas html baru di main/templates, yaitu:
    * register.html
        ```html
        {% extends 'base.html' %}

        {% block meta %}
            <title>Register</title>
        {% endblock meta %}

        {% block content %}  

        <div class = "login">
            
            <h1>Register</h1>  

                <form method="POST" >  
                    {% csrf_token %}  
                    <table>  
                        {{ form.as_table }}  
                        <tr>  
                            <td></td>
                            <td><input type="submit" name="submit" value="Daftar"/></td>  
                        </tr>  
                    </table>  
                </form>

            {% if messages %}  
                <ul>   
                    {% for message in messages %}  
                        <li>{{ message }}</li>  
                        {% endfor %}  
                </ul>   
            {% endif %}

        </div>  

        {% endblock content %}
        ```
    * login.html
        ```html
        {% extends 'base.html' %}

        {% block meta %}
            <title>Login</title>
        {% endblock meta %}

        {% block content %}

        <div class = "login">

            <h1>Login</h1>

            <form method="POST" action="">
                {% csrf_token %}
                <table>
                    <tr>
                        <td>Username: </td>
                        <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
                    </tr>
                            
                    <tr>
                        <td>Password: </td>
                        <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
                    </tr>

                    <tr>
                        <td></td>
                        <td><input class="btn login_btn" type="submit" value="Login"></td>
                    </tr>
                </table>
            </form>

            {% if messages %}
                <ul>
                    {% for message in messages %}
                        <li>{{ message }}</li>
                    {% endfor %}
                </ul>
            {% endif %}     
                
            Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

        </div>

        {% endblock content %}
        ```
    * khusus untuk logout hanya menambahkan button di main.html
        ```html
        ...
        <a href="{% url 'main:logout' %}">
            <button>
                Logout
            </button>
        </a>
        ...
        ```

4. Tambahkan import dan path ke main/urls.py dan urlpatterns main/urls.py
    ```python
    from main.views import register, login_user, logout_user
    ```
    ```python
    ...
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    ...
    ```

## Membuat dua akun pengguna dengan masing - masing tiga dummy data
1. akun fikri2211
![](image/Screenshot%202023-09-26%20at%2020.06.46.png)

2. akun dummy1
![](image/Screenshot%202023-09-26%20at%2020.07.05.png)

## Menghubungkan model Item dengan User
1. Menambah import dan model pada main/models.py:
    ```python
    ...
    from django.contrib.auth.models import User
    ...
    ```
    ```python
    class Items(models.Model):
        ...
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        ...
    ```

2. Mengubah function create_product di main/views.py
    ```python
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
        ...
    ```

3. Mengganti value dari key name untuk mereturn nama user yang login
    ```python
    def show_main(request):
        Items = Items.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
            ...
        }
    ...
    ```

4. Jalankan command `python3 manage.py makemigrations` dan `python3 manage.py migrate` untuk menyimpan perubahan pada model.

## Menerapkan cookies seperti last login pada halaman utama
1. Tambahkan import ke views.py:
    ```python
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```

2. Mengubah kode fucntion login_user di bagian:
    ```python
    ...
    if user is not None:
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main")) 
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```

3. Menambahkan kode last_login ke dalam context show_main wiews.py:
    ```python
    context = {
        ...
        'last_login': request.COOKIES['last_login'],
        ...
    }
    ```

4. Ubah function logout_user menjadi:
    ```python
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```

5. Menambahkan potongan kode di dalam main.html untuk menampilkan sesi terakhir login:
    ```html
    ...
    <h5>Sesi terakhir login: {{ last_login }}</h5>
    ...
    ```

## Django UserCreationForm itu apa? Apa kelebihan dan kekurangannya?

* UserCreationForm adalah suatu bentuk form untuk mendaftarkan user atau membuat akun baru.

    * Kelebihan: 
        1. Lebih mudah digunakan.
        2. Validasi otomatis.
        3. Aman karena sudah berintegrasi dengan Authentication Framework.

    * Kekurangan:
        1. Keterbatasan desain.
        2. Customization yang terbatas.
        3. Bergantung pada framework Django.

## Perbedaan antara Authentication dengan Authorization
| Authentication     | Authorization    | 
| :--------: |:--------:| 
| merupakan proses verifikasi atau pengecekan identitas seseorang atau login.   | pemberian otoritas atau proses verifikasi jika suatu user mempunya akses terhadap sistem. |  

## Apa itu cookies dalam konteks aplikasi web dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?

* Cookies adalah potongan data yang disimpan di sisi klien biasanya untuk menyimpan session id. Cookies juga berguna untuk mengingat informasi login dari si pengguna. 

* Cara Django menggunakan cookies untuk mengelola sesi data pengguna adalah:
    1. Membuat session cookies.
    2. Menyimpan data berupa session id.
    3. Mengirim cookie ke klien.
    4. Menerima cookie di permintaan selanjutnya.
    5. Mengakses session data.

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?

* Dalam penggunaan cookies, kita harus mewaspadai terkait data apa yang disimpan ke dalam cookies bukanlah data sensitif dan selalu memvalidasi data sesi pengguna agar tidak terkena session hijacking.
</details>
<br>

# Tugas 5
<details>
<summary>Expand</summary>

## Kustomisasi tampilan web
1. Tambahkan kode pada settings.py sebelum bagian `DEFAULT_AUTO_FIELD` di direktori proyek fantasy_guild_market:
    ```python
    ...
    STATIC_URL = 'static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    ...
    ```
2. Membuat folder static yang berada di direktori main untuk menyimpan file.css
    * login.css
        ```css
        *{
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        }
        body{
            background-image: url("https://static.wikia.nocookie.net/log-horizon/images/9/9b/RTC.jpg/revision/latest?cb=20141219174242");
            background-size: cover;
            background-attachment:fixed;
            background-repeat: no-repeat;
        }
        .container{
            margin-top: -50px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login{
            background-color: rgba(255,255,255, 0.8);
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
            text-align: center;
            padding: 20px;
            width: 375px;
        }
        .loginbutton{
        margin-right: 85px;
        }
        .style1{
            text-align: center;
        }
        ```
    
    * register.css
        ```css
        *{
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        }
        body{
            background-image: url("https://images.hdqwalls.com/wallpapers/cityscape-sky-anime-girl-peace-alone-4k-yg.jpg");
            background-size: cover;
            background-attachment:fixed;
            background-repeat: no-repeat;
        }
        .container{
            margin-top: -50px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .login{
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
            text-align: center;
            padding: 25px;
            margin-left: auto;
            margin-right: auto;
            margin-top: auto;
            margin-bottom: auto;
        }
        .title{
            text-align: center;
        }
        .loginbutton{
            margin-left: -190px;
        }
        ```

    * create_product.css
        ```css
        *{
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
        }
        .container{
            margin-top: -50px;
            display: flex;
            justify-content: center;
            text-align: left;
            align-items:center;
            height: 100vh;
        }
        .element{
            background-color: rgba(255, 255, 255, 0.8);
            border-radius: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
            padding: 25px;
            margin-left: auto;
            margin-right: auto;
            margin-top: auto;
            margin-bottom: auto;
        }
        .h1{
            text-align: center;
        }
        .button{
            margin-left: 60px;
        }
        body{
            background-image: url("https://i.redd.it/500pllhyaf3b1.jpg?w=144");
            background-size: cover;
            background-attachment:fixed;
            background-repeat: no-repeat;
        }
        ```
    
    * main.css
        ```css
        body{
            background-image: url("https://getwallpapers.com/wallpaper/full/4/e/2/1282331-sword-art-online-desktop-wallpaper-1920x1080-for-windows-7.jpg");
            background-size: cover;
            background-attachment:fixed;
            background-repeat: no-repeat;
        }
        .container{
            margin-top: -50px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 25vh;
        }
        .backgroundCard{
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 20px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
            text-align: center;
            padding: 30px;
            margin-left: auto;
            margin-right: auto;
            margin-top: auto;
            margin-bottom: auto;
            width: 1000px;
        }
        div{
            font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;
            text-align: center;
        }
        h1{
            text-align: center;
        }
        h3{
            text-align: center;
        }
        table {
            margin-left: auto;
            margin-right: auto;
            border-style: solid;
            border-color: rgb(34, 72, 175);   
        }
        th{
            border-style: outset;
            border-color: rgb(34, 72, 175);
            padding: 5px;
            background-color: lightgrey;
            text-align: center;
            font-family:  'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;;
        }
        td{
            border-style: solid;
            border-color: rgb(29, 149, 127);
            background-color:greenyellow;
            text-align: center;
        }
        a{
            justify-content: center;
            align-items: center;
            height: 200px;
        }
        ```

3. Tambahkan `{% load static %}` di bagian atas setiap file html yang akan dipakaikan file.css dan tambahkan tag link html `<link rel="stylesheet" href="{% static '{nama file}.css' %}">` di dalam {% block meta %} untuk mengimplementasikan file eksternal css ke html yang ingin dikostumisasi.

4. Kostumisasi menggunakan bootstrap css di login.html:
    ```html
    {% block meta %}
    ...
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    ...
    {% endblock meta %}
    ```

## Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya
1. Selector Universal (*):
    Berguna jika ingin mengubah semua elemen di dalam html. Penggunaannya berpengaruh terhadap kinerja.
2. Tag Selector (`<div>, <h1>`, dsb):
    Berguna untuk kustomisasi yang berbeda setiap tag html yang ada jadi lebih fleksibel. Dapat digunakan kapan saja. 
3. Selector ID (#):
    Berguna jika ingin kostumisasi tag html yang memiliki atribut id yang samasehingga bisa diubah secara unik. Dapat digunakan saat ingin mengubah tampilan secara lebih spesifik. 
4. Selector Kelas (.):
    Berguna dalam kostumisasi tag html yang berdasarkan atribut class yang sama. Dapat digunakan saat ingin mengubah tampilan berdasarkan class yang sama.

## HTML5 Tag
* Merupakan Markup Language standar terbaru, yaitu versi 5 (dideklarasikan dengan `<!DOCTYPE html>`) yang dimana menyediakan berbagai elemen baru, seperti: `<link>, <sytle>, <script>, <nav>`, dan masih banyak lagi.

## Perbedaan antara margin dan padding
| Margin     | Padding    | 
| :--------: |:--------:| 
| merupakan ruang yang berada di luar elemen | merupakan ruang yang berada di dalam elemen |
| digunakan untuk mengatur letak suatu container | digunakan saat ingin mengatur jarak antara elemen dengan border | 
| mengatur jarak di luar elemen | mengatur jarak di dalam elemen | 

## Perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya waktu penggunaan Tailwind atau Bootstrap? 

* Perbedaan
    | Tailwind     | Bootstrap    | 
    | :--------: |:--------:| 
    | tampilan dengan menggabungkan class utility yang telah didefinisikan | tampilan yang sudah jadi dan siap pakai |
    | memiliki file css yang lebih sedikit | memiliki file css yang lebih besar | 
    | fleksibilitas dan adaptabilitas yang tinggi | tampilan yang lebih konsisten | 
    | butuh pemahaman lebih tentang class utility | pemahaman lebih cepat karena merupakan tampilan instan | 

* Waktu Penggunaan
    | Tailwind     | Bootstrap    | 
    | :--------: |:--------:| 
    | dapat digunakan saat ingin bebas melakukan kostumisasi dan memiliki kontrol yang tinggi | dapat digunakan saat ingin menampilkan tampilan yang instan |
    | ingin belajar pendekatan class utility | ingin tampilan yang konsisten dan mudah dipakai | 
    | ingin menghindari kelas css yang tidak digunakan | sudah terbiasa menggunakan bootstrap khusus untuk proyek yang dibuat | 
</details>
<br>

# Tugas 6

## Implementasi AJAX GET
1. Membuat fungsi untuk me-return data JSON di views.py: 
    ```python
    def get_product_json(request):
        product_item = Items.objects.filter(user=request.user)
        return HttpResponse(serializers.serialize('json', product_item))
    ```

2. Menambahkan function async getProducts() di dalam main.html:
    ```html
    <script>
        async function getProducts() {
            return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
        }
    </script>
    ```

## Implementasi AJAX POST
1. Membuat tombol untuk memunculkan modal form dengan cara menambahkan kode berikut ke dalam main.html:
    ```html
    <div class="modal fade" id="exampleModal" role="dialog" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog">
                <div class="modal-content">
                    <div class="modal-header">
                        <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Product</h1>
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div class="modal-body">
                        <form id="form" onsubmit="return false;">
                            {% csrf_token %}
                            <div class="mb-3">
                                <label for="name" class="col-form-label">Name:</label>
                                <input type="text" class="form-control" id="name" name="name"></input>
                            </div>
                            <div class="mb-3">
                                <label for="amount" class="col-form-label">Amount:</label>
                                <input type="number" class="form-control" id="amount" name="amount"></input>
                            </div>
                            <div class="mb-3">
                                <label for="price" class="col-form-label">Price:</label>
                                <input type="number" class="form-control" id="price" name="price"></input>
                            </div>
                            <div class="mb-3">
                                <label for="power" class="col-form-label">Power:</label>
                                <input type="number" class="form-control" id="power" name="power"></input>
                            </div>
                            <div class="mb-3">
                                <label for="description" class="col-form-label">Description:</label>
                                <textarea class="form-control" id="description" name="description"></textarea>
                            </div>
                        </form>
                    </div>
                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                        <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Product</button>
                    </div>
                </div>
            </div>
        </div>
    ```
    ```html
        <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Product by AJAX</button>
    ```
    Saat tombol ditekan akan men-trigger class container modal dan container dengan id exampleModal.

2. Menambahkan fungsi baru di dalam views.py untuk menambahkan item baru ke dalam basis data
    * Import ```from django.views.decorators.csrf import csrf_exempt``` untuk penggunaan token. 
    * Menambahkan fungsi add_product_ajax: 
        ```python
        @csrf_exempt
        def add_product_ajax(request):
            if request.method == 'POST':
                name = request.POST.get("name")
                amount = request.POST.get("amount")
                price = request.POST.get("price")
                power = request.POST.get("power")
                description = request.POST.get("description")
                user = request.user

                new_product = Items(name=name, amount=amount ,price=price, power=power, description=description, user=user)
                new_product.save()

                return HttpResponse(b"CREATED", status=201)

            return HttpResponseNotFound()
        ```
    * Menambahkan path /add_product_ajax/ ke dalam urls.py yang berada di direktori main:
        ```python
        from main.views import add_product_ajax ...
        urlpatterns = [
            ...
            path('create-product-ajax/', add_product_ajax, name='add_product_ajax'),
        ]
        ```
    * Membuat function script di dalam main.html:
        ```javascript
        function addProduct() {
            fetch("{% url 'main:add_product_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshProducts)

            document.getElementById("form").reset()
            return false
        }
        document.getElementById("button_add").onclick = addProduct
        ```
        Saat tombol Add Product modal ditekan function akan mengambil data yang diisi berdasarkan form tag dengan atribut id form dengan memanggil fungsi add_product_ajax yang berada di views.py dan akan memproses semua data yang sudah diisi di dalam modal, lalu data akan disimpan berdasarkan user yang login ke dalam basis data. 
    
3. Melakukan refresh halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan
    * Membuat function async di dalam main.html:
        ```javascript
        async function refreshProducts() {
            document.getElementById("product_table").innerHTML = ""
            const products = await getProducts()
            let htmlString = `<tr>
                <th>NAME</th>
                <th>PRICE</th>
                <th>POWER</th>
                <th>DESCRIPTION</th>
                <th>Amount</th>
                <th>Qty</th>
                <th>Del</th>
                <th>Edit</th>
            </tr>`
            products.forEach((item) => {
                htmlString += `\n<tr class="lastrow">
                    <td class="column">${item.fields.name}</td>
                    <td class="column">${item.fields.price}</td>
                    <td class="column">${item.fields.power}</td>
                    <td class="column">${item.fields.description}</td>
                    <td class="column">${item.fields.amount}</td>
                    <td class="column">
                        <a href="increment/${item.pk}">
                            <button>
                                +
                            </button>
                        </a>
                        <a href="decrement/${item.pk}">
                            <button>
                                -
                            </button>
                        </a>
                    </td>
                    <td class="column">
                        <a href="delete/${item.pk}">
                            <button>
                                X
                            </button>
                        </a>
                    </td>
                    <td class="column">
                        <a href="edit-product/${item.pk}">
                            <button>
                                Edit
                            </button>
                        </a>
                    </td>
            </tr>` 
            })
            document.getElementById("product_table").innerHTML = htmlString
        }
        refreshProducts()
        ```

    * Saat memanggil function addProduct() pastikan setelah memproses data dari query form akan memanggil function refreshProduct():
        ```javascript
        function addProduct() {
            fetch("{% url 'main:add_product_ajax' %}", {
                method: "POST",
                body: new FormData(document.querySelector('#form'))
            }).then(refreshProducts)
            ...
        }
        ```

## Perbedaan antara Asynchronous Programming dan Synchronous Programming
| Asynchronous Programming | Synchronous Programming | 
| :--------: |:--------:| 
| Dapat melakukan operasi yang lain tanpa harus menunggu operasi sebelumnya selesai | Melakukan operasi secara berurutan operasi lain akan dijalankan ketika operasi yang sedang dilakukan telah selesai |
| Dapat meningkatkan efisiensi dan efektivitas program | Program akan terasa lambat dan tidak responsif |
| Contoh: async/await, callback function, promises, etc | Contoh: blocking programming | 

## Event Driven Programming 
Merupakan paradigma programming yang mengatur sebagai event handler atau penangan suatu peristiwa, seperti menekan button atau melakukan sesuatu yang men-trigger event listener dan bersifat responsif terhadap interaksi pengguna. 

Contoh yang diterapkan dalam tugas ini adalah function addProduct di dalam script tag main.html. Tombol ini akan merespon saat pengguna sudah selesai mengisi data suatu item di dalam modal dan saat menekan tombol Add Product, maka instruksi yang berada dalam function addProduct akan dijalankan. 

## Penerapan asynchronous programming pada AJAX
implementasi function async dan operator await yang menggunakan fetch API untuk mendapatkan data dari function get_product_json secara asinkronus dan blok then() akan memproses data yang diterima. Operator await di sini berperan untuk mengelola data dari kode asinkronus.
```javascript
async function getProducts() {
    return fetch("{% url 'main:get_product_json' %}").then((res) => res.json())
}
```
```javascript
async function refreshProducts() {
    document.getElementById("product_table").innerHTML = ""
    const products = await getProducts()
    ...
}
```

## Kenapa penerapan AJAX pada tugas ini menggunakan fetch API daripada library jQuery
* Dalam tugas ini, data delivery yang digunakan adalah JSON, dengan menggunakan fetch API untuk merespon format data JSON lebih mudah dibanding dengan jQuery.
* Fetch API merupakan build-in dari browser itu sendiri sehingga tidak perlu menambahkan library baru.
* Lebih ringan dan fleksibel karena fetch API hanya akan menggunakan fitur yang akan digunakan saja dan dapat dikonfigurasi dengan mudah. 