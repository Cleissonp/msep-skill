# MSEP Skill — SENAI

Skill reutilizável para apoiar o planejamento pedagógico na Metodologia SENAI de Educação Profissional (MSEP), com materiais em português brasileiro.

> **Nota:** este projeto é um recurso de apoio independente. Não é uma publicação oficial do SENAI e não substitui documentos institucionais, planos de curso ou orientações vigentes da unidade escolar.

## Estrutura

- `SKILL.md`: instruções principais para agentes de IA.
- `references/`: avaliação, estratégias de ensino e aprendizagem e glossário.
- `assets/modelo-situacao-aprendizagem.md`: modelo preenchível.
- `scripts/validar_msep.py`: validação estrutural básica.

## Uso

Peça, por exemplo: “Crie uma situação de aprendizagem de 4 horas para introduzir entradas e saídas digitais no Arduino para iniciantes.” Forneça, quando possível, curso, unidade curricular, perfil da turma, duração, infraestrutura e resultado esperado.

## Validação

Requer Python 3.10 ou superior. Execute:

```bash
python scripts/validar_msep.py
```

Esta skill é apoio de planejamento e não comprova conformidade oficial com versões institucionais da MSEP.
