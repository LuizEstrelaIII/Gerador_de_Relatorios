from django.shortcuts import render
from .forms import RelatorioForm
import matplotlib.pyplot as plt
import io
import urllib, base64
import pandas as pd

def index(request):
    if request.method == 'POST':
        form = RelatorioForm(request.POST)
        if form.is_valid():
            # Capturar os dados do formulário
            nome_relatorio = form.cleaned_data['nome_relatorio']
            data_inicio = form.cleaned_data['data_inicio']
            data_fim = form.cleaned_data['data_fim']
            tipo_relatorio = form.cleaned_data['tipo_relatorio']

            # Capturar os dados das vendas
            produto = form.cleaned_data['produto']
            preco = form.cleaned_data['preco']
            quantidade = form.cleaned_data['quantidade']
            total = preco * quantidade

            # Gerar um gráfico de exemplo
            fig, ax = plt.subplots()
            ax.bar([produto], [total], color='skyblue')
            ax.set_title("Total de Vendas por Produto")
            ax.set_ylabel("Total (R$)")
            ax.set_xlabel("Produto")

            # Salvar o gráfico em base64
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            image_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()

            # Passar os dados para o template
            return render(request, 'relatorios/formulario_relatorio.html', {
                'form': form,
                'nome_relatorio': nome_relatorio,
                'data_inicio': data_inicio,
                'data_fim': data_fim,
                'tipo_relatorio': tipo_relatorio,
                'vendas': [{'produto': produto, 'preco': preco, 'quantidade': quantidade, 'total': total}],
                'grafico': image_base64
            })
    else:
        form = RelatorioForm()

    return render(request, 'relatorios/formulario_relatorio.html', {'form': form})
