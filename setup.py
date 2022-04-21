from setuptools import setup
from pathlib import Path

directory = Path(__file__).parent
longDescription = (directory/'README.md').read_text()

setup(
    name='wbsearch',
    version='2.2.1',
    packages=['wbsearch'],
    author_email='cargo.coder@gmail.com',
    author='Cargo',
    description='Search anything on main browser directly from terminal',
    install_requires=['click', 'KvK'],
    long_description=longDescription,
    long_description_content_type='text/markdown',
    entry_points='''
    [console_scripts]
    wbsearch=wbsearch:search
    '''
)
