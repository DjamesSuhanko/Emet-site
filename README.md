# Emet · páginas públicas ClaveSol

Site público do Emet, separado do projeto privado VerbumDei, usando o layout de Musicool.

- Página: https://emet.clavesol.com.br/
- Política: https://emet.clavesol.com.br/privacidade/
- Contato: https://emet.clavesol.com.br/contato/
- Catálogo: https://emet.clavesol.com.br/biblia/catalogo.json

## Publicação

`python3 -m pip install -r requirements.txt`, `python3 build.py`, `python3 scripts/check_site.py`.
O workflow GitHub Actions publica exclusivamente `dist/` em Pages a cada push em `main`.

Textos editáveis em `content/`; identidade visual em `templates/` e `assets/`.
Para adicionar Bíblias, publique um novo pacote com nome versionado, seu manifesto e uma entrada em `biblia/catalogo.json`. O primeiro item será a seleção padrão no aplicativo. Cada pacote deve passar na validação do app (esquema v2, integridade, metadados e FTS5); favoritos são separados por edição. Não substitua arquivos de conteúdo versionados silenciosamente.

Este repositório não contém código-fonte do aplicativo, chaves de assinatura ou dados pessoais.
