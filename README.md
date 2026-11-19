# turkce-seo-slug

Türkçe başlıklardan SEO uyumlu URL slug'ı üretir.

```bash
pip install turkce-seo-slug
```

## Kullanım

```python
from turkce_seo_slug import tr_slug

tr_slug("Çok güzel başlık! İstanbul'da")
# 'cok-guzel-baslik-istanbulda'

tr_slug("Uzun bir SEO başlığı örneği", max_length=15)
# 'uzun-bir-seo'   (kelime sınırında kesilir)

tr_slug("Café Ünlü", lang="en")
# 'cafe-unlu'
```

## Parametreler

- `lang`: `"tr"` (varsayılan) Türkçe harfleri aksansız karşılığına çevirir. `"en"` yalnızca aksanları kaldırır.
- `separator`: Kelimeler arasındaki ayırıcı. Varsayılan `"-"`.
- `max_length`: Slug'ın en fazla uzunluğu. Kelime sınırında keser, tek kelime bile sığmıyorsa sertçe keser.

Kesme işaretleri kelimeyi bölmez: `İstanbul'da` → `istanbulda`.

Harf dönüşümleri `turkce-harf` paketinden gelir.

## Geliştirme

```bash
pip install -e ".[test]"
pytest
```

## Lisans

MIT
