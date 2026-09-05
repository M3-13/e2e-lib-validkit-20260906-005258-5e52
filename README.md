# validkit

validkit ist eine eigenständige, abhängigkeitsfreie Python-Bibliothek mit kleinen,
reinen, typannotierten Prüf- und Normalisierungsfunktionen. Sie stellt die Validierung
von E-Mail-Adressen, Kreditkarten-Prüfziffern (Luhn), ISBN-13 und IBAN sowie die
Normalisierung von Telefonnummern, Texten und Geheimnissen bereit. Alle Funktionen
sind über ein sauberes `__init__.py` als einheitliche API verfügbar.

## Tech-Stack

- **Sprache**: Python
- **Laufzeit**: Python 3.10+
- **Tests**: pytest
- **Abhängigkeiten**: keine (nur Standardbibliothek)
- **Paketierung**: setuptools (`pyproject.toml`)

## Installation

```bash
pip install -e .
```

Für die Entwicklung inklusive Testwerkzeug:

```bash
pip install -e ".[dev]"
```

## Verwendung

Alle neun Funktionen sind direkt über das Paket `validkit` verfügbar:

```python
import validkit
```

| Funktion | Beispiel | Ergebnis |
| --- | --- | --- |
| `is_valid_email` | `validkit.is_valid_email('user@example.com')` | `True` |
| `luhn_check` | `validkit.luhn_check('4532015112830366')` | `True` |
| `is_valid_isbn13` | `validkit.is_valid_isbn13('978-3-16-148410-0')` | `True` |
| `is_valid_iban` | `validkit.is_valid_iban('DE89 3704 0044 0532 0130 00')` | `True` |
| `normalize_phone` | `validkit.normalize_phone('030 1234567', '49')` | `'+49301234567'` |
| `strip_accents` | `validkit.strip_accents('Grüße')` | `'Gruße'` |
| `mask_secret` | `validkit.mask_secret('S3cret!')` | `'***ret!'` |
| `slugify` | `validkit.slugify('Héllo Wörld!')` | `'hello-world'` |
| `clamp` | `validkit.clamp(15, 0, 10)` | `10` |

## Funktionen

- `is_valid_email(text)` — prüft, ob `text` eine plausible E-Mail-Adresse ist.
- `luhn_check(digits)` — validiert eine Ziffernfolge über die Luhn-Prüfziffer.
- `is_valid_isbn13(text)` — prüft eine ISBN-13 inklusive Prüfziffer.
- `is_valid_iban(text)` — validiert eine IBAN über die Modulo-97-Prüfung.
- `normalize_phone(text, country_code)` — normalisiert eine Rufnummer in das E.164-Format.
- `strip_accents(text)` — entfernt Akzente (NFD) und lässt `ß` unverändert.
- `mask_secret(text, keep=4)` — maskiert alle Zeichen bis auf die letzten `keep`.
- `slugify(text)` — erzeugt einen kleingeschriebenen, URL-tauglichen Slug.
- `clamp(value, low, high)` — begrenzt `value` auf das Intervall `[low, high]`.

## Tests

```bash
pytest
```
