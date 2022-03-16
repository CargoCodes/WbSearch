from setuptools import setup

setup(
    name='wbsearch',
    author='Cargo',
    version='1.1.2',
    packages=['wbsearch'],
    install_requires=['click', 'KvK'],
    entry_points='''
    [console_script]
    wbsearch=wbsearch:search
    '''
)
