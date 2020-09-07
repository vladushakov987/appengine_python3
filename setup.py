from setuptools import setup, find_packages

version = '1.9.15'

setup(
  name='python3-appengine',
  version=version,
  author='Jon San Miguel',
  author_email='jon.sanmiguel@optimizely.com',
  packages=find_packages(),
  include_package_data=True,
  url='https://github.com/vladushakov987/appengine_python3',
  download_url='https://github.com/vladushakov987/appengine_python3',
  license='Apache License',
  description='GAE SDK Pip installable Mirror',
  long_description=open('README').read(),
  keywords=['google', 'appengine'],
)
