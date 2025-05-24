from setuptools import find_packages, setup

setup(
    name="clio-client-sdk",
    version="0.1.0",
    description="Reusable Clio API client with automatic session and token management.",
    author="Travis Crawford",
    packages=find_packages(),
    install_requires=[
        "python-dotenv",
        "requests",
        "openapi-client",  # replace with actual Clio client package if different
    ],
    python_requires=">=3.7",
)
