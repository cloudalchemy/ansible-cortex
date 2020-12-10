import pytest
import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("files", [
    "/etc/cortex/cortex.yml",
    "/etc/systemd/system/cortex.service",
    "/usr/local/bin/cortex-linux-amd64",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file
