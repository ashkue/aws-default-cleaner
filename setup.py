import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='aws-default-cleaner',
    version='1.0.3',
    description='AWS Default Cleaner - default VPC, default subnets, default internet gateway and etc',
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