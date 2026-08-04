from calc.slugify import slugify
from calc.median import median


def test_slugify_joins_words():
    assert "-" in slugify("two words")


def test_median_single():
    assert median([7]) == 7
