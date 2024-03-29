"""setup file for lcpy project."""

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
            'lcpy = lcpy.cli:lcpy_cli',
        ]
    },
)
