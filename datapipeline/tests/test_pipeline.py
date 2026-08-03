from datapipeline.ingest import ingest
from datapipeline.preprocess import preprocess


def test_ingest_returns_list():
    assert isinstance(ingest("config/pipeline.yaml"), list)


def test_preprocess_is_passthrough_on_empty():
    assert preprocess([]) == []
