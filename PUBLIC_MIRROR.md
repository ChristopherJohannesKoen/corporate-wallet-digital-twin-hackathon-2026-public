# Corporate Wallet Digital Twin V3.1.1 — safe public mirror

This clean-history mirror contains the production-shaped source, contracts,
tests and infrastructure definitions, but it runs only on an independently
generated, anonymized 20-client aggregate fixture. It contains no supplied or
derived row-level Syn Bank data, challenge-derived client aggregates,
credentials, provider payloads or downloaded source documents.

The public result demonstrates mechanics only. It is not the confidential
hackathon result, measured competitor share, causal uplift or a bank-production
release.

## Reproduce

```bash
uv sync --frozen --all-extras
uv run python scripts/build_safe_demo.py
```

The command rebuilds the V2/V3/V3.1 schemas and anonymous workbench fixtures,
runs the safe-demo tests, and checks the mirror manifest.
