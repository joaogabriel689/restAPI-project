# 📦 API REST → Sistema PDV (Ponto de Venda)

🔗 **Repositório:**  
https://github.com/joaogabriel689/restAPI-project

---

## 🎯 Visão Geral

Este projeto iniciou como uma **API REST em Python** para estudo de backend e está sendo evoluído de forma incremental para se tornar um **Sistema PDV (Ponto de Venda)** completo.

O foco está em **boas práticas profissionais**, **regras de negócio reais** e **organização arquitetônica**, sendo ideal como **projeto de portfólio para estágio ou posição júnior em backend Python**.

---

## 📌 Escopo Atual

- Somente backend  
- Sem frontend (por enquanto)  
- Ênfase em lógica, domínio e arquitetura  

---

## 🧠 Objetivo do Projeto

Demonstrar, na prática:

- Organização arquitetural de backend  
- Evolução incremental de um sistema real  
- Implementação de regras de negócio  
- Autenticação, autorização e permissões  
- Controle de estoque, vendas e caixa  
- Código limpo, legível e manutenível  

> ❗ **Este não é um CRUD simples.**  
> O projeto representa a evolução real de um sistema, com decisões técnicas, erros, correções e amadurecimento — exatamente como ocorre em ambientes profissionais.

---

## ⚙️ Tecnologias Utilizadas

- Python  
- FastAPI  
- SQLAlchemy  
- Pydantic  
- JWT (JSON Web Token)  
- SQLite (ambiente de desenvolvimento)  
- Pytest (planejado)  

---

## 🧱 Arquitetura e Organização

A estrutura do projeto é organizada por **domínios**, facilitando manutenção, escalabilidade e leitura de código.

### 📁 Estrutura de Pastas

app/  
├── users/  
│   ├── models.py  
│   ├── schemas.py  
│   ├── routes.py  
│   └── service.py  
│  
├── auth/  
│   ├── security.py  
│   └── utils.py  
│  
├── core/  
│   ├── config.py  
│   ├── database.py  
│   └── dependencies.py  
│  
└── main.py  

---

## 📌 Padrões Aplicados

- Separação clara entre:
  - **models** (ORM)
  - **schemas** (validação)
  - **routes** (endpoints)
  - **services** (regras de negócio)
- Injeção de dependências com `Depends`
- Configuração centralizada
- Prevenção de imports circulares

---

## 🔐 Funcionalidades Já Implementadas

### Autenticação e Usuários

- Cadastro de usuários  
- Login com JWT  
- Geração e validação de access token  
- Proteção de rotas autenticadas  
- Endpoint de usuário logado  
- Hash de senhas  
- Validação de credenciais  

### Conceitos Trabalhados

- API REST  
- Autenticação stateless com JWT  
- Validação de dados  
- Modularização por domínio  
- Debug de erros reais (auth, imports, erros 500, migrations)

---

## 🛣️ Roadmap — Sistema PDV

### 🛒 Produtos

- Cadastro, edição e listagem  
- SKU / código único  
- Produto ativo / inativo  
- Soft delete  

### 📦 Estoque

- Controle de quantidade por produto  
- Entrada manual de estoque  
- Saída automática ao realizar venda  
- Bloqueio de estoque negativo  
- Histórico de movimentações  

### 💰 Vendas

- Registro de venda  
- Associação ao usuário (vendedor)  
- Cálculo automático do total  
- Venda imutável após finalização  

### 🧾 Itens de Venda

- Produtos vinculados à venda  
- Quantidade e preço unitário  
- Preço histórico preservado  

### 👥 Papéis e Permissões

- Administrador  
- Vendedor  
- RBAC (Role Based Access Control)  

### 🧠 Regras de Negócio (Diferencial)

- Usuário precisa estar autenticado para vender  
- Apenas admin pode cadastrar produtos  
- Estoque validado antes da venda  
- Auditoria de ações importantes  
- Histórico de alterações  

---

## 🧪 Qualidade e Maturidade

- Testes automatizados com Pytest  
- Testes de regras de negócio  
- Validações consistentes  
- Código organizado e legível  

---

## ☁️ Extras Planejados

- Deploy da API (Render / Railway)  
- Relatórios de vendas  
- Exportação CSV  
- Logs de auditoria  
- Fechamento de caixa  

---

## 📚 Resumo de Rotas

### 🔐 Autenticação (/auth)

- POST /auth/register  
- POST /auth/login  
- POST /auth/refresh  
- POST /auth/logout  

### 👤 Usuários (/users)

- GET /users/me  
- GET /users (admin)  
- GET /users/{id}  
- POST /users (admin)  
- PUT /users/{id}  
- PATCH /users/{id}/status  
- DELETE /users/{id} (soft delete)  

### 🧑‍💼 Papéis e Permissões

- GET /roles  
- POST /roles  
- PUT /roles/{id}  
- DELETE /roles/{id}  
- GET /permissions  
- POST /roles/{id}/permissions  

### 🛒 Produtos (/products)

- GET /products  
- GET /products/{id}  
- POST /products  
- PUT /products/{id}  
- PATCH /products/{id}/status  
- DELETE /products/{id}  

### 📦 Estoque (/inventory)

- GET /inventory  
- GET /inventory/{product_id}  
- POST /inventory/entry  
- POST /inventory/adjustment  
- GET /inventory/history/{product_id}  

### 💰 Vendas (/sales)

- POST /sales  
- POST /sales/{id}/items  
- PUT /sales/{id}/items/{item_id}  
- DELETE /sales/{id}/items/{item_id}  
- POST /sales/{id}/finalize  
- GET /sales/{id}  
- GET /sales  
- GET /sales/user/{user_id}  

### 💳 Pagamentos (/payments)

- POST /payments  
- GET /payments/{sale_id}  

### 🧮 Caixa (/cash-register)

- POST /cash-register/open  
- POST /cash-register/close  
- GET /cash-register/current  
- GET /cash-register/history  

### 📊 Relatórios (/reports)

- GET /reports/sales  
- GET /reports/products  
- GET /reports/stock  
- GET /reports/export/csv  

### 🧾 Auditoria (/audit-logs)

- GET /audit-logs  
- GET /audit-logs/{id}  

### ⚙️ Sistema (/system)

- GET /system/health  
- GET /system/info  

---

## 🧭 Ordem Correta de Implementação (Evita Refatoração)

1. Autenticação + Usuários  
2. Papéis / Permissões  
3. Produtos  
4. Estoque  
5. Vendas  
6. Pagamentos  
7. Caixa  
8. Auditoria  
9. Relatórios  

> ⚠️ Implementar fora dessa ordem gera retrabalho e refatoração desnecessária.

---

## 🎯 Objetivo Profissional

Este projeto foi pensado para demonstrar:

- Conhecimento sólido de backend  
- Organização de código  
- Evolução incremental de um sistema  
- Domínio de regras de negócio  
- Preparação para estágio ou backend júnior Python  

---

## 🧠 Observação Final

Este repositório representa a **evolução real de um sistema backend**, não apenas endpoints funcionando.

É sobre **decisão técnica, estrutura, regra de negócio e crescimento profissional**.

🚀 **Backend de verdade.**
