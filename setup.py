from distutils.core import setup
from setuptools import find_packages

setup(
    name='spa-phone-api',
    version='0.2.2',
    author='Bouke Haarsma',
    author_email='bouke@webatoom.nl',
    packages=find_packages(),
    url='http://github.com/Bouke/spa-phone-api',
    description='Provides an API for Linksys/Sipura VoIP SPA Phones',
    license='MIT',
    long_description=open('README.rst').read(),
    install_requires=[
        'mechanize == 0.2.5',
    ],
    entry_points={
        'console_scripts': [
            'spa-sync = spa_sync:main',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Internet Phone',
    ]
)
