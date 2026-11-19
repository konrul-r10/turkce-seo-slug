"""Türkçe başlıklardan SEO uyumlu URL slug'ı üretir.

Harf dönüşümleri ``turkce-harf`` paketinden gelir.
"""

import re
import unicodedata

from turkce_harf import tr_fold, tr_lower, tr_nfc

__all__ = ["tr_slug"]

_APOSTROPHES = re.compile("['’ʼ`´]")
_NON_ALNUM = re.compile(r"[^a-z0-9]+")


def _ascii(text):
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def tr_slug(text, lang="tr", separator="-", max_length=None):
    """URL slug'ı üretir.

    - Kesme işaretleri silinir, kelimeyi bölmez: ``"İstanbul'da"`` → ``"istanbulda"``.
    - ``lang="tr"``: Türkçe harfler aksansız karşılığına çevrilir (``ç``→``c``, ``ı``→``i``).
    - ``lang="en"``: aksanlar kaldırılır (``é``→``e``).
    - Harf ve rakam dışındaki karakter dizileri ``separator`` ile değiştirilir.
    - ``max_length`` verilirse slug bu uzunluğu geçmez ve kelime sınırında kesilir.
      Tek bir kelime bile sığmıyorsa o kelime sertçe kesilir.

    >>> tr_slug("Çok güzel başlık! İstanbul'da")
    'cok-guzel-baslik-istanbulda'
    >>> tr_slug("Uzun bir SEO başlığı örneği", max_length=15)
    'uzun-bir-seo'
    """
    if separator == "" or not isinstance(separator, str):
        raise ValueError("separator boş olmayan bir metin olmalı")
    if lang not in ("tr", "en"):
        raise ValueError(f"lang 'tr' veya 'en' olmalı, verilen: {lang!r}")
    if max_length is not None and max_length < 1:
        raise ValueError("max_length en az 1 olmalı")

    text = _APOSTROPHES.sub("", tr_nfc(text))
    base = tr_fold(text, "tr") if lang == "tr" else tr_lower(text, "en")
    base = _ascii(base)
    slug = _NON_ALNUM.sub(lambda _m: separator, base).strip(separator)

    if max_length is not None and len(slug) > max_length:
        slug = _truncate(slug, max_length, separator)
    return slug


def _truncate(slug, max_length, separator):
    cut = slug[:max_length]
    # Kelime ortasında kesildiyse son, yarım kalmış parçayı at
    if len(slug) > max_length and slug[max_length] != separator:
        head, _, _ = cut.rpartition(separator)
        if head:
            cut = head
    return cut.rstrip(separator)
