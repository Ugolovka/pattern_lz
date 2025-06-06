import visitor

if __name__ == "__main__":
    print("Запуск client_code из отдельного файла...")
    visitor.client_code([visitor.ConcreteComponentA(), visitor.ConcreteComponentB()], visitor.Конкретный_посетитель1())
    visitor.client_code([visitor.ConcreteComponentA(), visitor.ConcreteComponentB()], visitor.Конкретный_посетитель2())
