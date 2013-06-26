import sys
major, minor = sys.version_info[0:2]
if major != 2 or minor < 6:
    print 'Magpie requires Python 2.6.x or 2.7.x'
    sys.exit(1)

from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

import magpie

with open('requirements.txt') as fh:
    requires = [requirement.strip() for requirement in fh]

entry_points = {
    'console_scripts': [
        'magpie = magpie.cli:run',
    ],
}

exclude_packages = [
    'tests',
    'tests.*',
]

package_data = {'': ['default_conf/*.yml']}

# py2.6 compatibility
try:
    import argparse
except ImportError:
    requires.append('argparse')

try:
    from collections import OrderedDict
except ImportError:
    requires.append('ordereddict')

setup(
    name='magpie',
    version=magpie.__version__,
    description='Magpie: Monitor and cut AWS costs',
    author='Magpie team',
    author_email='stijnbe@gmail.com',
    url='https://github.com/ainestal/magpie.git',
    packages=find_packages(exclude=exclude_packages),
    package_data=package_data,
    package_dir={'magpie': 'magpie'},
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
    entry_points=entry_points,
    license='ASL 2.0',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Installation/Setup',
        'Topic :: Utilities',
    ),
)
