import pandas as pd
from datetime import datetime

class AnalisadorFinancas:
    def __init__(self):
        self.gastos = []

    def adicionar_gasto(self, categoria, valor, data=None):
        """Adiciona um novo registro de gasto."""
        if data is None:
            data = datetime.now().strftime("%Y-%m-%d")
        
        self.gastos.append({
            'Data': data,
            'Categoria': categoria.capitalize(),
            'Valor': float(valor)
        })

    def gerar_relatorio(self):
        """Processa os dados e exibe estatísticas."""
        if not self.gastos:
            print("Nenhum dado para analisar ainda!")
            return

        df = pd.DataFrame(self.gastos)
        
        total_gasto = df['Valor'].sum()
        por_categoria = df.groupby('Categoria')['Valor'].sum().sort_values(ascending=False)
        media_gasto = df['Valor'].mean()

        print("\n--- 📊 RELATÓRIO FINANCEIRO ---")
        print(f"Total acumulado: R$ {total_gasto:.2f}")
        print(f"Média por transação: R$ {media_gasto:.2f}")
        print("\n--- Gastos por Categoria ---")
        print(por_categoria.to_string())
        
        maior_gasto = df.loc[df['Valor'].idxmax()]
        print(f"\n⚠️ Maior gasto único: R$ {maior_gasto['Valor']:.2f} em {maior_gasto['Categoria']}")

if __name__ == "__main__":
    app = AnalisadorFinancas()

    app.adicionar_gasto("Alimentação", 55.90)
    app.adicionar_gasto("Transporte", 15.00)
    app.adicionar_gasto("Lazer", 200.00)
    app.adicionar_gasto("Alimentação", 42.10)
    app.adicionar_gasto("Educação", 150.00)

    app.gerar_relatorio()
