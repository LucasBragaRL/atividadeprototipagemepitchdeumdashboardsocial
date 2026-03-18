# Dashboard Social - Startup 

[cite_start]Projeto de prototipagem para centralizar postagens e perfis usando a API JSONPlaceholder[cite: 10, 12].

## Arquitetura (MVC)
[cite_start]O sistema segue o padrão Model-View-Controller para separar a lógica de dados da interface[cite: 27].
- [cite_start]**Model**: Gerencia as requisições HTTP[cite: 27].
- [cite_start]**View**: Interface de usuário no terminal[cite: 27].
- [cite_start]**Controller**: Faz a ponte entre os dados e a tela[cite: 27].

## Modelagem e Classes
- [cite_start]**Usuário**: id, nome, email[cite: 22, 23].
- [cite_start]**Postagem**: id, id_usuario, título, corpo[cite: 22, 23].
- [cite_start]**Associação**: Um Usuário possui várias Postagens (1:N)[cite: 24].

## Resiliência e Falhas
Para evitar travamentos, implementamos:
- [cite_start]**Timeouts**: Limite de 5 segundos para resposta da API[cite: 30].
- [cite_start]**Try/Catch**: Tratamento de erros de rede e códigos HTTP (ex: 404)[cite: 30].
