try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup

setup(
    name='transcribeme',
    version='0.0.1',
    author='Caleb Tutty',
    author_email='caleb@prettymint.co.nz',
    packages=['transcribeme', 'transcribeme.tests'],
    url='http://github.com/tuttinator/transcribeme-py',
    license='LICENSE.txt',
    description='TranscribeMe SOAP API wrapper',
    test_suite='transcribeme.tests.get_suite'
)