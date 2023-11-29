# Scraping Marketplace B2W

Esta ferramenta foi desenvolvida com o objetivo de solucionar um problema de controle de estoque, uma vez que a ferramenta original da B2W está desatualizada e apresenta diversos problemas. Para utilizar esta ferramenta, será necessário ter seu login e senha, uma lista dos SKUs cadastrados na B2W e uma conexão estável com a internet. Estou trabalhando para automatizar a coleta dos SKUs de maneira automática, porém, até o momento atual, essa funcionalidade ainda não está disponível, então a obtenção dos SKUs continua sendo um processo manual.

# Atenção

Esta ferramenta é completamente segura e está livre de códigos maliciosos. O roubo de dados digitais é considerado crime no Brasil de acordo com o Código Penal Brasileiro. É crucial respeitar a privacidade e a segurança dos dados de terceiros, evitando acessar, alterar ou copiar informações sem autorização legal, pois tais ações são passíveis de punição conforme a legislação brasileira. Portanto, reforçamos que não estamos envolvidos em atividades de roubo de dados ou informações.

## Instalação

<details>
  <summary>Clique para expandir!</summary>
  <br>
  Para executar a aplicação, comece clonando este repositório ao executar o comando abaixo:

    git clone git@github.com:guilhermepallma/scraping_marketplace_b2w.git

  Entre no diretório raiz do projeto:

    cd scraping_marketplace_b2w
  
  Crie um ambiente virtual para a execução do programa:

    python3 -m venv .venv
    
  Ative o ambiente virtual:
  
    source .venv/bin/activate

  Instale as dependências no ambiente virtual:

    python3 -m pip install -r requirements.txt

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente. Quando precisar desativar o ambiente virtual, execute o comando `deactivate`. Lembre-se de ativar novamente quando voltar a trabalhar no projeto. O arquivo `requirements.txt` instalará todas as dependências que serão utilizadas no projeto.
    
</details>

## Execução

<details>
  <summary>Clique para expandir!</summary>
  <br>
  
  Antes de ativar a aplicação, é fundamental preencher um parâmetro básico, que consiste no login e na senha da B2W. Na pasta raíz do projeto, crie um arquivo com o nome `.env` e insira o seguinte conteúdo dentro dele:

    EMAIL='seu email'
    PASSWORD='sua senha'
    
  Para iniciar o scraping bastar rodar o seguinte comando:
  
    python3 main.py

  Conforme mencionado anteriormente, a coleta dos SKUs da B2W ainda não foi automatizada. Portanto, é necessário preencher o arquivo 'skus.py' manualmente com todos os SKUs que deseja monitorar, seguindo a seguinte formatação:

    all_skus = [ 'BR78901154', 'BR78901153', 'BR78901152', ...]

  Ao final desse processo de verificação, será gerada uma planilha no formato `.xlsx`, na qual estará disponível colunas com os títulos `MODELO`, `ESTOQUE 01` e `ESTOQUE 02`, referindo-se às quantidades. Esta ferramenta verifica apenas dois estoques, porém é possível adicionar a verificação de mais estoques facilmente ao editar o código no arquivo `main.py`.
<br>

Se por acaso ocorrer algum problema na leitura do SKU, basta acessar o arquivo `message.log`, onde será indicado qual SKU apresentou problemas ou se não existe.

</details>
<div>

  Desenvolvido por [Guilherme Palma](www.linkedin.com/in/guilhermepallma) © 2023.
</div>
