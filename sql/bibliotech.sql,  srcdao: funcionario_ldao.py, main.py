FOREIGN KEY (cpf) REFERENCES usuario(cpf)
);

CREATE SEQUENCE funcionario_seq START 1;

CREATE TABLE funcionario (
    matricula VARCHAR(20) PRIMARY KEY,
    matricula VARCHAR(20) PRIMARY KEY DEFAULT ('F' || LPAD(nextval('funcionario_seq')::TEXT, 3, '0')),
    nome VARCHAR(100) NOT NULL,
    salario DECIMAL(10,2) NOT NULL,
    cargo VARCHAR(50) NOT NULL

def insert(self, funcionario: Funcionario):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO funcionario (matricula, nome, salario, cargo)
            VALUES (%s, %s, %s, %s)
        """, (funcionario.matricula, funcionario.nome,
              funcionario.salario, funcionario.cargo))
        if funcionario.matricula:
            cur.execute("""
                INSERT INTO funcionario (matricula, nome, salario, cargo)
                VALUES (%s, %s, %s, %s)
            """, (funcionario.matricula, funcionario.nome,
                  funcionario.salario, funcionario.cargo))
        else:
            cur.execute("""
                INSERT INTO funcionario (nome, salario, cargo)
                VALUES (%s, %s, %s)
                RETURNING matricula
            """, (funcionario.nome, funcionario.salario, funcionario.cargo))
            funcionario.matricula = cur.fetchone()[0]
        conn.commit()
        cur.close()

    if op == "1":
            listar(UsuarioDAO().get_all, "USUARIOS",
                   [("CPF", "cpf"), ("Nome", "nome"), ("Nascimento", "data_nascimento"),
                    ("Bairro", "bairro")])
                     ("Rua", "rua"), ("Numero", "numero"), ("Bairro", "bairro")])
        elif op == "2":
            cpf = so_digitos(input("CPF: "))
            u = UsuarioDAO().get_by_cpf(cpf)

def inserir_funcionario():
    print("\n--- Novo Funcionario ---")
    mat = input("Matricula: ").upper()
    nome = input("Nome: ")
    salario = float(input("Salario: "))
    cargo = input("Cargo: ")
    FuncionarioDAO().insert(Funcionario(mat, nome, salario, cargo))
    print("Funcionario inserido!")
    f = Funcionario("", nome, salario, cargo)
    FuncionarioDAO().insert(f)
    print(f"Funcionario inserido! Matricula: {f.matricula}")


def crud_funcionario():

  def insert(self, funcionario: Funcionario):
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO funcionario (matricula, nome, salario, cargo)
            VALUES (%s, %s, %s, %s)
        """, (funcionario.matricula, funcionario.nome,
              funcionario.salario, funcionario.cargo))
        if funcionario.matricula:
            cur.execute("""
                INSERT INTO funcionario (matricula, nome, salario, cargo)
                VALUES (%s, %s, %s, %s)
            """, (funcionario.matricula, funcionario.nome,
                  funcionario.salario, funcionario.cargo))
        else:
            cur.execute("""
                INSERT INTO funcionario (nome, salario, cargo)
                VALUES (%s, %s, %s)
                RETURNING matricula
            """, (funcionario.nome, funcionario.salario, funcionario.cargo))
            funcionario.matricula = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()

 listar(UsuarioDAO().get_all, "USUARIOS",
                   [("CPF", "cpf"), ("Nome", "nome"), ("Nascimento", "data_nascimento"),
                    ("Bairro", "bairro")])
                     ("Rua", "rua"), ("Numero", "numero"), ("Bairro", "bairro")])
        elif op == "2":
            cpf = so_digitos(input("CPF: "))
            u = UsuarioDAO().get_by_cpf(cpf)
@@ -132,12 +132,12 @@ def crud_usuario():

def inserir_funcionario():
    print("\n--- Novo Funcionario ---")
    mat = input("Matricula: ").upper()
    nome = input("Nome: ")
    salario = float(input("Salario: "))
    cargo = input("Cargo: ")
    FuncionarioDAO().insert(Funcionario(mat, nome, salario, cargo))
    print("Funcionario inserido!")
    f = Funcionario("", nome, salario, cargo)
    FuncionarioDAO().insert(f)
    print(f"Funcionario inserido! Matricula: {f.matricula}")


def crud_funcionario():
        conn.close()

if op == "1":
            listar(UsuarioDAO().get_all, "USUARIOS",
                   [("CPF", "cpf"), ("Nome", "nome"), ("Nascimento", "data_nascimento"),
                    ("Bairro", "bairro")])
                     ("Rua", "rua"), ("Numero", "numero"), ("Bairro", "bairro")])
        elif op == "2":
            cpf = so_digitos(input("CPF: "))
            u = UsuarioDAO().get_by_cpf(cpf)
@@ -132,12 +132,12 @@ def crud_usuario():

def inserir_funcionario():
    print("\n--- Novo Funcionario ---")
    mat = input("Matricula: ").upper()
    nome = input("Nome: ")
    salario = float(input("Salario: "))
    cargo = input("Cargo: ")
    FuncionarioDAO().insert(Funcionario(mat, nome, salario, cargo))
    print("Funcionario inserido!")
    f = Funcionario("", nome, salario, cargo)
    FuncionarioDAO().insert(f)
    print(f"Funcionario inserido! Matricula: {f.matricula}")


def crud_funcionario():
