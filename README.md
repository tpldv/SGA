Sistema de Gestão Acadêmica (SGA)
Descrição
O Sistema de Gestão Acadêmica (SGA) é uma aplicação desenvolvida em Python para facilitar o gerenciamento de informações acadêmicas, incluindo estudantes, professores, turmas, disciplinas e matrículas. O sistema oferece funcionalidades de CRUD (Criar, Ler, Atualizar, Excluir) para cada uma dessas entidades, garantindo a integridade dos dados e evitando a duplicação de códigos entre as diferentes entidades.

Este projeto foi desenvolvido para auxiliar no acompanhamento e administração de dados acadêmicos em um ambiente educacional, utilizando boas práticas de programação, modularidade e persistência de dados com arquivos JSON.

Funcionalidades (CRUD)
Gestão de Estudantes, Professores, Disciplinas, Turmas e Matrículas: 
Validação de códigos: Evita duplicação de códigos entre estudantes, professores, disciplinas e turmas.
Requisitos
Python 3.x
Módulo json (nativo no Python)

Estrutura do Projeto
main.py: Arquivo principal com o menu para navegação entre as entidades.
dados.py: Módulo responsável por carregar, salvar e verificar dados em arquivos JSON.
estudantes.py: Módulo para gerenciar os dados dos estudantes.
professores.py: Módulo para gerenciar os dados dos professores.
disciplinas.py: Módulo para gerenciar os dados das disciplinas.
turmas.py: Módulo para gerenciar os dados das turmas.
matriculas.py: Módulo para gerenciar as matrículas dos estudantes nas turmas.
Exemplos de Uso
Cadastro de um novo professor
Acesse o menu de Professores.
Escolha a opção de Incluir Professor.
Informe o código, nome e CPF do professor.
Listar todos os estudantes
Acesse o menu de Estudantes.
Escolha a opção de Listar Estudantes.

Contribuições são bem-vindas! Siga as instruções abaixo para contribuir:

Faça um fork do projeto.
Crie uma branch para sua feature (git checkout -b feature/nome-da-feature).
Commit suas mudanças (git commit -m 'Adiciona nova feature').
Faça o push para sua branch (git push origin feature/nome-da-feature).
Abra um Pull Request.

Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para mais detalhes.
