import codecs
from setuptools import find_packages
from setuptools import setup

install_requires = []

test_requires = []

setup(
    name="pfrl",
    version="0.3.0",
    description="PFRL, a deep reinforcement learning library",
    long_description=codecs.open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Yasuhiro Fujita",
    author_email="fujita@preferred.jp",
    license="MIT License",
    packages=find_packages(),
    install_requires=install_requires,
    test_requires=test_requires,
)
