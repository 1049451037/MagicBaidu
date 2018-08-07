#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='MagicBaidu',
    version='0.0.9',
    description="A baidu search results crawler",
    install_requires=['beautifulsoup4', 'requests>=2.12.4', 'cchardet'],
    author='Qingsong Lv',
    author_email='lqs@mail.bnu.edu.cn',
    url="https://github.com/1049451037/MagicBaidu",
    packages=find_packages(),
    package_data={'MagicBaidu': ['data/*.txt']},
)
