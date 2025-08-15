# InfoFarma
InfoFarma é um sistema web para farmácias, desenvolvido com Flask e SQLite, que oferece um painel interativo, área de login, cadastro, gerenciamento de perfil e páginas institucionais. O sistema combina backend sólido com um frontend moderno e responsivo para proporcionar uma boa experiência de navegação.
Funcionalidades:
- Página inicial com navegação responsiva (Navbar e Footer)
- Dashboard com seções:
- Produtos
- Dicas de saúde
- Contato
- Informações institucionais
- Sistema de autenticação:
- Registro de usuários
- Login e Logout
- Edição de perfil
- Exclusão de conta
- Páginas institucionais:
- Sobre Nós
- Promoções
- Produtos
- Tratamento de erros com páginas personalizadas (404 e 500)
- Design responsivo com CSS customizado
- Formulário de Newsletter no rodapé
- Mensagens flash para feedback ao usuário

Design:
O layout utiliza HTML5, Jinja2 e CSS3 com:
- Navbar responsiva com menu hambúrguer
- Dashboard com cards e sidebar
- Estilo visual em tons de verde para identidade farmacêutica
- Componentes reutilizáveis: botões, cards e formulários
- Animações e transições suaves em hover
- Layout mobile-first
Arquivo principal de estilo:

`
static/style.css
`
— contém paleta de cores, responsividade e animações
Estrutura de Arquivos:
Arquivo Função
app.py Define rotas, lógica de autenticação e controle de
fluxo
database.py Configura e gerencia a conexão com o banco
SQLite
modelos.py Classe User integrada ao Flask-Login para
autenticação
iniciar.py Script para inicializar o banco a partir do
schema.sql
schema.sql Script SQL para criação das tabelas no banco de
dados
requirements.txt Lista de dependências do projeto
Arquivo Descrição
base.html Estrutura HTML base do site com Navbar e Footer
navbar.html Barra de navegação adaptável a login/usuário visitante
footer.html Rodapé com informações de contato, menu rápido e redes
sociais
dashboard.html Painel do usuário com cards, produtos e formulário de contato
login.html Página de login
register.html Página de cadastro de usuário
produtos.html Página de produtosl
index.html Página inicial da aplicação
404.html Página de erro interno personalizada
promocoes.html Página de promoções
perfil.html Página de perfil
editar
_perfil.html Página para edição de perfil
sobre.html Página institucional "Sobre Nós"
500.html Página de erro interno personalizada
style.css Arquivo de estilo com responsividade e paleta de cores
Tecnologias Utilizadas:
- Backend: Flask, Flask-Login
- Frontend: HTML5, Jinja2, CSS3
- Banco de Dados: SQLite
- Estilo: CSS customizado (`
style.css
`)
- Dependências: definidas em
`requirements.txt`
Rotas Principais:
Rota Descrição
/ Página inicial, exibe index.html
/register Registro de novos usuários
/login Login de usuários
/dashboard Painel do usuário (necessário login)
/logout Faz logout do usuário
/perfil Exibe informações do perfil do usuário
/editar-perfil Edita dados do perfil do usuário
/produtos Lista de produtos
/promocoes Página de promoções
/sobre Página institucional "Sobre Nós"
