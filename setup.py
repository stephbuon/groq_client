from setuptools import setup, find_packages

setup(
    name="groq_client",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="Your Name",
    author_email="your.email@example.com",
    description="Simple wrapper for querying the Groq API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/groq_client",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires='>=3.6',
)
