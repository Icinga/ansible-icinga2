import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_icinga_repository_file(host):
    if host.system_info.distribution == 'centos':
        i2_repo = host.file('/etc/yum.repos.d/ICINGA-release.repo')
    else:
        i2_repo = host.file('/etc/apt/sources.list.d/packages_icinga_com_ubuntu.list')

    assert i2_repo.exists
    assert i2_repo.user == 'root'
    assert i2_repo.group == 'root'


def test_icinga2_is_installed(host):
    i2_package = host.package("icinga2")

    assert i2_package.is_installed


def test_icinga2_running_and_enabled(host):
    i2_service = host.service("icinga2")

    assert i2_service.is_running
    assert i2_service.is_enabled
