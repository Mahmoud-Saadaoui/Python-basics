# Regex Fundamentals — A Practical Guide

## Common Regex Components
```
| Symbol  | Meaning                      | Example                       |      |      |
| ------- | ---------------------------- | ----------------------------- | ---- | ---- |
| `.`     | Any character except newline | `a.c` → matches `abc`, `a7c`  |      |      |
| `^`     | Start of string              | `^Hello`                      |      |      |
| `$`     | End of string                | `world$`                      |      |      |
| `*`     | 0 or more repetitions        | `ba*` → `b`, `ba`, `baaa`     |      |      |
| `+`     | 1 or more repetitions        | `ba+` → `ba`, `baa`           |      |      |
| `?`     | Optional (0 or 1)            | `colou?r` → `color`, `colour` |      |      |
| `{n}`   | Exactly n repetitions        | `a{3}` → `aaa`                |      |      |
| `{n,}`  | At least n repetitions       | `a{2,}`                       |      |      |
| `{n,m}` | Between n and m repetitions  | `a{2,4}`                      |      |      |
| `[]`    | Character set                | `[A-Z]`                       |      |      |
| `       | `                            | OR                            | `cat | dog` |
| `()`    | Grouping                     | `(ab)+`                       |      |      |
| `\`     | Escape special character     | `\.` for literal dot          |      |      |

```

## Real-World Examples
#### ✔ Validate Email
```
^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$

```

#### ✔ Validate Phone Number
(Example: US format)
```
^\+?1?\s?-?\(?\d{3}\)?\s?-?\d{3}\s?-?\d{4}$

```

#### ✔ Validate Strong Password
At least 8 chars, one uppercase, one lowercase, one digit:
```
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$

```

#### ✔ Match Dates (YYYY-MM-DD)
```
^\d{4}-\d{2}-\d{2}$

```

## Useful Tips
* Always prefix patterns with r"..." to create raw strings.
* Use online regex testers, like Regex101.
* Test patterns with real-world messy data.
* Avoid overly long or unreadable regex — use comments if needed:
```
pattern = r"""
^\d{4}      # year
-           # separator
\d{2}       # month
-           # separator
\d{2}$      # day
"""
re.compile(pattern, re.VERBOSE)

```

## Recommended Tools
* Regex101 (best tester)
* Pythex.org
* VS Code Regex Search (Ctrl + F → .* button)