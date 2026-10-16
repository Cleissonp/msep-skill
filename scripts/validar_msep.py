#!/usr/bin/env python3
"""Validador estrutural básico para a MSEP skill.

Este script verifica arquivos essenciais e referências locais. Não valida
conformidade pedagógica ou oficial com documentos institucionais do SENAI.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    Path("SKILL.md"),
    Path("README.md"),
    Path("references/avaliacao.md"),
    Path("references/estrategias-aprendizagem.md"),
    Path("references/estrategias-ensino.md"),
    Path("references/glossario.md"),
    Path("assets/modelo-situacao-aprendizagem.md"),
]


def main() -> int:
    errors: list[str] = []
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"Arquivo obrigatório ausente: {rel.as_posix()}")

    skill_path = ROOT / "SKILL.md"
    if skill_path.is_file():
        content = skill_path.read_text(encoding="utf-8")
        if not content.startswith("---\n"):
            errors.append("SKILL.md deve começar com frontmatter YAML delimitado por ---.")
        else:
            parts = content.split("---", 2)
            if len(parts) < 3:
                errors.append("Frontmatter do SKILL.md não foi fechado.")
            else:
                metadata = parts[1]
                for field in ("name:", "description:"):
                    if field not in metadata:
                        errors.append(f"Frontmatter sem campo obrigatório: {field}")
        if len(content) > 100_000:
            errors.append("SKILL.md excede o limite recomendável de 100 KB.")

    # Check relative Markdown links of the form [text](path.md).
    markdown_files = [ROOT / "README.md", *[(ROOT / rel) for rel in REQUIRED if rel.suffix == ".md"]]
    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for md_path in dict.fromkeys(markdown_files):
        if not md_path.is_file():
            continue
        for target in link_pattern.findall(md_path.read_text(encoding="utf-8")):
            if target.startswith(("https://", "http://", "mailto:", "#")):
                continue
            local_target = (md_path.parent / target.split("#", 1)[0]).resolve()
            if not local_target.exists():
                errors.append(f"Link local quebrado em {md_path.relative_to(ROOT)}: {target}")

    if errors:
        print("Falha na validação MSEP:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"Validação estrutural OK: {len(REQUIRED)} caminhos obrigatórios verificados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
