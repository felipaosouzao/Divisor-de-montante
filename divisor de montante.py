import os

def _format_eur(value: float) -> str:
    s = f"{value:,.2f}"
    s = s.replace(',', 'X').replace('.', ',').replace('X', '.')
    return s

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def distribute(amount: float, categories: list[tuple[str, float]]) -> list[tuple[str, float, float]]:
    allocations = []
    for name, pct in categories:
        allocated = amount * (pct / 100.0)
        allocations.append((name, pct, allocated))
    return allocations


def main() -> None:
    print("Este é um programa para dividir um montante em euros, por porcentagens ou subtrair valores.")
    print("1 - Digite o montante total em euros\n2 - Para cada categoria, defina um nome e sua porcentagem ou valor correspondente")
    print("3 - Para finalizar a lista de categorias, deixe o nome em branco e pressione Enter")
    print("(Você usará Enter duas vezes: uma para continuar e outra para finalizar as categorias.)")
    input("Pressione Enter para continuar...")
    limpar()

#loop principal 
    while True:  
        while True:
            s = input("Digite o montante total: ").strip()
            try:
                amount = float(s.replace(',', '.'))
                break
            except Exception:
                print("Valor inválido. Tente novamente (use ponto ou vírgula para decimais).")

        while True:
            mode = input("Deseja dividir por porcentagens ou por valores? (p/v): ").strip().lower()
            if mode in ('p', 'porcentagem', 'porcentagens'):
                mode = 'p'
                break
            if mode in ('v', 'valor', 'valores'):
                mode = 'v'
                break
            print("Opção inválida. Digite 'p' para porcentagens ou 'v' para valores.")

        category_names: list[str] = []
        while True:
            name = input("Nome da categoria (Enter vazio para finalizar): ").strip()
            if name == "":
                break
            category_names.append(name)

        if not category_names:
            print("Nenhuma categoria fornecida. Saindo.")
            return

    
        while True:
            if mode == 'p':
                categories: list[tuple[str, float]] = []
                for name in category_names:
                    while True:
                        sp = input(f"Porcentagem para '{name}': ").strip()
                        try:
                            pct = float(sp.replace(',', '.'))
                            if pct < 0:
                                print("Porcentagem inválida. Insira um número positivo.")
                                continue
                            break
                        except Exception:
                            print("Porcentagem inválida. Insira um número.")
                    categories.append((name, pct))

                total_pct = sum(p for _, p in categories)
                if total_pct == 0:
                    print("Soma das porcentagens é 0. Por favor, insira novas porcentagens.")
                    continue

                if total_pct > 100.0:
                    while True:
                        choice = input(
                            f"A soma das porcentagens é {total_pct:.2f}%, maior que 100%. Isso fará o restante ser negativo.\n"
                            "Deseja continuar mesmo assim ou corrigir as porcentagens? (continuar/corrigir): "
                        ).strip().lower()
                        if choice in ('continuar', 'c'):
                            break
                        if choice in ('corrigir', 'corr'):
                            print("\nVamos corrigir as porcentagens...\n")
                            break
                        print("Opção inválida. Digite 'continuar' ou 'corrigir'.")
                    if choice in ('corrigir', 'corr'):
                        continue

                allocations = distribute(amount, categories)

            else:  
                values: list[tuple[str, float]] = []
                for name in category_names:
                    while True:
                        sv = input(f"Valor em euros para '{name}': ").strip()
                        try:
                            val = float(sv.replace(',', '.'))
                            if val < 0:
                                print("Valor inválido. Insira um número não-negativo.")
                                continue
                            break
                        except Exception:
                            print("Valor inválido. Insira um número.")
                    values.append((name, val))

                total_val = sum(v for _, v in values)
                if total_val == 0:
                    print("Soma dos valores é 0. Por favor, insira novos valores.")
                    continue

                if total_val > amount:
                    while True:
                        choice = input(
                            f"A soma dos valores é {total_val:.2f}€, maior que o montante {amount:.2f}€.\n"
                            "Deseja continuar mesmo assim (restante negativo) ou corrigir os valores? (continuar/corrigir): "
                        ).strip().lower()
                        if choice in ('continuar', 'c'):
                            break
                        if choice in ('corrigir', 'corr'):
                            print("\nVamos corrigir os valores...\n")
                            break
                        print("Opção inválida. Digite 'continuar' ou 'corrigir'.")
                    if choice in ('corrigir', 'corr'):
                        continue

               
                allocations = []
                for name, val in values:
                    pct = (val / amount * 100.0) if amount != 0 else 0.0
                    allocations.append((name, pct, val))

            #exibir resultados 
            print("\nResultado:")
            for name, pct, allocated in allocations:
                print(f"- {name}: {pct:.2f}% -> € {_format_eur(allocated)}")

            sum_alloc = sum(a for _, _, a in allocations)
            print(f"\nTotal alocado: € {_format_eur(sum_alloc)}")
            diff = amount - sum_alloc
            print(f"Restante: € {_format_eur(diff)}")

           
            print("\nOpções:")
            print("1 - Finalizar")
            print("2 - Refazer tudo (montante e categorias)")
            print("3 - Refazer apenas valores/porcentagens (manter montante e nomes)")
            while True:
                opt = input("Escolha 1, 2 ou 3: ").strip().lower()
                if opt in ('1', 'finalizar', 'f'):
                    return
                if opt in ('2',):
                    #reiniciar o loop principal 
                    break
                if opt in ('3',):
                    #refazer apenas valores/porcentagens 
                    print("\nRefazendo apenas valores/porcentagens mantendo montante e categorias...\n")
                    break
                print("Opção inválida. Digite 1, 2 ou 3.")

            if opt == '2':
                #volta ao início do loop principal
                break
            


if __name__ == "__main__":
    main()
