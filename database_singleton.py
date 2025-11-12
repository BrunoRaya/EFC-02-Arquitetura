# database_singleton.py
# Implementação do padrão Singleton: garante uma única instância de "Database"
from typing import List, Dict, Any

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._init_storage()
        return cls._instance

    def _init_storage(self):
        self.orders: List[Dict[str, Any]] = []
        self.next_id = 1

    def add_order(self, order_data: Dict[str, Any]) -> int:
        order_data = order_data.copy()
        order_data['id'] = self.next_id
        self.orders.append(order_data)
        self.next_id += 1
        return order_data['id']

    def get_order(self, order_id: int) -> Dict[str, Any] | None:
        for o in self.orders:
            if o['id'] == order_id:
                return o
        return None

    def update_order(self, order_id: int, updates: Dict[str, Any]) -> bool:
        o = self.get_order(order_id)
        if o is None:
            return False
        o.update(updates)
        return True

    def list_orders(self) -> List[Dict[str, Any]]:
        return list(self.orders)
