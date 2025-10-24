# goit-pythonweb-hw-01

## Опис

Домашнє завдання №1 (Python Web).  
Реалізовано патерн **Factory** для створення транспортних засобів із регіональними специфікаціями (US/EU).

Код типізовано, для логування використано `logging.info`,  
форматування здійснено за допомогою **black** та **isort**,  
статичний аналіз — через **ruff** і **mypy**.


---

## Environment

- macOS Tahoe
- Python 3.12.12 (`pyenv + poetry`)
- Poetry 2.x
- Ruff 0.14.x, Mypy 1.18.x, Black 25.x, isort 7.x, pytest 8.x, pre-commit 4.x

---

## Commands via Makefile

| Command          | Description                                |
|------------------|--------------------------------------------|
| `make run`       | Run main application                       |
| `make check`     | Full code check (black, isort, ruff, mypy) |
| `make format`    | Auto-format imports & code                 |
| `make lint`      | Only linting (ruff + mypy)                 |
| `make test`      | Run pytest                                 |
| `make precommit` | Run all pre-commit hooks manually          |

---

## Example result

```bash
INFO:root:Ford Mustang (US Spec): Двигун запущено
INFO:root:BMW R nineT (EU Spec): Мотор заведено
```

### Домашня робота №2 — Принципи SOLID

У цьому завданні проведено рефакторинг простої програми керування бібліотекою з урахуванням **принципів SOLID**.

### Реалізація

- Додано клас **`Book`**, який відповідає лише за збереження інформації про книгу (**SRP**).
- Створено абстрактний інтерфейс **`LibraryInterface`** для чіткої специфікації методів (**ISP, LSP**).
- Клас **`Library`** реалізує цей інтерфейс і може бути розширений без зміни базового коду (**OCP**).
- Клас **`LibraryManager`** працює через абстракцію `LibraryInterface`, а не напряму з реалізацією (**DIP**).
- Логування виконано через `logging.info`.
- Уся програма **типізована** (`mypy --strict`).
- Додано **pytest-тести** для перевірки функціональності.

### Перевірка

```bash
make check
make test
make precommit
```