from setuptools import setup, find_packages

setup(
    name="logManager",
    version="1.0.4",
    author="Mark Hendriksen",
    author_email="your.email@example.com",  # Replace with your email
    description="A thread-safe logging manager for Python applications",
    long_description=open("README.md").read() if open("README.md", "r").readable() else "A thread-safe logging manager for Python applications",
    long_description_content_type="text/markdown",
    url="https://github.com/hendriksen-mark/logManager",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        # Add any dependencies your package needs
    ],
)
