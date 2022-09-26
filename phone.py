class Phone(Item):
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # Chamando a função super para ter acesso a todos atributos / metodos
        super().__init__(
            name, price, quantity
        )

        # validando argumentos
        assert broken_phones >= 0, f"Broken_phones {broken_phones} não é maior ou igual a zero!"

        # definindo o objeto
        self.broken_phones = broken_phones

        # Ações
        Phone.all.append(self)
