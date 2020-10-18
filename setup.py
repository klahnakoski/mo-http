# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from __future__ import unicode_literals
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)"],
    description='More HTTP! A few more features atop the Requests library',
    include_package_data=True,
    install_requires=["mo-dots>=3.93.20259","mo-files>=3.92.20258","mo-future>=3.89.20246","mo-json>=3.93.20259","mo-kwargs>=3.93.20259","mo-logs>=3.99.20292","mo-threads>=3.99.20292","mo-times>=3.76.20190","requests"],
    license='MPL 2.0',
    long_description='# mo-http\n\nMore HTTP! A few more features atop the Requests library\n\n## Overview\n\n* handles large data using streams or temporary files\n* compresses/decompresses automatically \n* try multiple urls \n* retry a number of times with sleeps between\n* reminds you to set headers, so you are good citizen \n',
    long_description_content_type='text/markdown',
    name='mo-http',
    packages=["mo_http"],
    url='https://github.com/klahnakoski/mo-http',
    version='3.99.20292'
)