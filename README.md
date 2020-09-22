# Ansible Role: cortex

[![Build Status](https://travis-ci.com/cloudalchemy/ansible-cortex.svg?branch=master)](https://travis-ci.com/cloudalchemy/ansible-cortex)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-cloudalchemy.cortex-blue.svg)](https://galaxy.ansible.com/cloudalchemy/cortex/)
[![GitHub tag](https://img.shields.io/github/tag/cloudalchemy/ansible-cortex.svg)](https://github.com/cloudalchemy/ansible-cortex/tags)

## Description

Deploy [cortex](https://github.com/cortexproject/cortex) using ansible.

## Requirements

- Ansible >= 2.7 (It might work on previous versions, but we cannot guarantee it)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below.

| Name           | Default Value | Description                        |
| -------------- | ------------- | -----------------------------------|
| `cortex_web_listen_address` | "0.0.0.0:9009" | Address on which cortex will listen |
| `cortex_binary_local_dir` | "" | Allows to use local packages instead of ones distributed on github. As parameter it takes a directory where `cortex` binaries are stored on host on which ansible is ran. This overrides `cortex_version` parameter |
| `cortex_interface` | "{{ ansible_default_ipv4.interface }}" | Network adapter that cortex will be using |
| `cortex_config_dir` | "/etc/cortex" | Default directory for the cortex config |
| `cortex_db_dir` | "/var/lib/cortex" | Path to the directory of the Cortex database |
| `cortex_system_user` | "cortex" | Default Cortex user |
| `cortex_system_group` | "cortex" | Default Cortex group |
| `cortex_version` | "1.4.0-rc.1" | The cortex package version |
| `cortex_auth_enabled` | "false" | Enables of disables the Cortex authentication |
| `cortex_server` | [From block storage example][bse] | Cortex server. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#server_config) |
| `cortex_distributor` | [From block storage example][bse] | Cortex distributor. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#distributor_config) |
| `cortex_ingester_client` | [From block storage example][bse] | Cortex ingester client. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#ingester_client_config) |
| `cortex_ingester` | [From block storage example][bse] | Cortex ingester. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#ingester_config) |
| `cortex_storage` | [From block storage example][bse] | Cortex storage. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#storage_config) |
| `cortex_blocks_storage` | [From block storage example][bse] | Cortex blocks storage. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#blocks_storage_config) |
| `cortex_compactor` | [From block storage example][bse] | Cortex compactor. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#compactor_config) |
| `cortex_frontend_worker` | [From block storage example][bse] | Cortex frontend worker. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#frontend_worker_config) |
| `cortex_ruler` | [From block storage example][bse] | Cortex ruler. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#ruler_config) |

[bse]:https://github.com/cortexproject/cortex/blob/master/docs/configuration/single-process-config-blocks.yaml

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  roles:
    - cloudalchemy.cortex
```
## Local Testing

The preferred way of locally testing the role is to use Docker and [molecule](https://github.com/metacloud/molecule) (v2.x). You will have to install Docker on your system. See "Get started" for a Docker package suitable to for your system.
We are using tox to simplify process of testing on multiple ansible versions. To install tox execute:
```sh
pip3 install tox
```
To run tests on all ansible versions (WARNING: this can take some time)
```sh
tox
```
To run a custom molecule command on custom environment with only default test scenario:
```sh
tox -e py35-ansible28 -- molecule test -s default
```
For more information about molecule go to their [docs](http://molecule.readthedocs.io/en/latest/).

If you would like to run tests on remote docker host just specify `DOCKER_HOST` variable before running tox tests.

## Travis CI

Combining molecule and travis CI allows us to test how new PRs will behave when used with multiple ansible versions and multiple operating systems. This also allows use to create test scenarios for different role configurations. As a result we have a quite large test matrix which will take more time than local testing, so please be patient.

## Contributing

See [contributor guideline](CONTRIBUTING.md).

## Troubleshooting

See [troubleshooting](TROUBLESHOOTING.md).

## License

This project is licensed under MIT License. See [LICENSE](/LICENSE) for more details.
