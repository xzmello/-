Empresas = {
    'ALB': 10,
    'MM': 8,
    'CZB': 5
}
Usuarios = {

}

def ExibirMenu():
    print('===========================')
    print('1 - Cadastrar Empresa')
    print('2 - Cadastrar Usuário')
    print('3 - Registrar Compra de um Usuário')
    print('4 - Mostrar Saldo de um Usuário')
    print('5 - Resgatar Saldo de um Usuário')
    print('6 - Excluir Empresa')
    print('7 - Excluir Usuário')
    print('8 - Mostrar Empresas')
    print('9 - Mostrar Usuários')
    print('0 - Sair')
    print('===========================')

def CadastrarEmpresa():   
    Empresa = input('Digite o nome da empresa: ').upper()
    CashBackEmpresa = int(input('Digite quantos porcento de cashback sera concedido: '))
    Empresas[Empresa] = CashBackEmpresa

def CadastrarUsuario():
    Usuario = input('Digite o ID do usuario a ser cadastrado: ').upper()
    Usuarios[Usuario] = 0
    print(Usuarios)

def RegistrarCompra():
    print('Usuarios:')
    for u in Usuarios:
        print(u)
    SolicID = input('Digite o ID do usuario: ').upper()
    ValorCompra = float(input('Digite o valor da compra: '))
    print('Empresas: ')
    for e in Empresas:
        print(e)
    SolicEmpresa = input('Digite o nome da empresa onde fez a compra: ').upper()
    CashBackPercent = Empresas[SolicEmpresa]
    Desconto = (ValorCompra * CashBackPercent)/100
    Usuarios[SolicID] = ValorCompra - Desconto
    print('Usuarios: ', Usuarios)

def MostrarSaldo():
    print('Usuarios: ')
    for uu in Usuarios:
        print(uu)
    DadosUsuario = input('Digite o ID do usuario que quer ver o saldo: ').upper()
    if DadosUsuario not in Usuarios:
        print('Usuario não cadastrado!')
    elif DadosUsuario in Usuarios:
        print(f'O saldo do usuario: {DadosUsuario} é: {Usuarios[DadosUsuario]}')
        print(Usuarios)
    else: 
        return


def ResgatarSaldo():
    print('Usuarios:')
    for uuu in Usuarios:
        print(uuu)
    IDUser = input('Digite o ID do usuario que quer resgatar o saldo: ').upper()
    if IDUser not in Usuarios:
        print('Usuario não está cadastrado: ')
    elif IDUser in Usuarios:
        print(f'O saldo do usuario selecionado é: {Usuarios[IDUser]}')
        ConfirmResgate = input('Deseja mesmo Resgatar o Saldo deste usuario para realizar a compra: Sim ou Não (S/N): ').upper()
        if ConfirmResgate == 'S' or ConfirmResgate == 'SIM':
            Usuarios[IDUser] = 0
        elif ConfirmResgate == 'N' or ConfirmResgate == 'NAO':
            return
        else:
            return
    else:
        return
    
def ExcluirEmpresa():
    print('Empresas:')
    for e in Empresas:
        print(e)
    EmpresaExcluida = input('Digite o ID da empresa que deseja excluir: ').upper()
    if EmpresaExcluida not in Empresas:
        print('A empresa Solicitada nao está registrada!')
    elif EmpresaExcluida in Empresas:
        del Empresas[EmpresaExcluida]
        print(Empresas)
    else:
        return

def ExcluirUsuario():
    print('Usuarios:')
    for uuuu in Usuarios:
        print(uuuu)
    IDExclusao = input('Digite o ID do usuario a ser excluido: ').upper()
    if IDExclusao not in Usuarios:
        print('Usuario nao está cadastrado: ')
    elif IDExclusao in Usuarios:
        del Usuarios[IDExclusao]
    else: 
        return

def MostrarEmpresas():
    for ee in Empresas:        
        print(f'Empresa: {ee} -- Valor do cashback oferecido: {Empresas[ee]}')

def MostrarUsuarios():
    for uuuuu in Usuarios:
        print(f'Usuarios: {uuuuu} -- Valor do saldo: {Usuarios[uuuuu]} ')
    
opcao = None

while opcao != 0:
    
    ExibirMenu()
    opcao = int(input('Digite uma das opções: '))

    if opcao == 1:
        CadastrarEmpresa()
    elif opcao == 2:
        CadastrarUsuario()
    elif opcao == 3:
        RegistrarCompra()
    elif opcao == 4:
        MostrarSaldo()
    elif opcao == 5:
        ResgatarSaldo()
    elif opcao == 6:
        ExcluirEmpresa()
    elif opcao == 7:
        ExcluirUsuario()
    elif opcao == 8:
        MostrarEmpresas()
    elif opcao == 9:
        MostrarUsuarios()
    elif opcao == 0:
        print('Fim!')
    else:
        print('Opção invalida, Tente novamente!')
        continue 
