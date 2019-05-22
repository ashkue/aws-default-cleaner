from setuptools import setup

setup(name='aws-default-cleaner',
      version='1.0',
      description='AWS Default Cleaner - default VPC, default subnets, default internet gateway and etc',
      url='https://github.com/ashkue/aws-default-cleaner',
      author='Pavel Morshenyuk',
      author_email='ashkue@outlook.com',
      license='MIT',
      scripts=['bin/aws-default-cleaner'],
      zip_safe=False)