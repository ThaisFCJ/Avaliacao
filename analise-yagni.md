# Análise YAGNI - Classe Usuário

## Itens desnecessários identificados

### Atributos desnecessários (Classe Usuario)

- id
- data_cadastro
- ultimo_login
- perfil
- permissoes
- configuracoes
- historico_logins
- foto_perfil_url
- telefone
- endereco
- empresa
- cargo
- departamento

O sistema atual requer apenas nome, email e senha. Os demais atributos antecipam funcionalidades futuras e aumentam a complexidade sem necessidade.

---

### Métodos desnecessários (Classe Usuario)

- _gerar_id()
- adicionar_permissao()
- remover_permissao()
- tem_permissao()
- atualizar_configuracao()
- registrar_login()
- exportar_json()
- exportar_xml()
- atualizar_foto_perfil()
- atualizar_dados_profissionais()

Esses métodos implementam funcionalidades como permissões, exportação e personalização, que não fazem parte dos requisitos atuais.

---

### Métodos desnecessários (GerenciadorUsuarios)

- buscar_por_perfil()
- buscar_por_permissao()
- exportar_todos_json()
- importar_usuarios_json()
- gerar_relatorio_atividade()
 
São funcionalidades avançadas que não foram solicitadas.

---