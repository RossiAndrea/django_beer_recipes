from setuptools import setup, find_packages
from beer_recipes import __version__

setup(
    name='Django Beer Recipes',
    version=__version__,
    author='Andrea Rossi',
    author_email='direlemming+github@gmail.com',
    description='Beer recipes in Django made easy!',
    url='https://github.com/RossiAndrea/django_beer_recipes',
    packages=find_packages(),
    include_package_data=True,
    setup_requires=[
        'setuptools_git>=0.3',
    ],
    install_requires=[
        'django>=1.5.1'
    ],
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
