# Discuss

A functional hacker news clone. Has the ability for users to sign up and post URLs that can get voted on and commented on one layer deep. Includes a captcha through a third party package.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Installing

A step by step series of examples that tell you have to get a development env running

1. Create a virtualenv for the project
2. Install the requirements.txt file with pip
```
pip install -r requirements.txt
```

3. Run the django server

```
python ./manage.py runserver
```

4. Enjoy the site at 127.0.0.1:8000 or your corresponding localhost

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [django-recaptcha](https://github.com/praekelt/django-recaptcha) - Library to slow down spam
* [DJango Project Blueprints](https://www.packtpub.com/web-development/django-project-blueprints)

## Contributing

Feel free to make PRs or Issues on things that need doing.

# License

This project is licensed under the MIT License
