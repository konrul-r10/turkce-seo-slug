# turkce-seo-slug

Türkçe başlıklardan SEO uyumlu URL slug'ı üretir.

Generates SEO-friendly URL slugs from Turkish titles.

```bash
pip install turkce-seo-slug
```

## Kullanım / Usage

```python
from turkce_seo_slug import tr_slug

tr_slug("Çok güzel başlık! İstanbul'da")
# 'cok-guzel-baslik-istanbulda'

tr_slug("Uzun bir SEO başlığı örneği", max_length=15)
# 'uzun-bir-seo'   (kelime sınırında kesilir / cut at a word boundary)

tr_slug("Café Ünlü", lang="en")
# 'cafe-unlu'
```

## Parametreler / Parameters

- `lang`: `"tr"` (varsayılan / default) Türkçe harfleri aksansız karşılığına çevirir / converts Turkish letters to their plain ASCII forms. `"en"` yalnızca aksanları kaldırır / only removes accents.
- `separator`: Kelimeler arasındaki ayırıcı / separator between words. Varsayılan / default `"-"`.
- `max_length`: Slug'ın en fazla uzunluğu / maximum slug length. Kelime sınırında keser, tek kelime bile sığmıyorsa sertçe keser / cuts at a word boundary; if a single word doesn't fit, it is cut hard.

Kesme işaretleri kelimeyi bölmez / Apostrophes do not split words: `İstanbul'da` → `istanbulda`.

Harf dönüşümleri `turkce-harf` paketinden gelir / Letter conversions come from the `turkce-harf` package.

## Geliştirme / Development

```bash
pip install -e ".[test]"
pytest
```

## Lisans / License

MIT
