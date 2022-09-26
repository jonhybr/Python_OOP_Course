# Quando usar um método da classe e quando usar um método estático


class Item:
    @staticmethod
    def is_integer():
        """
        Isso deve ter alguma relação com a classe,
        mas não algo que deve ser único por instancia!
        """

    @classmethod
    def instantiate_from_something(cls):
        """
        Isso também deve ter alguma relação com a classe, mas normalmente
        essas são usadas para manipular diferentes estruturas de dados
        para instanciar objetos, como o que fizemos com o CSV.
        """

# Porém, esses também podem ser chamados pelas instancias.


item1 = Item()
item1.is_integer()
item1.instantiate_from_something()
