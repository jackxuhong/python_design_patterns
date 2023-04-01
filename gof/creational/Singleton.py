from threading import Lock, Thread


class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_logic(self):
        print(f"Some logic value: {self.value}...")


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == '__main__':
    s1 = Singleton('test1')
    s2 = Singleton('test2')

    if id(s1) == id(s2):
        print("Singleton works!")
    else:
        print("Singleton fails!")

    s1.some_logic()
    s2.some_logic()

    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
 