import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='aws-default-cleaner',
    version='1.0.4',
    description='AWS Default Cleaner - delete default VPCs and associated Subnets, Internet Gateways, Route Tables, Network ACLs and Security Groups',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ashkue/aws-default-cleaner',
    author='Pavel Morshenyuk',
    author_email='ashkue@outlook.com',
    license='MIT',
    scripts=['bin/aws-default-cleaner'],
    install_requires=[
        'click',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])