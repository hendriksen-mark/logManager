"""
setup.py for logManager
"""
from setuptools import setup

def readme():
    """Read the README.md file for the long description."""
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()

setup(
    name="logManager",
    version="1.1.4",
    author="Mark Hendriksen",
    author_email="your.email@example.com",  # Replace with your email
    description="A thread-safe logging manager for Python applications",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/hendriksen-mark/logManager",
    packages=['logManager'],
    package_dir={'logManager': 'log_manager'},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3.14",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[
        "colorlog>=6.0.0"
    ],
)
