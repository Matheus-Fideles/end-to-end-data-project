# Data Engineering 360º: Fundamentals for a Modern and Resilient Data Infrastructure

>:memo: **Nota:** Este caso apresentará uma abordagem completa para a conceção e implementação de uma infraestrutura de dados robusta e resiliente. O foco será a construção de pipelines escaláveis, governação eficiente e arquitecturas que suportem alta disponibilidade e tolerância a falhas. Além disso, serão exploradas as melhores práticas para a otimização do armazenamento, o processamento distribuído e a integração de diferentes fontes de dados, garantindo a fiabilidade e o desempenho para a análise e a tomada de decisões.

### Sumário

- [Pre-requisites](#pre-requisites)
- [Architecture Decision Record (ADR)](#architecture-decision-record-adr)
    - [ADR - 001](#adr---001)
    - [ADR - 002](#adr---002)
    - [ADR - 003](#adr---003)
    - [ADR - 004](#adr---004)
- [System Design](#system-design)


## Pre-requisites

* <strong>Java</strong>. 
[How to install Java?](https://www.oracle.com/java/technologies/downloads/) 
<br>
* <strong>Python</strong>.
[How to install Python?](https://realpython.com/installing-python/) 
<br>
* <strong>PySpark</strong>.
[How to install PySpark?](https://spark.apache.org/docs/latest/api/python/getting_started/install.html) 
<br>
* <strong>Rancher Desktop</strong>.
[How to install Rancher Desktop?](https://docs.rancherdesktop.io/getting-started/installation/) 
<br>
* <strong>Terraform</strong>.
[How to install Terraform?](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli) 
<br>
* <strong>Helm</strong>.
[How to install Helm?](https://helm.sh/docs/intro/install/) 
<br>
* <strong>AWS CLI</strong>.
[How to install AWS CLI?](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) 
<br>
* <strong>Git</strong>.
[How to install Git?](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) 
<br>

## Architecture Decision Record (ADR)

### ADR - 001

**Título:** Escolha da Tecnologia PySpark.


| **Seção**               | **Descrição**                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Contexto**             | O projeto exige o processamento de grandes volumes de dados em um ambiente de nuvem (AWS), com foco em escalabilidade e integração com outros serviços da AWS, como S3 e Redshift.     |
| **Decisão**              | Utilizar PySpark no Amazon EMR para processamento distribuído de dados em larga escala.                                                                                                 |
| **Justificativa**        | - **Escalabilidade:** Amazon EMR permite escalar automaticamente os clusters conforme a demanda. <br> - **Integração com AWS:** Integração fácil com serviços como S3 e Redshift. <br> - **Suporte a Big Data:** PySpark é otimizado para grandes volumes de dados e operações complexas. <br> - **Gerenciamento Simplificado:** Solução totalmente gerenciada pelo EMR. <br> - **Custo-benefício:** Custos ajustáveis com clusters sob demanda. |
| **Alternativas Consideradas** | - **AWS Glue:** Para processamento sem servidor, mas com menos flexibilidade que PySpark. <br> - **Databricks:** Mais robusto, mas com custos mais altos em comparação ao EMR.         |
| **Consequências**        | - **Escalabilidade sob demanda:** Otimização de recursos e custos. <br> - **Complexidade de configuração:** Requer esforço inicial para configuração e otimização de clusters. <br> - **Especialização:** A equipe precisa de conhecimento em Spark e EMR. <br> - **Integração com AWS:** Fácil integração com o ecossistema AWS.                                  |
| **Referências**          | - [Documentação do Amazon EMR](https://aws.amazon.com/emr/) <br> - [Documentação do PySpark](https://spark.apache.org/docs/latest/api/python/)                                              |

<br>

### ADR - 002

**Título:** Escolha da Tecnologia para Microserviços


| **Seção**               | **Descrição**                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Contexto**             | O projeto exige a criação de microserviços escaláveis e eficientes em termos de desempenho. As tecnologias devem ser leves, de fácil integração e suportar um alto volume de requisições. |
| **Decisão**              | Utilizar **Quarkus** com **Java** para desenvolvimento de microserviços devido ao seu desempenho otimizado para ambientes de contêineres e ao seu foco em microserviços nativos para a nuvem. |
| **Justificativa**        | - **Desempenho e Tempo de Inicialização:** Quarkus foi projetado para otimizar tempo de inicialização e uso de memória, tornando-o ideal para ambientes em containers como Docker e Kubernetes. <br> - **Integração com GraalVM:** Quarkus pode ser compilado nativamente com GraalVM, reduzindo significativamente o tempo de execução e o uso de memória. <br> - **Desenvolvimento para Nuvem:** Focado em microserviços e ambientes nativos da nuvem, Quarkus possui integração fácil com ferramentas e plataformas como Kubernetes, OpenShift, etc. <br> - **Facilidade de Uso:** Sua configuração e uso são simplificados para desenvolvedores Java, com suporte à programação reativa e integração com bibliotecas Java tradicionais. |
| **Alternativas Consideradas** | - **Spring:** Amplamente utilizado e com uma vasta comunidade, oferece soluções robustas para microserviços, mas com tempo de inicialização mais lento e maior consumo de memória em comparação ao Quarkus. <br> - **Express (Node.js):** Solução rápida para microserviços em JavaScript/TypeScript, mas não tão otimizada em termos de desempenho e escalabilidade em comparação ao Quarkus, além de ser mais difícil de integrar em um ecossistema Java corporativo.  |
| **Consequências**        | - **Desempenho Melhorado:** Com o Quarkus, espera-se tempos de inicialização e uso de memória significativamente menores. <br> - **Facilidade de Configuração e Integração com Kubernetes:** Quarkus facilita a implementação de microserviços em ambientes baseados em contêineres. <br> - **Foco em Nuvem e Kubernetes:** A escolha de Quarkus alinha-se bem com arquiteturas nativas de nuvem, proporcionando escalabilidade eficiente. <br> - **Curva de Aprendizado:** A equipe precisará aprender as novas ferramentas e práticas associadas ao Quarkus, principalmente se já estiver acostumada com o Spring. |
| **Referências**          | - [Documentação do Quarkus](https://quarkus.io/) <br> - [Documentação do Spring](https://spring.io/projects/spring-boot) <br> - [Documentação do Express](https://expressjs.com/) |


<br>

### ADR - 003

**Título:** Escolha do Kubernetes


| **Seção**               | **Descrição**                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Contexto**             | O projeto exige uma solução robusta e escalável para orquestrar e gerenciar o deploy de aplicativos, incluindo microserviços, processamento distribuído de dados com **Spark**, e outros aplicativos. A necessidade de escalabilidade, flexibilidade e integração com a nuvem levou à escolha do **Kubernetes** |
| **Decisão**              | Optamos por utilizar **Kubernetes** como o sistema de gerenciamento de clusters para o deploy de qualquer aplicativo, incluindo **microserviços com Quarkus** e processamento com **Spark**. Kubernetes fornecerá mais flexibilidade, escalabilidade e integração com outros serviços, além de ser amplamente adotado. |
| **Justificativa**        | - **Escalabilidade e Flexibilidade:** Kubernetes oferece escalabilidade granular e flexível para todos os tipos de workloads, incluindo microserviços e clusters Spark, com fácil gerenciamento de contêineres. <br> - **Suporte a Multicloud:** Kubernetes é agnóstico de nuvem, permitindo sua execução em múltiplos provedores, como AWS, GCP, e Azure. Ao contrário do YARN, que é mais restrito à AWS, Kubernetes proporciona mais liberdade. <br> - **Facilidade de Integração com Outras Ferramentas:** Kubernetes integra-se facilmente com ferramentas de CI/CD, monitoramento, logging, além de facilitar o deploy de microserviços e aplicações distribuídas, oferecendo integração com Helm para automação de deploys. <br> - **Menor Sobrecarga de Gestão:** Apesar da curva de aprendizado inicial, Kubernetes oferece uma administração mais padronizada e menos dependente de infraestrutura específica da nuvem. |
| **Alternativas Consideradas** | - **Amazon ECS (Elastic Container Service):** Solução útil para orquestração de containers dentro da AWS, mas ainda assim não oferece a mesma flexibilidade, portabilidade e funcionalidades nativas que o Kubernetes proporciona para qualquer tipo de aplicação. |
| **Consequências**        | - **Escalabilidade e Flexibilidade:** Kubernetes permitirá a escalabilidade eficiente de qualquer tipo de aplicação, incluindo Spark e Quarkus, com uma gestão simples de recursos. <br> - **Portabilidade e Agnosticismo:** A escolha de Kubernetes facilita a migração entre diferentes provedores de nuvem, tornando o sistema mais flexível e menos dependente de uma infraestrutura específica da AWS. <br> - **Maior Complexidade Inicial:** Kubernetes exige um maior envolvimento inicial para configurar e gerenciar clusters, mas os benefícios a longo prazo superam esse custo. <br> |
| **Referências**          | - [Documentação do Kubernetes](https://kubernetes.io/docs/) <br> - [Documentação do Spark no Kubernetes](https://spark.apache.org/docs/latest/running-on-kubernetes.html) <br> - [Documentação do YARN (EMR)](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-yarn.html) |

<br>

### ADR - 004

**Título:** Escolha do Apache Flink para CDC (Change Data Capture)


| **Seção**               | **Descrição**                                                                                                                                                                           |
|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Contexto**             | O projeto exige uma solução para capturar e processar mudanças de dados em tempo real. O **Change Data Capture (CDC)** é essencial para garantir que as mudanças em bancos de dados sejam refletidas em tempo real em outros sistemas, como data lakes, sistemas de analytics ou caches. Considerando o cenário, foi necessário escolher uma ferramenta robusta para implementar o CDC. |
| **Decisão**              | Optamos por usar o **Apache Flink** como a solução para implementar o CDC. Flink oferece uma plataforma de processamento de fluxo em tempo real que é altamente escalável, tolerante a falhas e ideal para processar grandes volumes de dados em tempo real. |
| **Justificativa**        | - **Processamento de Dados em Tempo Real:** O Flink é projetado para processamento em tempo real, o que o torna ideal para CDC, permitindo a captura e processamento imediato das mudanças nos dados. <br> - **Escalabilidade e Tolerância a Falhas:** O Flink foi projetado para suportar grandes volumes de dados e garante a continuidade do processamento mesmo em caso de falhas, o que é essencial para ambientes de produção. <br> - **Integração com Diversas Fontes de Dados:** Flink oferece conectores para uma variedade de fontes de dados, como bancos de dados relacionais, sistemas NoSQL, e sistemas de mensageria, permitindo capturar mudanças em diversos sistemas e armazená-las de forma eficiente. <br> - **Eficiência no Processamento de Streams:** O Flink permite que o processamento de streams seja feito de forma eficiente e com latência muito baixa, o que é um requisito crítico para a captura de dados em tempo real. <br> - **Suporte à Consistência e Precisão:** Flink garante a consistência dos dados durante o processamento de streams, mesmo em cenários de falha ou recuperação, o que é fundamental para a precisão da captura das mudanças nos dados. |
| **Alternativas Consideradas** | - **Debezium (via Kafka Connect):** Debezium é uma ferramenta popular para CDC, que também se integra bem com Kafka. No entanto, ela não oferece a mesma flexibilidade e capacidade de processamento de fluxo em tempo real como o Flink. Debezium é mais focado em capturar mudanças e transmiti-las, enquanto o Flink pode processar essas mudanças em tempo real, agregando mais valor ao projeto. <br> - **Apache Kafka Streams:** Embora o Kafka Streams seja uma solução eficiente para processamento de dados em tempo real, ele não possui a flexibilidade do Flink em termos de integração com múltiplas fontes de dados e complexidade de processamento. Além disso, o Kafka Streams não oferece o mesmo nível de suporte a estados e operações mais complexas, como o Flink. |
| **Consequências**        | - **Processamento em Tempo Real:** Com o Flink, seremos capazes de capturar e processar dados em tempo real com alta precisão e baixa latência. <br> - **Escalabilidade e Resiliência:** O Flink oferece escalabilidade horizontal e resiliente, o que garante que o sistema possa lidar com grandes volumes de dados e se recupere rapidamente de falhas. <br> - **Complexidade Operacional:** O Flink pode exigir mais esforços para configurar e monitorar adequadamente, mas sua flexibilidade e capacidade de processamento de streams em tempo real compensam essa complexidade adicional. <br> - **Maior Precisão no CDC:** A implementação do CDC com Flink garantirá a precisão na captura de mudanças e o envio dessas informações para outros sistemas em tempo real, garantindo a integridade dos dados. |
| **Referências**          | - [Documentação do Apache Flink](https://flink.apache.org/documentation.html) <br> - [Documentação do Debezium](https://debezium.io/docs/) <br> - [Kafka Connect CDC](https://docs.confluent.io/platform/current/connect/index.html) |

<br>

## System Design