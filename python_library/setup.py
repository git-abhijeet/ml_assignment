"""
Setup script for MLMath library installation.
"""

from setuptools import setup, find_packages

# Read the README file for long description
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A custom Python library for machine learning mathematics"

setup(
    name="mlmath",
    version="1.0.0",
    author="GitHub Copilot",
    author_email="copilot@github.com",
    description="A custom Python library for machine learning mathematics",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/mlmath",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies - pure Python implementation
    ],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    keywords="machine learning, mathematics, linear algebra, probability, vectors, matrices",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/mlmath/issues",
        "Source": "https://github.com/yourusername/mlmath",
        "Documentation": "https://github.com/yourusername/mlmath/wiki",
    },
)
