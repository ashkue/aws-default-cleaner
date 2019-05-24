# Introduction

`aws-default-cleaner` is a command line tool to delete default AWS account resources:

- VPCs
- Subnets
- Internet Gateways
- Route Tables
- Network ACLs
- Security Groups

# Installation

Install package using [pip](https://pypi.org/project/aws-default-cleaner/) package-manager

``` shell
pip install aws-default-cleaner
```

# Usage

## Basic usage

Currently this tool supports two operations: `discover` and `delete`.

- `discover` command searches for default VPCs and other resources in the AWS account and outputs ids (no objects deleted)
- `delete` command tries to delete default VPCs and associated Subnets, Internet Gateways, Route Tables, Network ACLs and Security Groups

Example:
``` shell
aws-default-cleaner discover
aws-default-cleaner delete
```

## Assuming role

When you use multi-account setup with central IAM account and specific roles in spoke accounts, you can force `aws-default-cleaner` to assume role before performing any operations. Simply supply one or more `--assume` or `-a` flags with the corresponding role names.

Example:
``` shell
aws-default-cleaner discover -a arn:aws:iam::account-one-id:role/infra-admin-assumerole -a arn:aws:iam::account-two-id:role/infra-admin-assumerole
aws-default-cleaner delete -a arn:aws:iam::XXXXXXXXXXXX:role/infra-admin-assumerole
```

## Region filtering

By default `aws-default-cleaner` will search for the default resources in the all available regions, but you can override this behavior by supplying `--region` or `-r` flags.

Example:
``` shell
aws-default-cleaner discover -r eu-central-1 -r eu-west-3
aws-default-cleaner delete -r eu-central-1 -r eu-west-3
```
