# main.py
# Exemplo de aplicação que integra Singleton, Strategy, Observer e Adapter
from database_singleton import Database
from payment_strategy import PixPayment, CardPayment, BoletoPayment, PaymentStrategy
from observer_pattern import Order, Client
from adapter_pattern import ExternalDeliveryService, ExternalDeliveryAdapter

def simulate_order_flow():
    db = Database()

    # 1) Criar um pedido e persistir (Singleton fornece storage global)
    order_data = {
        "customer_name": "Carlos",
        "items": [{"name": "Pizza Margherita", "qty": 1, "price": 38.0}],
        "total": 38.0,
        "status": "Criado"
    }
    order_id = db.add_order(order_data)
    print(f"Pedido criado com ID {order_id}.")

    # 2) Criar objeto observado e clientes (Observer)
    order_obj = Order(order_id=order_id, customer_name=order_data["customer_name"], items=order_data["items"])
    client = Client(name="Carlos", contact="carlos@email.com")
    delivery_contact = Client(name="Entregador", contact="delivery@serv.com")  # exemplo de observador adicional

    order_obj.attach(client)
    order_obj.attach(delivery_contact)

    # 3) Selecionar estratégia de pagamento (Strategy)
    # Exemplo: escolha dinâmica da estratégia
    payment: PaymentStrategy = PixPayment()
    success = payment.pay(amount=order_data["total"], details={"pix_key": "carlos@pix"})

    if success:
        db.update_order(order_id, {"status": "Pago"})
        order_obj.set_status("Pago")

    # 4) Agendar envio usando Adapter para serviço externo
    external_service = ExternalDeliveryService()
    delivery_adapter = ExternalDeliveryAdapter(external_service)

    shipment_info = delivery_adapter.send(order_id=order_id, address="Rua Exemplo, 123")
    db.update_order(order_id, {"shipment": shipment_info})
    order_obj.set_status("Em preparo")

    # 5) Simular transições de status
    order_obj.set_status("Saiu para entrega")
    order_obj.set_status("Entregue")

    # 6) Listar pedidos armazenados no singleton
    print("\nPedidos no 'banco' (singleton):")
    for o in db.list_orders():
        print(o)


if __name__ == "__main__":
    simulate_order_flow()
