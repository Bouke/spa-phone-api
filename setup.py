from distutils.core import setup

setup(
    name='spa-phone-api',
    version='0.1.1',
    author='Bouke Haarsma',
    author_email='bouke@webatoom.nl',
    packages=[
        'spa_phone',
    ],
    url='http://github.com/Bouke/spa-phone-api',
    description='Provides an API for Linksys/Sipura VoIP SPA Phones',
    license='MIT',
    long_description=open('README.rst').read(),
    install_requires=[
        'mechanize == 0.2.5',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications :: Internet Phone',
    ]
)
