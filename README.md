# Scraping B2W Marketplace

Esta aplicação foi desenvolvida com o objetivo de solucionar um problema de controle de estoque, uma vez que a ferramenta original da B2W está desatualizada e apresenta diversos problemas. Para utilizar esta ferramenta, será necessário ter seu login e senha, uma lista dos SKUs cadastrados na B2W e uma conexão estável com a internet. Estou trabalhando para automatizar a coleta dos SKUs de maneira automática, porém, até o momento atual, essa funcionalidade ainda não está disponível, então a obtenção dos SKUs continua sendo um processo manual.

## Atenção

Esta ferramenta é completamente segura e está livre de códigos maliciosos. O roubo de dados digitais é considerado crime no Brasil de acordo com o Código Penal Brasileiro. É crucial respeitar a privacidade e a segurança dos dados de terceiros, evitando acessar, alterar ou copiar informações sem autorização legal, pois tais ações são passíveis de punição conforme a legislação brasileira. Portanto, reforçamos que não estamos envolvidos em atividades de roubo de dados ou informações.

## Instalação

<details>
  <summary>Clique para expandir!</summary>

  Para executar a aplicação inicie realizando o clone deste repositório com o comando abaixo.

    git clone git@github.com:guilhermepallma/delivery-app.git

  Navegue até a raíz do projeto.

    cd delivery-app/
    
  Suba o contêiner do banco de dados no Docker.
    
    docker-compose up -d
    
  Instale as dependência básicas para rodas os scripts.
  
    npm install
    
  Inicie a aplicação e popule o banco de dados.
  
    npm run dev:prestart
    
</details>
