# Dashboard Social - Startup 

Projeto de prototipagem para centralizar postagens e perfis usando a API JSONPlaceholder.

## Arquitetura (MVC)
O sistema segue o padrão Model-View-Controller para separar a lógica de dados da interface.
- **Model**: Gerencia as requisições HTTP e a conexão com o servidor.
- **View**: Interface de usuário que roda diretamente no terminal.
- **Controller**: Faz a ponte entre o modelo de dados e a visualização na tela.

## Modelagem e Classes
- **Usuário**: atributos id, nome e email.
- **Postagem**: atributos id, id_usuario, título e corpo.
- **Associação**: Um Usuário possui várias Postagens (Relação 1:N).

## Resiliência e Falhas
Para evitar travamentos e garantir a estabilidade do protótipo, implementamos:
- **Timeouts**: Definido um limite de 5 segundos para resposta da API.
- **Try/Catch**: Tratamento de exceções para erros de rede e códigos de erro HTTP (ex: 404).
