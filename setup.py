# -*- coding: utf-8 -*-


from setuptools import setup

setup(name='hyapi',
      version='0.0.1',
      description='Python SDK for Hanyang Univ API',
      url='https://github.com/HYLionLab/hyapi.git',
      author='Lionlab',
      author_email='admin@lionlab.io',
      license='MIT',
      packages=['hyapi'],
      zip_safe=False,
      install_requires=[
        'pycrypto',
        'requests'
      ],
      keywords='Hanyang University',
      classifiers=[
        'Development Status :: 3 - Pre-Alpha',
        'Topic :: Software Development :: Libraries',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
      ])
