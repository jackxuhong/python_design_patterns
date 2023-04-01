class Target:
    def request(self) -> str:
        return "Target: default behavior"


class Adaptee:
    def specific_request(self) -> str:
        return "specific behavior"


class Adapter(Target, Adaptee):
    def request(self) -> str:
        return f"Adapter: {self.specific_request()}"


def client_code(target: "Target") -> None:
    print(target.request())

if __name__ == "__main__":
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    print(adaptee.specific_request())

    adapter = Adapter()
    client_code(adapter)
