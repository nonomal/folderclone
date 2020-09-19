from sys import platform
from setuptools import setup,find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
     name='folderclone',
     entry_points={
        'console_scripts': [
            'multimanager=folderclonecli:main',
            'multifolderclone=folderclonecli:main']
    },
     version='1.0.0',
     author='Spazzlo',
     description="Due to changes to Google's APIs, Folderclone is dead.",
     long_description=long_description,
     long_description_content_type='text/markdown',
     url='https://github.com/Spazzlo/folderclone',
     packages=find_packages('src'),
     package_dir={'':'src'},
     install_requires=[],
     classifiers=[
         'Programming Language :: Python :: 3',
         'License :: OSI Approved :: MIT License',
         'Operating System :: OS Independent',
         'Development Status :: 7 - Inactive'
     ]
 )