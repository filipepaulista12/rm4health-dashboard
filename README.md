# RM4Health Dashboard 🏥

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![REDCap API](https://img.shields.io/badge/REDCap-API-red.svg)](https://redcap.vanderbilt.edu/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📊 Plataforma de Análise de Dados REDCap

Dashboard web profissional para análise e visualização de dados do projeto RM4Health através da API REDCap. Sistema desenvolvido para monitoramento remoto de saúde com análises avançadas e insights clínicos.

### 🚀 Funcionalidades

#### 📈 **6 Módulos de Análise Avançada**
- **Dashboard Principal** - Visão geral dos dados e estatísticas
- **Análise Longitudinal** - Tracking de evolução temporal dos participantes  
- **Utilização de Cuidados de Saúde** - Padrões de uso dos serviços de saúde
- **Análise de Sono** - Monitoramento e insights dos padrões de sono
- **Adesão Medicamentosa** - Tracking de compliance com medicações
- **Comparação por Residência** - Análises geográficas e demográficas

#### 🔧 **Características Técnicas**
- ✅ **596 registros** processados de **23 participantes** ativos
- ✅ Integração segura com **REDCap API**
- ✅ Interface web responsiva e profissional
- ✅ Processamento de dados em tempo real
- ✅ Visualizações interativas e insights automatizados
- ✅ Sistema de cache para performance otimizada

### 🏗️ Arquitetura

```
RM4Health Dashboard/
├── app.py                 # Aplicação Flask principal (27KB)
├── data_processor.py      # Motor de análise de dados (213KB)
├── redcap_client.py      # Cliente API REDCap
├── config.py             # Configurações do sistema
├── requirements.txt      # Dependências Python
├── templates/            # Templates HTML (17 arquivos)
│   ├── dashboard.html    # Dashboard principal
│   ├── longitudinal.html # Análises temporais
│   ├── healthcare_*.html # Análises clínicas
│   └── ...              # Outros módulos
└── .gitignore           # Configuração Git
```

### 🛠️ Stack Tecnológico

- **Backend**: Python Flask
- **Dados**: REDCap API, Pandas, NumPy
- **Frontend**: HTML5, CSS3, JavaScript
- **Visualização**: Charts.js, Bootstrap
- **Deploy**: Git, GitHub

### ⚡ Quick Start

```bash
# 1. Clone o repositório
git clone https://github.com/filipepaulista12/rm4health-dashboard.git
cd rm4health-dashboard

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure as variáveis de ambiente
# Edite config.py com suas credenciais REDCap

# 4. Execute o dashboard
python app.py

# 5. Acesse http://localhost:5000
```

### 🔑 Configuração

1. **REDCap API Token**: Configure sua chave API no `config.py`
2. **URL REDCap**: Defina a URL do seu servidor REDCap
3. **Variáveis de Ambiente**: Configure as credenciais de forma segura

### 📊 Análises Disponíveis

#### **Dashboard Principal**
- Estatísticas gerais dos participantes
- Métricas de qualidade dos dados
- Alertas e notificações importantes

#### **Análise Longitudinal**
- Evolução temporal dos indicadores
- Trends de saúde por participante
- Comparações entre períodos

#### **Utilização de Cuidados**
- Padrões de uso de serviços de saúde
- Correlações com indicadores clínicos
- Análises de custo-efetividade

#### **Análise de Sono**
- Qualidade e padrões de sono
- Correlações com outros biomarcadores
- Insights de wellness

#### **Adesão Medicamentosa**
- Compliance com tratamentos
- Identificação de padrões de não-adesão
- Alertas de risco

#### **Comparação Residencial**
- Análises geográficas
- Comparações demográficas
- Insights regionais

### 📈 Métricas do Projeto

- **📊 Dados**: 596 registros processados
- **👥 Participantes**: 23 ativos
- **📁 Código**: 12,307+ linhas
- **🔧 Módulos**: 6 análises especializadas
- **📱 Templates**: 17 interfaces web

### 🤝 Contribuindo

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### 📝 License

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para detalhes.

### 🏥 Sobre o RM4Health

O RM4Health é um projeto de investigação em saúde digital focado no monitoramento remoto de pacientes. Este dashboard representa a interface de análise central para dados coletados através da plataforma REDCap.

### 📞 Contacto

**Projeto**: RM4Health Dashboard  
**Repositório**: [github.com/filipepaulista12/rm4health-dashboard](https://github.com/filipepaulista12/rm4health-dashboard)  
**Tecnologia**: Flask + REDCap API  

---

*Desenvolvido com ❤️ para a comunidade de saúde digital*
