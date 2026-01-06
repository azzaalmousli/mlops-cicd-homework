from app.features import hash_feature


def test_hash_feature_is_deterministic():
    """
    Same input should always return the same bucket.
    """
    assert hash_feature("azza", 10) == hash_feature("azza", 10)


def test_hash_feature_output_range():
    """
    Output must always be within bucket range.
    """
    result = hash_feature("mlops", 10)
    assert 0 <= result < 10
