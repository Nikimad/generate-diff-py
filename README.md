# generate-diff-py

[![CI](https://github.com/Nikimad/generate-diff-py/actions/workflows/ci.yml/badge.svg)](https://github.com/Nikimad/generate-diff-py/actions/workflows/ci.yml)

Консольная утилита, которая сравнивает два файла конфигурации (JSON и YAML) и показывает различия. Вложенные структуры сравниваются рекурсивно.

## Требования

- Python 3.10+
- [uv](https://docs.astral.sh/uv/)

## Установка

```bash
git clone https://github.com/Nikimad/generate-diff-py.git
cd generate-diff-py
uv sync
```

## Использование

```bash
uv run gendiff [-f FORMAT] first_file second_file
```

Поддерживаемые входные форматы: `.json`, `.yml`, `.yaml` (файлы могут быть разных форматов).

Форматы вывода (`-f`, `--format`):

| Формат | Описание |
|---|---|
| `stylish` | дерево с отступами, по умолчанию |
| `plain` | одна строка на каждое изменение |
| `json` | дерево различий в JSON |

### Примеры

```bash
uv run gendiff file1.json file2.json
uv run gendiff --format plain file1.yml file2.json
uv run gendiff -f json file1.yml file2.yml
```

Пример `plain`:

```
Property 'common.setting2' was removed
Property 'common.setting4' was added with value: 'blah blah'
Property 'group1.baz' was updated. From 'bas' to 'bars'
```

Пример `stylish`:

```
{
    common: {
      - setting2: 200
      + setting4: blah blah
    }
}
```
