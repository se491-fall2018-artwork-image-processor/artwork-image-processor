# Artwork Image Processor

This is a Django application that leverages the Tensorflow library to transfer painting styles onto images.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

These are the Python dependencies required to build and run the application:
```
Python 3.6.6
Django 2.1.2
Tensorflow 1.11
Bootstrap 4.1.3
Pillow 5.3.0
Numpy 1.14.5
Gunicorn 19.9.0
Whitenoise 4.1
Dj Database URL 0.5.0
```

### Installing your Development Environment

1. Install all dependencies noted above
2. Navigate to the project root in your command line / terminal 
3. Execute the `runserver` command to start the development server 
  - Ex: `python manage.py runserver <port>` 
  - The `runserver` command defaults to port `8000`
4. In a browser, navigate to `http://localhost:<port>' to load the root webpage

## Automated Test Suite

The project has a suite of automated tests that are built on top of the Django test framework, which is built on top of the *unittest* module built in to the Python standard library.

### Test Files 

The project's automated tests are defined in the following files:

| Test File                                                          | Description                                                |
|--------------------------------------------------------------------|------------------------------------------------------------|
| &lt;project-root&gt;/artwork_image_processor/tests/tests_forms.py  | Tests validating Django forms in the project               |
| &lt;project-root&gt;/artwork_image_processor/tests/tests_models.py | Tests validating Django models in the project              |
| &lt;project-root&gt;/artwork_image_processor/tests/tests_views.py  | Tests validating Django views in the project               |
| &lt;project-root&gt;/artwork_image_processor/tests/tests_style.py  | Tests validating the Image Processing logic in the project |

### Running the tests

Run the following commands to execute the test suite:

```
python manage.py test
```

The test suite is also run automatically as part of our pull-request process. A PR *cannot* be merged unless *all* tests are passing.

## Deployment

TODO: Add additional notes about how to deploy this on a live system

## Contributing

TODO: Create Contribution Guidelines

Ex:
Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

TODO: Create Versioning Guidelines
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Cecil Beeland** - *Initial work* - [beelandc](https://github.com/beelandc)
* **Camille Rosewright** - *Initial work* - [kamiyokamiru](https://github.com/kamiyokamiru)
* **Wunyan Wong** - *Initial work* - [wunyanw](https://github.com/wunyanw)
* **Greg Zimmerman** - *Initial work* - [gjz999gitit](https://github.com/gjz999gitit)


See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the GPL 3.0 License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

TODO
* Hat tip to anyone whose code was used
* Inspiration
* etc

