import sys
from distutils.core import setup
from setuptools import find_packages

if sys.platform == 'win32':
    import py2exe
    extra_options = dict(
        setup_requires=['py2exe'],
        options=dict(
            py2exe=dict(
                excludes=['spa_sync.providers.contacts',],
                compressed=2,
                bundle_files=1,
            ),
        ),
        console=[
            dict(
                script='main.py',
                dest_base='spa_sync',
                description='Command prompt utility to sync SPA phones',
            ),
        ],
        zipfile=None,
    )
else:
    extra_options = dict()

setup(
    name='spa-phone-api',
    version='0.3.0',
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
    ],
    **extra_options
)
