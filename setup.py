"""
Setup script for AI-Powered Compound Disaster Risk Assessment System
"""

from setuptools import setup, find_packages

setup(
    name="compound-disaster-analytics",
    version="1.0.0",
    author="Abayomi Ajayi",
    author_email="ajayi.abayomi5@gmail.com",
    description="AI-Powered Compound Disaster Risk Assessment System for Emergency Management",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Abayommy/Compound-Disaster-Analytics",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "emergency management", "disaster risk assessment", 
        "compound disasters", "heat waves", "flood prediction",
        "artificial intelligence", "FEMA", "public safety"
    ],
)
