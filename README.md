[![Build Status](https://api.travis-ci.org/Icinga/ansible-icinga2.svg?branch=master)](https://travis-ci.org/Icinga/ansible-icinga2)

# Icinga 2 Role for Ansible

Ansible role to install and configure [Icinga 2](https://www.icinga.com/products/icinga-2/).

## Setup

``` bash
$ ansible-galaxy install icinga.icinga2
```

### Limitations

The role is supported on the following platforms:

* Icinga 2 >= v2.8
* Ubuntu: 14.04, 16.04
* Debian: 8,9
* CeontOS/RHEL: 6,7

Other operating systems or versions may work but have not been tested.

## Development
A roadmap of this project is located at https://github.com/Icinga/ansible-icinga2/milestones. Please consider this
roadmap when you start contributing to the project.

### Contributing
When contributing several steps such as pull requests and proper testing implementations are required. Find a detailed
step by step guide in [CONTRIBUTING.md](CONTRIBUTING.md).

### Testing
Testing is essential in our workflow to ensure a good quality. We use Molecule to test all
components of this role. For a detailed description see [TESTING.md](TESTING.md).

## Release Notes
When releasing new versions we refer to [SemVer 1.0.0](http://semver.org/spec/v1.0.0.html) for version numbers. All steps required when creating a new
release are described in [RELEASE.md](RELEASE.md)

See also [CHANGELOG.md](CHANGELOG.md)

## Authors
[AUTHORS](AUTHORS) is generated on each release.