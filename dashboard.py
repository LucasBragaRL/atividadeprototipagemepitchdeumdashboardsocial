import requests

class model:
    def __init__(self):
        self.base_url = "https://jsonplaceholder.typicode.com"

    def buscar_dados(self, endpoint):
        try:
            response = requests.get(f"{self.base_url}/{endpoint}", timeout=5)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException:
            return None

class controller:
    def __init__(self):
        self.model = model()

    def listar_usuarios(self):
        return self.model.buscar_dados("users")

    def listar_posts_usuario(self, user_id):
        return self.model.buscar_dados(f"users/{user_id}/posts")

    def listar_comentarios_post(self, post_id):
        return self.model.buscar_dados(f"posts/{post_id}/comments")

class view:
    def __init__(self):
        self.ctrl = controller()

    def exibir_menu(self):
        while True:
            print("\n--- dashboard social ---")
            usuarios = self.ctrl.listar_usuarios()
            
            if not usuarios:
                print("erro ao conectar com a api. tente mais tarde.")
                break

            for u in usuarios:
                print(f"[{u['id']}] {u['name']}")

            escolha = input("\ndigite o id do usuario para ver posts (ou 'sair'): ")
            if escolha.lower() == 'sair':
                break

            posts = self.ctrl.listar_posts_usuario(escolha)
            if posts:
                for p in posts:
                    print(f"\npost {p['id']}: {p['title']}")
                    # exibe o primeiro comentario de cada post como exemplo
                    comentarios = self.ctrl.listar_comentarios_post(p['id'])
                    if comentarios:
                        print(f"  comentario: {comentarios[0]['body'][:50]}...")
            else:
                print("nao foi possivel carregar os posts.")

if __name__ == "__main__":
    app = view()
    app.exibir_menu()