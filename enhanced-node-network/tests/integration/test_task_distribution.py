from enhanced_network.coordination.load_balancer import LoadBalancer


def test_round_robin_load_balancer():
    lb = LoadBalancer()
    lb.register("a")
    lb.register("b")
    assert lb.next_worker() == "a"
    assert lb.next_worker() == "b"
    assert lb.next_worker() == "a"
