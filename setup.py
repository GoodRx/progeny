from setuptools import find_packages
from setuptools import setup

setup(
    name='progeny',
    version='0.1.0',
    description='Simple but powerful management for complex class hierarchies',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    required=('six', ),
)
