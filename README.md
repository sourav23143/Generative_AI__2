# Dependency workflow

Use `uv add` as the source of truth for this project. It updates `pyproject.toml`, `uv.lock`, and the environment.

To keep `requirements.txt` updated too, use:

```powershell
.\scripts\add-package.ps1 tavily-python
```

For multiple packages:

```powershell
.\scripts\add-package.ps1 tavily-python requests
```

For dev-only packages:

```powershell
.\scripts\add-package.ps1 pytest -Dev
```

If you already changed dependencies and only want to refresh `requirements.txt`, run:

```powershell
.\scripts\sync-requirements.ps1
```

These scripts use the repo-local `.uv-cache` directory to avoid cache permission problems.
