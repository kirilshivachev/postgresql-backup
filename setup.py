from setuptools import find_packages, setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name = 'pgbackup',
    version = '0.1.0',
    author = 'Kiril Shivachev',
    author_email = 'kirilshivachev@gmail.com',
    descriptiopn = 'A utility for backing up posgresql databases',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/kirilshivachev'
    packages = find_packages('src')
)