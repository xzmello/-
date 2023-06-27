print('===========================\n1 - Cadastrar Empresa\n2 - Cadastrar Usuário\n3 - Registrar Compra de um Usuário\n4 - Mostrar Saldo de um Usuário\n5 - Resgatar Saldo de um Usuário\n6 - Excluir Empresa\n0 - Sair\n===========================')

empresas = {
    'ALB': 10,
    'MM': 8,
    'CZB': 5
}
usuarios = {

}
    
opcao = int(input('Digite uma das opções: '))

while opcao != 0:
    if opcao == 1:
        CadastroEmpresa = input('Digite o nome da empresa: ').upper()
        CashBackEmpresa = int(input('Digite quantos porcento de cashback sera concedido: '))
        empresas[CadastroEmpresa] = CashBackEmpresa
    elif opcao == 2:
        usuario = input('Digite o id de usuario: ').upper()
        usuarios[usuario] = 0
        print(usuarios)
    elif opcao == 3:
        print('Usuarios: ')
        for u in usuarios:
            print(u)
        SolicId = input('Digite o id do usuario: ').upper()
        ValorCompra = float(input('Digite o valor da compra: '))
        print('Empresas: ')
        for e in empresas:
            print(e)
        SolicEmpresa = input('Dgite o nome da empresa onde fez a compra: ').upper()
        cashbackpercent = empresas[SolicEmpresa]
        Desconto = (ValorCompra * cashbackpercent)/100
        
        usuarios[SolicId] = ValorCompra - Desconto
        print('usuarios: ',usuarios)
    elif opcao == 4:
        print('Usuarios: ')
        for uu in usuarios:
            print(uu)
        DadosUsuario = input('Digite o id de usuario: ').upper()
        if DadosUsuario not in usuarios:
            print('usuario não cadastrado!')
        elif DadosUsuario in usuarios:
            print(f'O usuario {DadosUsuario} possui um saldo de: R${usuarios[DadosUsuario]}')
            print(usuarios)
    elif opcao == 5:
        print('Usuarios: ')
        for uuu in usuarios:
            print(uuu)
            uuu = uuu.values()
            print(uuu)
        iduser = input('Digite o id do usuario a ser resgtado a quantia: ').upper()
        if iduser not in usuarios:
            print('Usuario nao cadastrado!')
        elif iduser in usuarios:
            print('Saldo do usuario selecionado: ',usuarios[iduser])
            confirm = input('Deseja resgatar o saldo? s/sim  n/nao:  ').upper()
            if confirm == 'S' or 'SIM':
                usuarios[iduser] = 0
            elif confirm == 'N' or 'NAO':
                continue
    elif opcao == 6:
        print('Empresas: ')
        for ee in empresas:
            print(ee)
        empresaExcluida = input('Digite qual empresa deseja excluir: ').upper()
        confirmexclusao = input('Deseja mesmo excluir a empresa? s/sim n/nao:  ').upper()
        if confirmexclusao == 'S' or 'SIM':
            del empresas[empresaExcluida]
            print(empresas)
        elif confirmexclusao == 'N' or 'NAO':
            continue
    opcao = int(input('Digite uma das opções: '))

