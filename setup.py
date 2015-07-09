import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-mptt-comments',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    description='Django Mptt Comments is a simple way to display threaded comments instead of the django contrib comments.',
    long_description=README,
    url='https://github.com/hovel/django-mptt-comments',
    author='fivethreeo',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
