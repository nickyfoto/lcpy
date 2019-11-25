"""Minimal setup file for tasks project."""

from setuptools import setup, find_packages

setup(
    name='lcpy',
    version='0.1.0',
    description='Python toolkit for leetcode',

    author='Qiang Huang',
    author_email='nickyfoto@gmail.com',

    packages=find_packages(where='src'),
    package_dir={'': 'src'},

    install_requires=['click'],

    entry_points={
        'console_scripts': [
            'tasks = lcpy.cli:lcpy_cli',
        ]
    },
)
