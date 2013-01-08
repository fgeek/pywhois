from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='whois',
    version=version,
    description="Whois querying and parsing of domain registration information.",
    long_description='',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP'
    ],
    keywords='whois',
    author='Richard Penman',
    author_email='richard@webscraping.com',
    url='http://code.google.com/p/pywhois/',
    license='MIT',
    packages=['pywhois'],
    package_dir={'pywhois':'pywhois'},
    include_package_data=True,
    zip_safe=False,
)
