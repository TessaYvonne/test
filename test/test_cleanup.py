from Word import Word
from reconstructions import cleanup_all


def test_cleanup():
    assert(cleanup_all("d-ɔ̀l°° (fskbvs) / m-ɔ̀l") == Word("ɔ̀l", "d-"))
