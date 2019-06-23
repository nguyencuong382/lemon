from setuptools import setup, find_packages
from pip.req import parse_requirements

# parse_requirements() returns generator of pip.req.InstallRequirement objects
install_reqs = parse_requirements('./lemon/requirements.txt')

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
reqs = install_reqs

setup(name='lemon',
      version='0.1',
      description='your mood analyzer',
      author='mp',
      author_email='hello@micropyramid.com',
      license='MIT',
      install_requires=reqs,
      packages=find_packages(),
      entry_points={
          'console_scripts': ['lemon=lemon.task:main'],
      },
      zip_safe=False
      )
