# K-System IDE

**The K-System IDE** is a recursive symbolic development environment designed to execute real-time mathematics encoded in K-notation.

Unlike traditional programming interfaces, this IDE interprets **recursive, dimensional, and symbolic logic** used in Chronogenesis, Mirror Theory, and the full K-Math framework.

It supports symbolic execution, visual recursive flows, and plug-and-play glyphic language extensions.

---

## 🔁 Key Modules

- `k_parser.py`  
  Parses K-notation symbols (e.g., `Ω°`, `⦿`, `Δ⟡`) into logical tree structures.

- `k_runtime.py`  
  Executes parsed symbolic structures in a real-time symbolic engine.

- `mirror_workspace.py`  
  Simulates a reflective symbolic canvas where transformations and recursions animate visibly.

- `plugin_core.py`  
  Loads IDE extension modules, including Chrono scripts, Ghost overlays, and dimension shifters.

---

## 🧪 Testing

A basic test script is available in `tests/test_suite.py` to verify the parser + runtime.

```python
expr = 'Ω°Δ⦿'
parsed = KParser().parse(expr)
output = KRuntime().execute(parsed)
print(output)
```

### Running tests

Use Python's built-in test runner:

```bash
python -m unittest discover -s src/tests -v
```
