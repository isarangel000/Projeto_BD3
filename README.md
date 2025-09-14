

# ㅤ♡     Projeto Banco de Usuários — Inclusão com Carinhoㅤ

Este projeto foi desenvolvido no **3º bimestre da disciplina de Redes**, ministrada pelo professor **Bruno**.
As alunas responsáveis pelo trabalho são:

* ۶ৎ **Ana Clara dos Santos Moreira**
* ۶ৎ **Isabela Rangel**
* ۶ৎ **Isabelli Arantes Galvão**
  
  Todas do **2J - Informática** 💻

---

## 🌸 Funcionalidades 🌸

* 📌 **Cadastrar usuário** (com nome, idade e tipo de deficiência)
* 📋 **Listar todos os usuários cadastrados**
* 🔎 **Buscar por tipo de deficiência**
* 🖥️ Menu interativo e intuitivo

---

##  Tecnologias usadas

*  **Python** (com `mysql.connector`)
*  **MySQL** (para guardar os dados)

---

## 📂 Estrutura do Banco

```sql
CREATE DATABASE banco_proj3;
USE banco_proj3;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INT NOT NULL,
    tipo_deficiencia VARCHAR(100) NOT NULL
);

DELETE FROM usuarios WHERE id = 0;
```

---

## ˙⋆✮ Como rodar 

1. Clone este repositório 
2. Configure o MySQL (usuário `root` e senha em branco ou ajuste no código )
3. Crie o banco de dados com o script acima 
4. Execute o programa:

   ```bash
   python seu_arquivo.py
   ```
5. Aproveite o menu interativo e cadastre seus usuários ✨

---

## 💖 Exemplo de uso

```
--- Menu ---
1 - Cadastrar novo usuário
2 - Listar todos os usuários
3 - Buscar por tipo de deficiência
0 - Sair
```

---

## 🎀 Sobre o projeto

A ideia é simples, mas cheia de significado: registrar informações de forma organizada, valorizando **inclusão e acessibilidade**. 🌍💜


---

❀ Trabalho feito com carinho pelas alunas do **2J** ❀
