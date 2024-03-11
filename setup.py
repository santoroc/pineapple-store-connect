from setuptools import setup, find_packages

setup(
    name='pineapple-store-connect',
    version='0.1.0',
    packages=find_packages(),
    license='MIT',
    author='Carlos Santoro',
    description='Defines a python API to simplify connecting in App Store Connect.',
    long_description='This Python SDK simplifies the process of connecting to the App Store Connect API for reporting purposes. It provides a streamlined interface for downloading sales and subscription reports, eliminating the need for manual HTTP logic and API parameter handling. With this SDK, you can focus on your data, not the details of API interaction.',
    setup_requires=['wheel']
)