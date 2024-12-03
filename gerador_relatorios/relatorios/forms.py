# relatorios/forms.py

from django import forms

class RelatorioForm(forms.Form):
    nome_relatorio = forms.CharField(max_length=100, label="Nome do Relatório")
    data_inicio = forms.DateField(widget=forms.SelectDateWidget(years=range(2020, 2031)), label="Data de Início")
    data_fim = forms.DateField(widget=forms.SelectDateWidget(years=range(2020, 2031)), label="Data de Fim")
    tipo_relatorio = forms.ChoiceField(
        choices=[('vendas', 'Vendas'), ('clientes', 'Clientes'), ('estoque', 'Estoque')], 
        label="Tipo de Relatório"
    )

    # Campos para vendas
    produto = forms.CharField(max_length=100, label="Nome do Produto")
    preco = forms.FloatField(label="Preço")
    quantidade = forms.IntegerField(label="Quantidade")
