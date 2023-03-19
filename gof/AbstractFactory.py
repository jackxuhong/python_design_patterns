from __future__ import annotations
from abc import ABC, abstractmethod

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA1()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ConcreteProductA2()
    
    def create_product_b(self) -> AbstractProductB:
        return ConcreteProductB2()


class AbstractProductA(ABC):
    @abstractmethod
    def useful_fuction_a(self) -> str:
        pass

class ConcreteProductA1(AbstractProductA):
    def useful_fuction_a(self) -> str:
        return "The result of product A1."

class ConcreteProductA2(AbstractProductA):
    def useful_fuction_a(self) -> str:
        return "The result of product A2."


class AbstractProductB(ABC):
    @abstractmethod
    def func_b(self) -> None:
        pass

    @abstractmethod
    def func_bb(self, collaborator: AbstractProductA) -> None:
        pass



class ConcreteProductB1(AbstractProductB):
    def func_b(self) ->  str:
        return  "The result of product B1."
    
    def func_bb(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_fuction_a()
        return f"The result of B1 collaborating with ({result})"


class ConcreteProductB2(AbstractProductB):
    def func_b(self) ->  str:
        return  "The result of product B2."
    
    def func_bb(self, collaborator: AbstractProductA) -> str:
        result = collaborator.useful_fuction_a()
        return f"The result of B2 collaborating with ({result})"


def client_code(factory: AbstractFactory) -> None:
    product_a = factory.create_product_a()
    product_b = factory.create_product_b()

    print(f"{product_b.func_b()}")
    print(f"{product_b.func_bb(product_a)}", end="")

if __name__ == "__main__":
    print("Client: testing client code wit the 1st factory type:")
    client_code(ConcreteFactory1())

    print("\n")

    print("Client: testing the same client code with the 2nd factory type: ")
    client_code(ConcreteFactory2())

