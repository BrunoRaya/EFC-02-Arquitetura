# RESUMO — Estudo e Aplicação de Padrões de Projeto

## Introdução
Este documento apresenta o estudo e a aplicação prática de quatro padrões de projeto implementados em Python: **Singleton**, **Strategy**, **Observer** e **Adapter**.  
A aplicação desenvolvida é um **sistema de notificações de pedidos online**, que simula o fluxo de criação, pagamento, acompanhamento e entrega de pedidos.  
O objetivo é demonstrar como cada padrão contribui para uma arquitetura de software mais **organizada, flexível e manutenível**.

---

## 1. Singleton
### Propósito
Garante que uma classe tenha **apenas uma instância** e fornece um ponto de acesso global a ela.  
Esse padrão é útil para recursos centralizados, como conexões de banco de dados, cache, ou gerenciamento de configurações.

### Estrutura
O Singleton é implementado controlando a criação de objetos com o método `__new__`, armazenando a instância em uma variável de classe e retornando sempre a mesma referência.

### Aplicação no Projeto
No arquivo `database_singleton.py`, o padrão Singleton foi usado na classe `Database`, responsável por armazenar os pedidos.  
Isso garante que todas as partes do sistema utilizem o **mesmo repositório de dados**, evitando inconsistências e duplicações.

### Benefícios
- Acesso centralizado e consistente aos dados.  
- Facilidade de manutenção e controle do estado global.  

### Sem o padrão
Seria necessário passar manualmente o objeto de armazenamento entre classes e funções, tornando o código mais **acoplado e confuso**.

---

## 2. Strategy
### Propósito
Define uma **família de algoritmos** (estratégias) e permite que sejam trocados em tempo de execução, sem alterar o código do cliente.  
É ideal para situações em que há várias formas de realizar uma mesma ação, mas com regras diferentes.

### Estrutura
É composta por uma interface abstrata (`PaymentStrategy`) e múltiplas implementações concretas (`PixPayment`, `CardPayment`, `BoletoPayment`).

### Aplicação no Projeto
No arquivo `payment_strategy.py`, cada classe representa um método de pagamento.  
No código principal (`main.py`), a escolha da estratégia é feita dinamicamente, permitindo que o sistema aceite **novos métodos de pagamento** sem alterações estruturais.

### Benefícios
- Flexibilidade na troca de algoritmos.  
- Isolamento de regras específicas em classes independentes.  
- Redução de condicionais extensas no código.

### Sem o padrão
O código teria diversos `if/else` para lidar com cada tipo de pagamento, dificultando a manutenção e a inclusão de novos métodos.

---

## 3. Observer
### Propósito
Permite que **vários objetos sejam notificados automaticamente** quando o estado de outro objeto muda.  
É ideal para sistemas que exigem reações automáticas a eventos, como interfaces gráficas ou notificações.

### Estrutura
O padrão define um **Sujeito** que mantém uma lista de **Observadores**. Quando o estado muda, todos os observadores são notificados.

### Aplicação no Projeto
No arquivo `observer_pattern.py`, a classe `Order` representa o sujeito observado, e a classe `Client` atua como observador.  
Quando o status do pedido muda (ex: "Pago", "Entregue"), os clientes recebem notificações automáticas.

### Benefícios
- Baixo acoplamento entre emissor e receptores.  
- Facilidade para adicionar novos tipos de observadores.  
- Melhoria na comunicação entre objetos.

### Sem o padrão
As notificações precisariam ser enviadas manualmente para cada cliente, tornando o código repetitivo e difícil de expandir.

---

## 4. Adapter
### Propósito
Permite que **interfaces incompatíveis trabalhem juntas**, convertendo a interface de uma classe para outra esperada pelo sistema cliente.

### Estrutura
Um **Adapter** traduz chamadas entre a interface do sistema interno e a de um componente externo (ou legado).

### Aplicação no Projeto
No arquivo `adapter_pattern.py`, a classe `ExternalDeliveryAdapter` adapta a interface do serviço externo `ExternalDeliveryService` para o formato usado internamente pelo sistema.  
Assim, o código principal pode solicitar entregas sem precisar conhecer a estrutura da API externa.

### Benefícios
- Facilita integrações com sistemas de terceiros.  
- Mantém o código interno estável mesmo com mudanças externas.  
- Evita duplicação de lógica de conversão.

### Sem o padrão
Seria necessário alterar o código interno sempre que a API externa fosse modificada, o que geraria **acoplamento e fragilidade**.

---

## Comparações e Relações entre os Padrões
- **Singleton × Strategy:** O primeiro centraliza dados; o segundo descentraliza comportamentos. Ambos reduzem redundância.  
- **Observer × Adapter:** Enquanto Observer lida com **eventos internos**, Adapter lida com **integrações externas**.  
- **Strategy × Observer:** Ambos promovem baixo acoplamento e facilitam extensões futuras.

Esses padrões podem coexistir de forma harmônica em uma mesma aplicação, como demonstrado no projeto.

---

## Conclusão
A aplicação dos padrões **Singleton**, **Strategy**, **Observer** e **Adapter** resultou em um sistema **modular, extensível e de fácil manutenção**.  
Cada padrão resolveu um problema específico de design, melhorando a clareza e a organização do código.

Sem o uso dos padrões, o sistema apresentaria:
- Estruturas mais rígidas e acopladas;  
- Dificuldade para adicionar novas funcionalidades;  
- Repetição de lógica e menor reuso de código.

O estudo e a implementação prática reforçam a importância dos **padrões de projeto** como ferramentas fundamentais na engenharia de software, proporcionando **soluções elegantes e sustentáveis** para problemas recorrentes de desenvolvimento.
