from enhanced_network.utils.metrics import Metrics


def test_timer_records_duration():
    m = Metrics()
    with m.time("op"):
        pass
    assert m.timer("op") >= 0.0
