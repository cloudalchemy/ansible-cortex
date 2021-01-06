import pytest
import os
import yaml
import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def AnsibleDefaults():
    with open("../../defaults/main.yml", 'r') as stream:
        return yaml.load(stream)


@pytest.mark.parametrize("dirs", [
    "/cortex",
    "/cortex/rules",
    "/cortexdb"
])
def test_directories(host, dirs):
    d = host.file(dirs)
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    "/cortex/cortex.yml",
    "/etc/systemd/system/cortex.service",
    "/usr/local/bin/cortex-linux-amd64",
    "/etc/default/cortex",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("vortex").exists
    assert host.user("vortex").exists


def test_service(host):
    s = host.service("cortex")
    # assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket("tcp://0.0.0.0:9009")
    assert s.is_listening

def test_string(host):
    f = host.file("/etc/default/cortex")
    assert "JAEGER_AGENT_HOST=localhost" in f.content_string
