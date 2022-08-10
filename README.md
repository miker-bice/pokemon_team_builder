
# Pokemon random Team Generator using PokeAPI built with Python and Django

Want to be a Pokemon trainer? Well you can easily
generate your own team using this web app. Who doesn't
want those cute Pokemons?




## Requirements
* [requests](https://pypi.org/project/requests/)
* [python3.xx latest](https://www.python.org/)

To install these packages, just run
```bash
  pip install package_name
```

## Installation and Running Locally

After cloning the project, it is recommended to 
create a virtualenv by following these steps:

```bash
  cd ProjectDirectory
```

Now after changing cd to the this repository's folder
you can now create a virtual environment. The 'myEnv'
is your preferred folder name for your virtual environment.

```bash
  py -m venv myEnv
```

After creating a virtual environment, you might want
to activate it first by doing the following commands:

```bash
  source myEnv/Scripts/activate
```
After activating the virtual environment, you must see
an indicator in your terminal which signals that your
virtual environment is already activated and running.

This is the only time that you can install the requirements
like **django** and **requests**. This command will both
install the said this project.

```bash
  pip install django requests
```

After installation, you might want to try and make a
**migration**

```bash
  py manage.py makemigrations
  py manage.py migrate
```

After successful migrations to database, you can now
test run the app using the command

```bash
  py manage.py runserver
```
## Tech Stack

**Python3.xx latest** 

