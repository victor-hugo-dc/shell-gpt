from setuptools import setup, find_packages

__version__ = "0.0.1"

setup(
    name="shell-gpt",
    packages=find_packages(),
    version=__version__,
    license="MIT",
    description="A chatGPT client on the terminal",
    author="Victor Del Carpio",
    author_email="",
    url="",
    long_description_content_type="text/markdown",
    keywords=[
        "artificial intelligence",
        "generative models",
        "natural language processing",
        "openai",
    ],
    install_requires=[
        "rich",
        "openai",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.11",
    ],
    entry_points={"console_scripts": ["sensei=terminal.chat:main"]},
)