"""
morepath_services
-----
Morepath services demo.
"""

import io
from setuptools import (
    setup,
    find_packages
    )


version = '0.1.0.dev0'

long_description = '\n'.join((
    io.open('README.md', encoding='utf-8').read(),
    io.open('CHANGES', encoding='utf-8').read()
    ))

install_requires = [
    'morepath',
    'more.transaction',
    'more.services',
    'zope.sqlalchemy',
    'sqlalchemy',
    'click',
    'gunicorn'
    ]

tests_require = [
    'pytest',
    'coverage',
    'pytest-cov',
    'webtest'
    ]

docs_require = [
    'sphinx',
    'docutils'
    ]


setup(
    name='morepath_services',
    version=version,
    url='https://github.com/blaflamme/morepath_services',
    license='BSD',
    author='Blaise Laflamme',
    author_email='blaise@laflamme.org',
    description='Morepath services demo.',
    long_description=long_description,
    keywords='morepath service services',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Morepath',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'tests': tests_require,
        'docs': docs_require
        },
    test_suite='morepath_services',
    entry_points={
        'console_scripts': [
            'run-demo = morepath_services.run:run',
            'init-database = morepath_services.cli:initdb'
        ]
    },
    )
