import os
from setuptools import setup

readme_path = os.path.join(os.path.dirname(
  os.path.abspath(__file__)),
  'README.rst',
)
long_description = open(readme_path).read()

setup(
  name='flask-phantom-emoji',
  version='0.1.2',
  packages=['flask_phantom_emoji'],
  author="Nick Whyte",
  author_email='nick@nickwhyte.com',
  description="Add phantom emoji's to your flask application",
  long_description=long_description,
  url='https://github.com/nickw444/flask-phantom-emoji',
  include_package_data=True,
  zip_safe=False,
)
