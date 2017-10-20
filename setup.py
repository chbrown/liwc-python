from setuptools import setup

setup(
    name='liwc',
    version='0.3.0',
    url='https://github.com/chbrown/liwc-python',
    description='Linguistic Inquiry and Word Count (LIWC) analyzer (proprietary data not included)',
    long_description=open('README.rst').read(),
    license='MIT',
    author='Christopher Brown',
    author_email='chrisbrown@utexas.edu',
    packages=['liwc'],
    zip_safe=True
)
