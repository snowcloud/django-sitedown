from setuptools import setup, find_packages

version = '0.1'

setup(
    name='django-sitedown',
    version=version,
    description=("A simple application for Django"
                 " to effectively take a site offline and display a web page for all URLs except admin."),
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords='utility,django',
    author='Derek Hoy',
    author_email='derek@snowcloud.co.uk',
    url='http://github.com/snowcloud/django-sitedown/',
    license='BSD',
    packages=find_packages(),
    zip_safe=False,
    package_data = {
        'sitedown': [
            'templates/*/*.html',
        ],
    }
)
