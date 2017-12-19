# Teste técnico junto à DSBR

O propósito deste teste é uma avaliação das minhas capacidades técnicas como desenvolvedor para trabalhar junto à DSBR.

O teste consiste na leitura de dados públicos advindos de um arquivo CSV com tamanho consideráve: 1.1Gb e mais de 3,3 
milhões de registros.

As principais tecnologias utilizadas para a solução do teste ténico foram: Python, Django, PostgreSQL, Celery e Redis.

Python e Django como o coração de todo o desenvolvimento.

PostgreSQL por ser um Sistema de Gerenciamento de Banco de Dados muito robusto e versátil, escolha feita devido à 
quantidade de registros envolvidos.

Celery e Redis para que a geração assíncrona do Banco de Dados, haja vista que, em média, a duração desse processo
fica na casa dos 18 a 20 minutos. 

O Redis também foi usado como backend do Cache para as sessões do Django, melhorando a performance do sistema.

Outras bibliotecas foram utilizadas, mas todas referentes ao Python e o próprio Django, no intuito de dar 
mais flexibilidade ao código. 