# Notificador de Pedidos (Exemplo de Padrões de Projeto em Python)

## Visão geral
Aplicação didática que simula um sistema de pedidos com a aplicação de 4 padrões de projeto:
- **Singleton** (`database_singleton.py`) — armazenamento compartilhado dos pedidos.
- **Strategy** (`payment_strategy.py`) — diferentes métodos de pagamento (Pix, Cartão, Boleto).
- **Observer** (`observer_pattern.py`) — notificações para clientes/observadores sobre alterações de status do pedido.
- **Adapter** (`adapter_pattern.py`) — integração com um serviço de entrega externo que possui interface diferente.

## Estrutura
notificador_pedidos/
├── main.py
├── database_singleton.py
├── payment_strategy.py
├── observer_pattern.py
├── adapter_pattern.py
├── README.md
└── RESUMO.md

## Requisitos
- Python 3.8+ (testado com Python 3.10)
- Nenhuma dependência externa

## Como executar
1. Salvar os arquivos na mesma pasta.
2. No terminal, executar:
```bash
python main.py
