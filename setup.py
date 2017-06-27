from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

setup(
    name='ckanext-mdfromowl',
    version=version,
    description="Metadata properties from owl",
    long_description="""
    """,
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='UPM - OEG',
    author_email='jfbaculima@delicias.dia.fi.upm.es',
    url='',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points=\
    """
    [ckan.plugins]
    mdfromowl=ckanext.repeating.plugins:MDfromowlPlugin
    """,
)
