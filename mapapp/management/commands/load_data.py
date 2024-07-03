import pandas as pd
from django.core.management.base import BaseCommand
from mapapp.models import Estacao  # Certifique-se de que a importação está correta

class Command(BaseCommand):
    help = 'Carrega dados do Excel para o banco de dados'

    def handle(self, *args, **kwargs):
        # Carregar o arquivo Excel
        file_path = 'mapapp\markers.xlsx'  # Atualize com o caminho correto do arquivo
        df = pd.read_excel(file_path)

        # Iterar sobre as linhas do DataFrame e criar objetos Estacao
        for index, row in df.iterrows():
            Estacao.objects.create(
                nome_entidade=row['NomeEntidade'],
                num_servico=row['NumServico'],
                num_estacao=row['NumEstacao'],
                latitude=row['Latitude'],
                longitude=row['Longitude'],
                tecnologia=row['Tecnologia'],
                frequencia=row['Frequencia'],
                azimute=row['Azimute'],
                altura_antena=row['AlturaAntena']
            )
        self.stdout.write(self.style.SUCCESS('Dados carregados com sucesso!'))
