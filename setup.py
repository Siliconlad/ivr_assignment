from setuptools import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=['ivr_assignment',
              'ivr_assignment.control',
              'ivr_assignment.fusion',
              'ivr_assignment.joints',
              'ivr_assignment.joints.color',
              'ivr_assignment.joints.utils',
              'ivr_assignment.sensor',
              'ivr_assignment.target'],
    package_dir={'': 'src'})

setup(**setup_args)