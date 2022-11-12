# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from __future__ import unicode_literals
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)","Programming Language :: Python :: 3.7","Programming Language :: Python :: 3.8","Programming Language :: Python :: 3.9"],
    description='More HTTP! A few more features atop the Requests library',
    include_package_data=True,
    install_requires=["mo-dots==9.238.22316","mo-files==5.239.22316","mo-future==6.230.22310","mo-json==6.239.22316","mo-kwargs==7.238.22316","mo-logs==7.238.22316","mo-threads==5.241.22316","mo-times==5.239.22316","requests"],
    license='MPL 2.0',
    long_description='# mo-http\n\nMore HTTP! A few more features atop the Requests library\n\n## Overview\n\n* handles large data using streams or temporary files\n* compresses/decompresses automatically \n* try multiple urls \n* retry a number of times with sleeps between\n* reminds you to set headers, so you are a good citizen \n',
    long_description_content_type='text/markdown',
    name='mo-http',
    packages=["mo_http"],
    url='https://github.com/klahnakoski/mo-http',
    version='4.241.22316'
)