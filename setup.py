from setuptools import setup, find_packages
import os
import os.path
import sys

if sys.version[0] == '2':
    sys.exit('Use Python 3')

requires = [
'asciimatics==1.11.0',
'certifi==2019.11.28',
'chardet==3.0.4',
'feedparser>=5.2.1',
'future==0.18.2',
'idna==2.9',
'oauthlib==3.1.0',
'Pillow>=7.0.0',
'pyfiglet==0.8.post1',
'PySocks==1.7.1',
'requests>=2.23.0',
'requests-oauthlib==1.3.0',
'six==1.14.0',
'tweepy==3.8.0',
'urllib3>=1.26.6',
'wcwidth==0.1.8',
]

setup(name='rterm',
      version='1.4a',
      description='Twitter and RSS reader client for CLI',
      long_description=open("./README.rst", "r").read(),
      classifiers=[
          'Environment :: Console',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.7',
      ],
      keywords='twitter, RSS, CLI, command line, terminal',
      author='Lee JunHaeng',
      author_email='rainygirl@gmail.com',
      url='https://github.com/rainygirl/rterm',
      license='MIT License',
      packages=find_packages(exclude=[]),
      python_requires='>=3.7',
      zip_safe=False,
      install_requires=requires,
      entry_points='''
      # -*- Entry points: -*-
      [console_scripts]
      rterm=rterm_src.run:do
      ''',
      )
