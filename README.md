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
* Ubuntu: 16.04, 18.04
* Debian: 8,9
* CeontOS/RHEL: 6,7

Other operating systems or versions may work but have not been tested.

## Usage

### Default behaviour

By default this role adds the official [Icinga Repository](https://packages.icinga.com) to the system and installs the
`icinga2` package.

``` yaml
- name: Default Example
  hosts: localhost
  roles:
    - icinga2
```

### Disable repository management

You may choose to use your own or the systems default repositories. Repository management can be disabled:

``` yaml
- name: Example without repository
  hosts: all
  roles:
    - icinga2
  vars:
    - i2_manage_repository: false
```

## Reference

- [**Variables**](#variables)
    - [Variable: i2_manage_repository](#variable-i2_manage_repository)
    - [Variable: i2_manage_package](#variable-i2_manage_package)
    - [Variable: i2_manage_service](#variable-i2_manage_service)
    - [Variable: i2_apt_key](#variable-i2_apt_key)
    - [Variable: i2_apt_url](#variable-i2_apt_url)
    - [Variable: i2_i2_yum_key](#variable-i2_yum_key)
    - [Variable: i2_i2_yum_url](#variable-i2_yum_url)
- [**Handlers**](#handlers)
    - [Handler: start icinga2](#handler-start-icinga2)

### Variables

#### Variable: `i2_manage_repository`
Whether to add the official [Icinga Repository](https://packages.icinga.com/) to the system or not. Defaults to `true`.

#### Variable: `i2_manage_package`
Whether to install packages or not. Defaults to `true`.

#### Variable: `i2_manage_service`
Whether to start, restart and reload the Icinga 2 on changes or not. Defaults to `true`.

#### Variable: `i2_apt_key`
GPG key used to verify packages on APT based system. The key will be imported. Defaults to
`https://packages.icinga.com/icinga.key`.

#### Variable: `i2_apt_url`
Repository URL for APT based systems. Defaults 
to `deb http://packages.icinga.com/{{ ansible_distribution|lower }} icinga-{{ ansible_distribution_release }} main`.
This may be customized if you have a local mirror.

#### Variable: `i2_yum_key`
GPG key used to verify packages on YUM based sytems. The key URL will be added to the repository file. Defaults to
`https://packages.icinga.com/icinga.key`.

#### Variable: `i2_yum_url`
Repository URL for YUM based sytem. Defaults to `http://packages.icinga.com/epel/$releasever/release/`. This may be
customized if you have a local mirror.

### Handlers

#### Handler: `start icinga2`
This handler starts Icinga 2. It is only used to make sure Icinga 2 is running. You can prevent this handler from
being triggerd by setting `i2_manage_service` to false.

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
