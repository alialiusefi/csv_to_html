from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='sample',
    version='0.1.0',
    description='Sample package for Python-Guide.org',
    long_description=readme,
    author='Ali Al-Iusefi',
    author_email='alighanem99@live.com',
    url='',
    license="none yet",
    packages=find_packages(exclude=('tests', 'docs'))
)
