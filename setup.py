#from distribute_setup import use_setuptools
#use_setuptools()

from setuptools import setup, find_packages
from os.path import dirname, join
import os

here = dirname(__file__)
setup(
    name='ledgerblue',
	# Bump up the version from 0.1.17 to 0.1.18alpha
	# by Xuesong Hu @ Pit.AI
    version='0.1.18alpha',
    author='Ledger',
    author_email='hello@ledger.fr',
    description='Python library to communicate with Ledger Blue/Nano S',
    long_description=open(join(here, 'README.md')).read(),
    url='https://github.com/LedgerHQ/blue-loader-python',
    packages=find_packages(),
	# Change one required package from pycrypto>=2.6.1 to pycryptodome>=3.6.1
	# by Xuesong Hu @ Pit.AI
    install_requires=['hidapi>=0.7.99', 'protobuf>=2.6.1', 'pycryptodome>=3.6.1', 'future', 'ecpy>=0.8.1', 'pillow>=3.4.0', 'python-u2flib-host>=3.0.2'],
    extras_require = {
	'smartcard': [ 'python-pyscard>=1.6.12-4build1' ]
    },
    include_package_data=True,
    zip_safe=False,
    classifiers=[
	'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Microsoft :: Windows',
	'Operating System :: MacOS :: MacOS X'
    ]
)

