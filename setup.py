# -*- coding: utf-8 -*-
# Copyright (c) 2013 Stijn Beauprez & Alejandro Inestal
from distutils.core import setup


setup(
    name='magpie',
    version='0.1',
    maintainer='Stijn Beauprez',
    maintainer_email='stijnbe@gmail.com',
    packages=['magpie', 'magpie.test'],
    package_data={'magpie.test': ['examples/*.*']},
    scripts=['bin/magpie'],
    url='http://pypi.python.org/pypi/magpie/',
    description='AWS cost monitoring and cost cutting tool',
    requires=["boto(>=2.7)", "mysqlConnectorPython"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
    ],
)