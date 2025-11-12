# observer_pattern.py
# Implementação do padrão Observer: observadores (clientes) são notificados quando o pedido muda de status
from typing import Protocol, List, Any, Dict


class Observer(Protocol):
    def update(self, subject: "Order", event: str) -> None:
        ...


class Order:
    def __init__(self, order_id: int, customer_name: str, items: List[Dict[str, Any]]):
        self.id = order_id
        self.customer_name = customer_name
        self.items = items
        self.status = "Criado"
        self._observers: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        if observer in self._observers:
            self._observers.remove(observer)

    def notify(self, event: str) -> None:
        for obs in list(self._observers):
            try:
                obs.update(self, event)
            except Exception:
                pass

    def set_status(self, new_status: str) -> None:
        self.status = new_status
        self.notify(event=f"status_atualizado:{new_status}")


class Client:
    def __init__(self, name: str, contact: str):
        self.name = name
        self.contact = contact

    def update(self, subject: Order, event: str) -> None:
        print(f"[Notificação -> {self.name}] Pedido #{subject.id} - novo status: {subject.status} (evento: {event})")
