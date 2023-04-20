# dbc2csv [![license](https://img.shields.io/github/license/mashape/apistatus.svg?maxAge=2592000)](https://github.com/greatjapa/dbc2csv/blob/master/LICENSE)

`dbc2csv` é um utilitário que converte arquivos no formato `dbc` para `csv`. A ideia principal do `dbc2csv` é facilitar pesquisas relacionadas a dados públicos de saúde através da geração de dados em formatos fáceis de serem processados, como `csv`.

*NOTA:* O arquivo `dbc` em questão é um formato proprietário do Departamento de Informatica do SUS (DATASUS) e não possui relação com o formato de mesmo nome da Microsoft FoxPro ou CANdb.

## Como instalar?

Para usar o `dbc2csv` é preciso ter os seguintes programas instalados na sua máquina:
- git
- make
- python


Logo em seguinda execute os passos abaixo:

```bash
$ git clone https://github.com/greatjapa/dbc2csv.git
$ cd dbc2csv
$ make all
```

Ao final deste processo teremos uma imagem Docker com todos os programas utlizados na manipulação de arquivos `dbc`.

## Como converter?

ainda dentro da pasta dbc2csv use o comando a seguir substituindo diretorio pelo caminho absoluto ou relativo ao diretorio atual
```bash
python main.py <diretorio>
```
## Agradecimentos

- A [Prof. Rita Berardi](mailto:ritaberardi@utfpr.edu.br) pela atenção dedicada no desenvolvimento desta ferramenta.
- A toda comunidade que se preocupa com o desenvolvimento e transparência dos dados públicos.

## Referências

* ["Microdatasus: pacote para download e pré-processamento de microdados do Departamento de Informática do SUS (DATASUS)"](https://doi.org/10.1590/0102-311x00032419), `urn:doi:10.1590/0102-311x00032419`.

* [Documentação oficial do SUS](http://cnes.datasus.gov.br/pages/downloads/documentacao.jsp), `http://CNES.DataSUS.gov.br`.

# TD:LR

este projeto é um fork preguiçoso e com recurso de diretorios recursivos que funciona aparentemente em linux apenas e mão usa o docker, sendo um fork do projeto https://github.com/greatjapa/dbc2csv


  

