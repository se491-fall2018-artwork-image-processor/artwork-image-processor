# Artwork Image Processor

This is a Django application that leverages a Deep Neural Net to transfer painting styles onto images.

The application also reaches out to the [PhotoTagger API](https://github.com/PhotoTagger/django-initial#api) to tag any uploaded images with classifcations based on what is in the image (Ex: dog, train, car, etc)

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

These are the Python dependencies required to build and run the application:
```
Python 3.6.6
Django 2.1.2
Bootstrap 4.1.3
Pillow 5.3.0
Numpy 1.14.5
Gunicorn 19.9.0
Whitenoise 4.1
Dj Database URL 0.5.0
requests 2.20.0
imutils 0.5.1
Scipy 1.1.0
OpenCV 3.4.3.18
```

### Installing your Development Environment

1. Install all dependencies noted above
2. Navigate to the project root in your command line / terminal 
3. Execute the `migrate` command to create any necessary database tables
  - Ex: `python manage.py migrate` 
4. Execute the `collectstatic` command to populate the `staticfiles` directory
  - Ex: `python manage.py collectstatic`
5. Execute the `runserver` command to start the development server 
  - Ex: `python manage.py runserver <port>` 
  - The `runserver` command defaults to port `8000`
6. In a browser, navigate to `http://localhost:<port>` to load the root webpage

### Configuring PhotoTagger API Endpoint
The PhotoTagger API endpoint can be configured by setting the `PHOTOTAGGER_CLASSIFY_API_ENDPOINT` variable in `settings.py`


## Automated Test Suite

The project has a suite of automated tests that are built on top of the Django test framework, which is built on top of the **unittest** module built in to the Python standard library.

### Test Files 

The project's automated tests are defined in the following files:

| Test File                                                          | Description                                                |
|--------------------------------------------------------------------|------------------------------------------------------------|
| &lt;project_root&gt;/artwork_image_processor/tests/tests_forms.py  | Tests validating Django forms in the project               |
| &lt;project_root&gt;/artwork_image_processor/tests/tests_models.py | Tests validating Django models in the project              |
| &lt;project_root&gt;/artwork_image_processor/tests/tests_views.py  | Tests validating Django views in the project               |
| &lt;project_root&gt;/artwork_image_processor/tests/tests_style.py  | Tests validating the Image Processing logic in the project |
| &lt;project_root&gt;/artwork_image_processor/tests/tests_tags.py  | Tests validating the Photo Tagger API Integration logic in the project |

### Running the tests

Run the following commands to execute the test suite:

```
python manage.py test
```

The test suite is also run automatically as part of our pull-request process. A PR **cannot** be merged unless **all** tests are passing.

### Generating a Code Coverage Report

A code coverage report can be generated using the `Coverage.py` utility for python. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.

Coverage.py can be installed using `pip` or other python dependency management frameworks. Ex: `pip install coverage`

Run the following commands at the project root to build and view the code coverage report for this project:
```
coverage run --source='.' manage.py test
coverage report
```

## Deployment

Our current deployment environment is Heroku. We have a CI/CD Pipeline that will automatically deploy changes that are successfully merged into the **master** branch. 
* Our live URL is: [https://art-processor.herokuapp.com/](https://art-processor.herokuapp.com/)

The primary distinction between running the application locally vs in a deployment environment involves the management of the project's static files. We have configured the application to successfully deploy to our Heroku deployment environment, but there may be additional requirements in other deployment environments.

For additional information on how to handle static files when deploying Django applications, see the following links:
* [Django - Managing Static Files](https://docs.djangoproject.com/en/2.1/howto/static-files/)
* [Django - Deploying Static Files](https://docs.djangoproject.com/en/2.1/howto/static-files/deployment/)
* [Heroku - Django and Static Assets](https://devcenter.heroku.com/articles/django-assets)

## Monitoring

We are currently using two different monitoring solutions for our deployments:
* [FreshPing - Uptime Monitoring](https://statuspage.freshping.io/1886-ArtProcessor/check/19770)
* [New Relic APM](https://newrelic.com/)

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

* **Cecil Beeland** - *Initial work* - [beelandc](https://github.com/beelandc)
* **Camille Rosewright** - *Initial work* - [kamiyokamiru](https://github.com/kamiyokamiru)
* **Wunyan Wong** - *Initial work* - [wunyanw](https://github.com/wunyanw)
* **Greg Zimmerman** - *Initial work* - [gjz999gitit](https://github.com/gjz999gitit)


See also the list of [contributors](https://github.com/se491-fall2018-artwork-image-processor/artwork-image-processor/graphs/contributors) who participated in this project.

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* For inspiration: 
  * [Udacity - How to Process Images With TensorFlow - by Mat Leonard](https://blog.udacity.com/2018/04/how-to-process-images-with-tensorflow.html) 
  * [How to Upload Files with Django - by Vitor Freitas](https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html)
  * [Neural Style Transfer with OpenCV - by Adrian Rosebrock](https://www.pyimagesearch.com/2018/08/27/neural-style-transfer-with-opencv/)
* 

