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
| `cortex_all_in_one` | true | Setup Cortex in all-in-one binary mode. |
| `cortex_services` | `{}` | Cortex services configurations. |
| `cortex_web_listen_address` | "0.0.0.0:9009" | Address on which cortex will listen |
| `cortex_binary_local_dir` | "" | Allows to use local packages instead of ones distributed on github. As parameter it takes a directory where `cortex` binaries are stored on host on which ansible is ran. This overrides `cortex_version` parameter |
| `cortex_interface` | "{{ ansible_default_ipv4.interface }}" | Network adapter that cortex will be using |
| `cortex_config_dir` | "/etc/cortex" | Default directory for the cortex config |
| `cortex_db_dir` | "/var/lib/cortex" | Path to the directory of the Cortex database |
| `cortex_limit_nofile` | 10240 | Number of File Descriptors allowed for Cortex processes |
| `cortex_system_user` | "cortex" | Default Cortex user |
| `cortex_system_group` | "cortex" | Default Cortex group |
| `cortex_version` | "1.6.0" | The cortex package version |
| `cortex_auth_enabled` | "false" | Enables of disables the Cortex authentication |
| `cortex_alertmanager` | `{}` | Cortex alertmanager. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#alertmanager_config) |
| `cortex_api` | `{}` | Cortex api. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/) |
| `cortex_blocks_storage` | [From block storage example][bse] | Cortex blocks storage. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#blocks_storage_config) |
| `cortex_chunck_store` | `{}` | Cortex chunck store. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#configstore_config) |
| `cortex_compactor` | [From block storage example][bse] | Cortex compactor. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#compactor_config) |
| `cortex_configs` | `{}` | Cortex configs. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#configs_config) |
| `cortex_distributor` | [From block storage example][bse] | Cortex distributor. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#distributor_config) |
| `cortex_flusher` | `{}` | Cortex flusher. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#flusher_config) |
| `cortex_frontend_worker` | [From block storage example][bse] | Cortex frontend worker. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#frontend_worker_config) |
| `cortex_frontend` | `{}` | Cortex frontend. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/) |
| `cortex_ingester_client` | [From block storage example][bse] | Cortex ingester client. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#ingester_client_config) |
| `cortex_ingester` | [From block storage example][bse] | Cortex ingester. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#ingester_config) |
| `cortex_limits` | `{}` | Cortex limits. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#limits_config) |
| `cortex_memberlist` | `{}` | Cortex memberlist. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#memberlist_config) |
| `cortex_prealloc` | `{}` | Cortex prealloc. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/) |
| `cortex_purger` | `{}` | Cortex purger. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#purger_config) |
| `cortex_querier` | `{}` | Cortex querier. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#querier_config) |
| `cortex_query_range` | `{}` | Cortex query range. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#query_range_config) |
| `cortex_ruler` | [From block storage example][bse] | Cortex ruler. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#ruler_config) |
| `cortex_runtime_config` | `{}` | Cortex runtime config. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/) |
| `cortex_schema` | `{}` | Cortex schema. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/) |
| `cortex_server` | [From block storage example][bse] | Cortex server. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#server_config) |
| `cortex_storage` | [From block storage example][bse] | Cortex storage. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#storage_config) |
| `cortex_store_gateway` | `{}` | Cortex store gateway. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#store_gateway_config) |
| `cortex_table_manager` | `{}` | Cortex table manager. Compatible with [official configuration](https://cortexmetrics.io/docs/configuration/configuration-file/#table_manager_config) |

[bse]:https://github.com/cortexproject/cortex/blob/master/docs/configuration/single-process-config-blocks.yaml

## Example

### Playbook

Use it in a playbook as follows:
```yaml
- hosts: all
  roles:
    - cloudalchemy.cortex
```

### Services mode

You can run the different Cortex modules as separate services by setting
`cortex_services` as a module:config map and `cortex_all_in_one` to `false`.
```yaml
- hosts: all
  roles:
    - cloudalchemy.cortex
  vars:
    cortex_all_in_one: false
    cortex_services:
      ingester:
        server:
            http_listen_port: 9009
        ingester:
            lifecycler:
              join_after: 0
              min_ready_duration: 0s
              final_sleep: 0s
              num_tokens: 512

              ring:
                kvstore:
                  store: inmemory
                  replication_factor: 1
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
