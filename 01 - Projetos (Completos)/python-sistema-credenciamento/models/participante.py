class Participante:

    def __init__(self, nome, cpf, email, telefone, empresa, cargo,
                 uuid = None, qr_code = None, entrada_realizada = False, 
                 data_entrada = None, hora_entrada = None, criado_em = None,
                 id = None, cracha = None):
                    self.id = id
                    self.uuid = uuid

                    self.nome = nome
                    self.cpf = cpf
                    self.email = email
                    self.telefone = telefone

                    self.empresa = empresa
                    self.cargo = cargo

                    self.qr_code = qr_code

                    self.entrada_realizada = entrada_realizada

                    self.data_entrada = data_entrada

                    self.hora_entrada = hora_entrada

                    self.criado_em = criado_em
                    self.cracha = cracha
    
    def __str__(self):
        
        return (
            f"Participante("
            f"id={self.id}, "
            f"nome='{self.nome}', "
            f"cpf='{self.cpf}', "
            f"empresa='{self.empresa}')"
        )

    def to_dict(self):

        return {
            "id": self.id,
            "uuid": self.uuid,
            "nome": self.nome,
            "cpf": self.cpf,
            "email": self.email,
            "telefone": self.telefone,
            "empresa": self.empresa,
            "cargo": self.cargo,
            "qr_code": self.qr_code,
            "entrada_realizada": self.entrada_realizada,
            "data_entrada": self.data_entrada,
            "hora_entrada": self.hora_entrada,
            "criado_em": self.criado_em,
            "cracha": self.cracha
        }
            
    @classmethod
    def from_dict(cls, dados):

        return cls(
            id=dados["id"],
            uuid=dados["uuid"],
            nome=dados["nome"],
            cpf=dados["cpf"],
            email=dados["email"],
            telefone=dados["telefone"],
            empresa=dados["empresa"],
            cargo=dados["cargo"],
            qr_code=dados["qr_code"],
            entrada_realizada=bool(dados["entrada_realizada"]),
            data_entrada=dados["data_entrada"],
            hora_entrada=dados["hora_entrada"],
            criado_em=dados["criado_em"],
            cracha=dados["cracha"]
        )