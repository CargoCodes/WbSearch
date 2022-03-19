from setuptools import setup
from pathlib import Path

directory = Path(__file__).parent
README = (directory / "README.md").read_text()

setup(
    name='wbsearch',
    author='Cargo',
    version='1.1.2',
    packages=['wbsearch'],
    install_requires=['click', 'KvK'],
    license='MIT',
    long_description=README,
    entry_points='''
    [console_scripts]
    wbsearch=wbsearch:search
    '''
)
