from enhanced_network.discovery.topology_manager import TopologyManager


def test_topology_add_remove():
    tm = TopologyManager()
    tm.add_node("a", {"ip": "1.1.1.1"})
    assert tm.count() == 1
    tm.remove_node("a")
    assert tm.count() == 0
