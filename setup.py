from setuptools import find_packages
from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

setup(
    name='progeny',
    version='0.1.0',
    description='Simple but powerful management for complex class hierarchies',
    long_description=readme,
    url='https://github.com/GoodRx/progeny',
    author='Lyndsy Simon',
    author_email='lyndsy@goodrx.com',
    license='MIT',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ),
    packages=find_packages('src'),
    package_dir={
        '': 'src',
    },
    install_requires=(
        'six',
    ),
)
