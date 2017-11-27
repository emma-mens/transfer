# setup.py
from setuptools import setup, find_packages

setup(name='fast',
  version='0.1',
  packages=find_packages(),
  description='run fast style transfer on gcloud ml-engine',
  author='Emmanuel Azuh',
  author_email='emazuh@mit.edu',
  license='MIT',
  install_requires=[
      'Pillow',
  ],
  zip_safe=False)
