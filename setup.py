from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='dgi_forms',
    version=version,
    description='App for managing tax forms required by the Minister of Economics and Finance, Panama.',
    author='Leafhat',
    author_email='info@leafhat.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
