from setuptools import setup, find_packages

setup(
    name='multi-time-series-connectedness',
    version='0.1.0',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        # List your project's dependencies here.
        # Example: 'requests>=2.20.0',
    ],
    author='Victor Chen',
    author_email='victor.yccchen1@gmail.com',
    description='This package provides a framework for measuring connectedness among multiple time series.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YCChenVictor/MultiTimeSeries_Connectedness',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
