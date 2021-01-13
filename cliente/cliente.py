import json
import requests
url = 'http://localhost:5000/'

def menu():
    print("-------------  ESCOLHA UMA DAS OPÇÕES -------------")
    print("1) ADICIONAR PRODUTO")
    print("2) LISTAR PRODUTOS")
    print("3) PROCURAR PRODUTO")
    print("4) REMOVER PRODUTO")
    print("5) ATUALIZAR PRODUTO")
    print("0) SAIR")
    opcao = int(input())
    print('\n')
    return opcao

def main():
    escolha = -1

    while escolha != 0:
        try:
            escolha = menu()
        except:
            print("Digite um valor entre 0 e 5.\n\n")

        if(escolha == 1):   
            print("-------------  CADASTRO DE PRODUTO -------------")      
            nome = input("Digite o nome do produto: ")            
            preco = input("Digite o preço do produto: ")            
            quantidade = input("Digite a quantidade de produtos disponíveis: ")
            
            try:
                produto = requests.post(url + 'produto', json={
                    "name": nome,
                    "preco": preco,
                    "quantidade": quantidade
                })

                print("Produto cadastrado com sucesso.\n")
            except:
                print("Erro ao cadastrar produto, verifique os dados e tente novamente.\n")
        elif(escolha==2):
            i = 1
            produtos = requests.get(url + 'produto')
            produtos = json.loads(produtos.content.decode())
            print('------------- PRODUTOS -------------')

            for produto in produtos['Produtos']:
                
                print('------- Produto ', i, ' -------')
                print("id: ", produto['id'])
                print("Nome: ", produto['name'])
                print("Preço: ", produto['preco'])
                print("Quantidade: ", produto['quantidade'])
                i+=1
                print('\n')
        elif(escolha == 3):
            prod = input("Digite o id do produto a ser encontrado: ")
            
            try:
                produto = requests.get(url + 'produto/'+prod)            
                produto = json.loads(produto.content.decode())            

                for prod in produto['Produto']:
                    
                    print('------- Produto -------')
                    print("id: ", prod['id'])
                    print("Nome: ", prod['name'])
                    print("Preço: ", prod['preco'])
                    print("Quantidade: ", prod['quantidade'])                
                    print('\n')    
            except:
                print('Erro ao recuperar produto, verifique os dados e tente novamente.\n')
        elif(escolha == 4):
            prod = input("Digite o id do produto a ser removido: ")

            try:
                produto = requests.delete(url + 'produto/'+prod)
                if(404 == produto.status_code):
                    print("Produto não encontrado, por favor digite um id válido.")
                else:
                    print("Produto removido com sucesso.")
            except:
                print("Erro ao cadastrar produto, verifique os dados e tente novamente.\n")
        elif(escolha == 5):
            opc = input("Digite o id do produto a ser atualizado: ")



            nome = input("Digite o novo nome: ")
            preco = input("Digite o novo preco: ")
            quantidade = input("Digite a nova quantidade: ")
            
            if(nome == '' and preco == '' and quantidade == ''):
                print("Nada alterado pois nenhum dado foi informado.")
            elif(nome == '' and preco == ''):
                try:
                    produto = requests.put(url + 'produto/'+opc, json={                        
                        "quantidade": int(quantidade)
                    })

                    print("Produto atualizado com sucesso.\n")
                except:
                    print("Erro ao cadastrar produto, verifique os dados e tente novamente.\n")
            elif(nome == '' and quantidade == ''):
                try:
                    produto = requests.put(url + 'produto/'+opc, json={                        
                        "preco": int(preco)
                    })

                    print("Produto atualizado com sucesso.\n")
                except:
                    print("Erro ao cadastrar produto, verifique os dados e tente novamente.\n")
            elif (quantidade == '' and preco == ''):
                try:
                    produto = requests.put(url + 'produto/'+opc, json={                        
                        "name": nome
                    })

                    print("Produto atualizado com sucesso.\n")
                except:
                    print("Erro ao cadastrar produto, verifique os dados e tente novamente.\n")
            elif (nome == ''):
                try:
                    produto = requests.put(url + 'produto/'+opc, json={   
                        "preco": int(preco),                     
                        "quantidade": int(quantidade)
                    })

                    print("Produto atualizado com sucesso.\n")
                except:
                    print("Erro ao cadastrar produto, verifique os dados e tente novamente.\n")
            elif quantidade == '':
                try:
                    produto = requests.put(url + 'produto/'+opc, json={   
                        "name": nome,
                        "preco": int(preco),                                        
                    })

                    print("Produto atualizado com sucesso.\n")
                except:
                    print("Erro ao cadastrar produto, verifique os dados e tente novamente.\n")
            elif preco == '':
                try:
                    produto = requests.put(url + 'produto/'+opc, json={   
                        "name": nome,                     
                        "quantidade": int(quantidade)
                    })

                    print("Produto atualizado com sucesso.\n")
                except:
                    print("Erro ao cadastrar produto, verifique os dados e tente novamente.\n")
            else:
                try:
                    produto = requests.put(url + 'produto/'+opc, json={   
                        "name": nome,
                        "preco": int(preco),                     
                        "quantidade": int(quantidade)
                    })

                    print("Produto atualizado com sucesso.\n")
                except:
                    print("Erro ao cadastrar produto, verifique os dados e tente novamente.\n")
        


            
        

main()