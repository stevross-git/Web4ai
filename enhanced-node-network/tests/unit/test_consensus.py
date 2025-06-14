from enhanced_network.coordination.consensus import majority_vote


def test_majority_vote():
    result = majority_vote({"a": 1, "b": 1, "c": 2})
    assert result == 1
