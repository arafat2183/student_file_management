Here we will follow the steps to set up the project.

1.To set up the backend environment now we need the following:
    - django
    - django rest framework
    - virtual environment

2.We have to create a virtual environment first to install the package or library. Do not forget to add the name on gitignore if you have changed the name of the virtual environment
    - python -m venv venv
3.Now we have to activate the virtual environment to install the package or library on it. The command will be as below.
    - venv\Scripts\activate (To activate)
    - deactivate (To deactivate)

For Mac : source package_config/bin/activate

4.we can save all the information on a file named requirements.txt. All the required package are written here. Please run the file and install them.
    - pip install -r requirements.txt
    - pip uninstall package_name (to uninstall any package)

    - brew install mysql pkg-config (for mac)
    - pip install mysqlclient (for mac)

5.First we have to create a new django project using the following command
    - django-admin startproject sfm

6.After that we have to create app. To create app we have to use the following command
    - python manage.py startapp student_profile

7.After adding the app we have to register that on the main_app/settings.py file. There will be an array named INSTALLED_APPS. We will add 'rest_framework' and 'company' there.
8.If we want to use mysql database with django, so we have to use the package name sqlparse what is already added to the requirements.txt file. So now we have to add the database credentials on the main_app/settings.py file.
There will be an array named DATABASES. The following information will add there.

MySql Client Install Command for Mac
brew install mysql-client

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'mydb',
		'USER': 'root',
		'PASSWORD': 'admin',
		'HOST':'localhost',
		'PORT':'3306',
	}
}


