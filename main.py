from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Component(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor) -> None:
        pass


class ConcreteComponentA(Component):

    def accept(self, visitor: Visitor) -> None:

        visitor.visit_concrete_component_a(self)

    def exclusive_method_of_concrete_component_a(self) -> str:

        return "A"


class ConcreteComponentB(Component):

    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def special_method_of_concrete_component_b(self) -> str:
        return "B"


class Visitor(ABC):

    @abstractmethod
    def visit_concrete_component_a(self, element: ConcreteComponentA) -> None:
        pass

    @abstractmethod
    def visit_concrete_component_b(self, element: ConcreteComponentB) -> None:
        pass



class Конкретный_посетитель1(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + Конкретный_посетитель1")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + Конкретный_посетитель1")


class Конкретный_посетитель2(Visitor):
    def visit_concrete_component_a(self, element) -> None:
        print(f"{element.exclusive_method_of_concrete_component_a()} + Конкретный_посетитель2")

    def visit_concrete_component_b(self, element) -> None:
        print(f"{element.special_method_of_concrete_component_b()} + Конкретный_посетитель2")


def client_code(components: List[Component], visitor: Visitor) -> None:


    for component in components:
        component.accept(visitor)


if __name__ == "__main__":
    components = [ConcreteComponentA(), ConcreteComponentB()]

    print("Клиентский код работает со всеми посетителями через базовый интерфейс посетителя:")
    visitor1 = Конкретный_посетитель1()
    client_code(components, visitor1)

    print("Это позволяет одному и тому же клиентскому коду работать с разными типами посетителей:")
    visitor2 = Конкретный_посетитель2()
    client_code(components, visitor2)