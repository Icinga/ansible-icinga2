**Attention: This role is no longer maintained.** See: https://github.com/Icinga/ansible-collection-icinga

# Icinga 2 Role for Ansible

Ansible role to install and configure [Icinga 2](https://www.icinga.com/products/icinga-2/).



The scope of this role is to handle the installation and configuration of Icinga 2. In the future it will be possible to configure Icinga as master, satellite or agent. This role handles only Icinga 2 and not any third-party software (like databases, nrpe, UI etc.). The installation and configuration of Icinga Web 2 is currently not part of this role.

The role is supported on the following platforms:

- Ansible >= v2.8
- Icinga 2 >= v2.8
- Ubuntu: 18.04, 20.04
- Debian: 9, 10
- CentOS/RHEL: 7, 8

Other operating systems or versions may work but have not been tested.  
Platform support may be extended after a v1.0 release.

## Installation

Using `ansible-galaxy`:

```bash
ansible-galaxy install icinga.icinga2
```

Using `requirements.yml`:

```yaml
---

- src: icinga.icinga2
```

## Requirements

Prerequisites that you may need, but are not covered by this role:

- Database (MySQL/MariaDB/Postgres)
- Web UI (icingaweb2)
- NRPE

## Role Configuration

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

### Variables

#### Variable: `i2_manage_repository`

Whether to add the official [Icinga Repository](https://packages.icinga.com/) to the system or not. Defaults to `true`.

#### Variable: `i2_manage_package`

Whether to install packages or not. Defaults to `true`.

#### Variable: `i2_manage_epel`

Whether to install the EPEL release package. Defaults to `true`.

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

#### Variable: `i2_confd`

By default, configuration located in `/etc/icinga2/conf.d` is included. This list may be modified to include additional directories or set to `[]` to not include `conf.d` at all (e.g. on distributed installations).
Defaults to `[ "conf.d" ]`.

#### Variable: `i2_include_plugins`

The [ITL](https://www.icinga.com/docs/icinga2/latest/doc/10-icinga-template-library/) comes with a set of
pre-configured check commands. This variable defines what to include. Defaults to
`["itl", "plugins", "plugins-contrib", "manubulon", "windows-plugins", "nscp"]`

#### Variable: `i2_const_plugindir`

Set `PluginDir` constant. Defaults to `{{ i2_lib_dir }}/nagios/plugins`.

#### Variable: `i2_const_manubulonplugindir`

Set `ManubulonPluginDir` constant. Defaults to `{{ i2_lib_dir }}/nagios/plugins`.

#### Variable: `i2_const_plugincontribdir`

Set `PluginContribDir` constant. Defualts to `{{ i2_lib_dir }}/nagios/plugins`.

#### Variable: `i2_const_nodename`

Set `NodeName` constant. Defaults to `{{ ansible_fqdn }}`.

#### Variable: `i2_const_zonename`

Set `ZoneName` constant. Defaults to `{{ ansible_fqdn }}`.

#### Variable: `i2_const_ticketsalt`

Set `TicketSalt` constant. Empty by default.

#### Variable: `i2_custom_constants`

Add custom constants to `constants.conf`. Must be a dictionary. Defaults to: `{}`

Some default required values are specified in `i2_default_constants` and merged with this variable. Use this variable to override these default values, or add your own constants.

Default values of `i2_default_constants`:

```yaml
  PluginDir: "{{ i2_lib_dir }}/nagios/plugins"
  ManubulonPluginDir: "{{ i2_lib_dir }}/nagios/plugins"
  PluginContribDir: "{{ i2_lib_dir }}/nagios/plugins"
  NodeName: "{{ ansible_fqdn }}"
  ZoneName: "{{ ansible_fqdn }}"
  TicketSalt: ""
```

Example usage:

```yaml
  vars:
    - i2_constants:
        TicketSalt: "My ticket salt"
        Foo: "bar"
```

#### Variable: `i2_zones`

Replaces `zones.conf` with configured zones.

Example:

```yaml
  vars:
    i2_zones:
      - name: master
        is_parent: true
        endpoints:
          - name: master1.example.tom
            host: master1.example.tom
            port: 15667
          - name: master2.example.tom
            host: 128.0.0.1
          - name: global-templates
            is_global: true
          - name: director-global
            is_global: true
```

is_parent = sets the parent zone to this zonename (optional).
is_global = sets the zone to a global zone (optional).
host = sets the host ip/fqdn to connect to this endpoint (optional).
port = sets the port (optional). Defaults to 5665. Requires host do be set.

### System specific variables

The following variables are system specific and don't need to be overwritten in most cases. Be careful when making
changes to any of these variables.

#### Variable: `i2_conf_dir`

Base Icinga 2 configuration directory. Defaults to `/etc/icinga2`.

#### Variable: `i2_user`

Icinga 2 running as user. Default depends on OS.

#### Variable: `i2_group`

Icinga 2 running as group. Default depends on OS.

#### Variable: `i2_lib_dir`

Lib dir. Default depends on OS.

### Feature Usage

#### Variable: `i2_custom_features`

Features are maintained over the dictionary `i2_custom_features`.
By default features won't be managed until `i2_custom_features` has further values.

Example usage:

```yaml
vars:
  i2_custom_features:
    ApiListener:                #ObjectType
      api:                      #ObjectName
        accept_command: true    #ObjectAttribute
        accept_config: true     #ObjectAttribute
    GraphiteWriter:
      graphite:
        host: "127.0.0.1"
        port: "2004"
```

#### Variable: `i2_remove_unmanaged_features`

The variable `i2_remove_unmanaged_features` change the behaviour of the feature handling.
It will remove all **unmanged** `.conf` files from the directory `/etc/icinga2/features-enabled` and let you manage only your defined features.

### Handlers

#### Handler: `start icinga2`

This handler starts Icinga 2. It is only used to make sure Icinga 2 is running. You can prevent this handler from
being triggered by setting `i2_manage_service` to false.

#### Handler: `reload icinga2`

This handler reloads Icinga 2 when configuration changes. You can prevent this handler from being triggered by setting
`i2_manage_service` to false.

### Examples

Example Agent Config:

Example usage (api featuer will NOT be enabled in this example):

```yaml
- name: icinga Package
  hosts: icingaagents
  roles:
    - icinga2
  vars:
    i2_confd: [] #don't include conf.d
    i2_zones:
      - name: master
        is_parent: true
        endpoints:
          - name: master1.example.tom
            host: master1.example.tom
            port: 15667
          - name: master2.example.tom
            host: 128.0.0.1
```

## Dependencies

None

## Example Playbook

```yaml
---

- name: Playbook
  hosts: all

  roles:
    - icinga.icinga2
```

<!--
## Development
A roadmap of this project is located at https://github.com/Icinga/ansible-icinga2/milestones. Please consider this
roadmap when you start contributing to the project.
-->

## Contributing

When contributing several steps such as pull requests and proper testing implementations are required. Find a detailed
step by step guide in [CONTRIBUTING.md](CONTRIBUTING.md).

## Testing

Testing is essential in our workflow to ensure a good quality. We use Molecule to test all
components of this role. For a detailed description see [TESTING.md](TESTING.md).

## Release Notes

When releasing new versions we refer to [SemVer 1.0.0](http://semver.org/spec/v1.0.0.html) for version numbers. All steps required when creating a new
release are described in [RELEASE.md](RELEASE.md)

See also [CHANGELOG.md](CHANGELOG.md)

## Authors

[AUTHORS](AUTHORS) is generated on each release.

## License

This project is under the Apache License. See the [LICENSE](LICENSE) file for the full license text.
