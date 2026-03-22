import hashlib
from typing import List, Optional

class Usuario:
    
    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = self._hash_senha(senha)
    
    def _hash_senha(self, senha: str) -> str:
        """Segurança básica: Hash da senha."""
        return hashlib.sha256(senha.encode()).hexdigest()
    
    def validar_senha(self, senha: str) -> bool:
        """Valida se a senha informada corresponde ao hash."""
        return self._hash_senha(senha) == self.senha


class GerenciadorUsuarios:
    
    def __init__(self):
        self.usuarios: List[Usuario] = []
    
    def cadastrar(self, nome: str, email: str, senha: str) -> Usuario:
        """Cadastra novo usuário validando duplicidade de email."""
        if any(u.email == email for u in self.usuarios):
            raise ValueError("Email já cadastrado")
        
        novo_usuario = Usuario(nome, email, senha)
        self.usuarios.append(novo_usuario)
        return novo_usuario
    
    def fazer_login(self, email: str, senha: str) -> Optional[Usuario]:
        """Realiza login validando credenciais."""
        for usuario in self.usuarios:
            if usuario.email == email and usuario.validar_senha(senha):
                return usuario
        return None
    
    def listar_todos(self) -> List[Usuario]:
        return self.usuarios