import pytest

from turkce_seo_slug import tr_slug


@pytest.mark.parametrize(
    "given, expected",
    [
        ("Çok güzel başlık!", "cok-guzel-baslik"),
        ("İstanbul'da ılık", "istanbulda-ilik"),
        ("ŞİŞLİ  --  Çankaya", "sisli-cankaya"),
        ("Ğ Ü Ö Ş Ç", "g-u-o-s-c"),
        ("  Başta ve sonda  ", "basta-ve-sonda"),
        ("", ""),
        ("!!!", ""),
    ],
)
def test_basic(given, expected):
    assert tr_slug(given) == expected


def test_apostrophe_does_not_split_word():
    assert tr_slug("Ankara'nın") == "ankaranin"


def test_en_strips_accents():
    assert tr_slug("Café Ünlü", lang="en") == "cafe-unlu"
    assert tr_slug("Hello, World!", lang="en") == "hello-world"


def test_custom_separator():
    assert tr_slug("Çok güzel", separator="_") == "cok_guzel"


def test_max_length_cuts_at_word_boundary():
    assert tr_slug("Uzun bir SEO başlığı örneği", max_length=15) == "uzun-bir-seo"


def test_max_length_keeps_short_slug_intact():
    assert tr_slug("kısa", max_length=50) == "kisa"


def test_max_length_hard_cuts_single_long_word():
    assert tr_slug("abcdefghij", max_length=4) == "abcd"


def test_max_length_does_not_leave_trailing_separator():
    result = tr_slug("bir iki üç", max_length=7)
    assert not result.endswith("-")
    assert len(result) <= 7


@pytest.mark.parametrize(
    "kwargs",
    [
        {"lang": "de"},
        {"separator": ""},
        {"max_length": 0},
    ],
)
def test_invalid_arguments_raise(kwargs):
    with pytest.raises(ValueError):
        tr_slug("abc", **kwargs)
