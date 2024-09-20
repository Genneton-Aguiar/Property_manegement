1. Gerenciamento de Inquilinos:
1.1 Cadastro de Inquilinos:

[CHECK] Endpoints para criar, listar, atualizar e deletar inquilinos. Campos devem incluir nome completo, CPF/CNPJ, telefone, e-mail e endereço.
[CHECK] Relacionamento com o imóvel alugado e contratos vinculados.

1.2 Histórico de Inquilinos:

[CHECK] Rastrear o histórico dos inquilinos, incluindo todos os contratos de aluguel e seus status (adimplente/inadimplente).

1.3 Filtragem de Inquilinos:
[CHECK] Implementar filtros para listar inquilinos por adimplentes, inadimplentes, nome, cpf.

2. Gerenciamento de Proprietários:
2.1 Cadastro de Proprietários:

[CHECK] Endpoints para criar, listar, atualizar e deletar proprietários dos imóveis. Campos devem incluir nome completo, CPF/CNPJ, telefone, e-mail e endereço.

2.2 Relatório de Recebimentos:
[] Gerar relatório para os proprietários, detalhando os recebimentos dos aluguéis e repasses mensais, deduzindo taxas da imobiliária.

3. Gerenciamento de property
3.1 CRUD de Imóveis:

[CHECK] Endpoints para cadastrar, listar, atualizar e deletar imóveis. Cada imóvel deve conter informações como endereço, tipo (apartamento, casa, comercial), número de quartos, vagas de garagem, valor do aluguel, status (disponível, alugado, manutenção), e proprietário responsável.

3.2 Busca e Filtros de Imóveis:

[CHECK] Implementar busca por localidade, tipo de imóvel, valor do aluguel, número de quartos e vagas de garagem.

[CHECK] Filtrar por imóveis disponíveis ou alugados.

4. Gerenciamento de Contratos de Aluguel:
4.1 Cadastro de Contratos de Locação:

[CHECK] Endpoint para registrar um contrato de aluguel, associando um imóvel a um inquilino e definindo o período de vigência, data de início, data de término, valor mensal, reajustes previstos e 
???forma de pagamento.???

4.2 Histórico de Contratos:

[CHECK] Manter um histórico de contratos encerrados, com informações como datas de início e término, valores pagos, e observações sobre a devolução do imóvel.

5. Controle de Pagamentos e Repasses:

5.1 Registro de Pagamentos:

[CHECK] Endpoint para registrar o pagamento do aluguel pelo inquilino. Campos devem incluir o valor pago, data de pagamento, e método (boleto, transferência bancária).

[] Marcar o contrato como adimplente ou inadimplente de acordo com os pagamentos registrados.

5.2 Repasses a Proprietários:

[] Funcionalidade para calcular e registrar os repasses mensais para os proprietários, deduzindo automaticamente a taxa de administração da imobiliária.

6. Autenticação e Autorização:

6.1 Cadastro de Usuários:

[] O sistema deve permitir o cadastro de usuários com diferentes níveis de acesso: administradores, gestores e operadores.
[] Autenticação JWT: Implementar autenticação para garantir que apenas usuários autenticados possam acessar ou modificar dados do sistema.

6.2 Controle de Acesso:
[] Administradores devem ter acesso total ao sistema, incluindo a gestão de imóveis, contratos e inquilinos.
[] Gestores podem gerenciar imóveis e contratos.
[] Operadores podem apenas registrar pagamentos e gerar relatórios.
