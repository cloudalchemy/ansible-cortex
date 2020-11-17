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
    "/cortex/cortex-ingester.yml",
    "/etc/systemd/system/cortex@.service",
    "/usr/local/bin/cortex-linux-amd64",
])
def test_files(host, files):
    f = host.file(files)
    assert f.exists
    assert f.is_file


def test_user(host):
    assert host.group("vortex").exists
    assert host.user("vortex").exists


def test_service(host):
    s = host.service("cortex@ingester")
    # assert s.is_enabled
    assert s.is_running


@pytest.mark.parametrize("port", [9009, 9010, 9095, 9096])
def test_socket(host, port):
    s = host.socket("tcp://0.0.0.0:%d" % port)
    assert s.is_listening


def test_config_file_no_target(host):
    f = host.file("/cortex/cortex-ingester.yml")
    config = yaml.load(f.content_string, Loader=yaml.SafeLoader)
    assert config["target"] == "ingester"


def test_config_file_explicit_target(host):
    f = host.file("/cortex/cortex-readpath.yml")
    config = yaml.load(f.content_string, Loader=yaml.SafeLoader)
    assert config["target"] == "querier,store-gateway"
