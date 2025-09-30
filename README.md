# 🌐 Projeto IoT com ESP32-C3 – Automação e Dashboard

## 📌 Visão Geral
Este projeto demonstra um protótipo de **automação IoT** utilizando a placa **ESP32**, sensores **DHT11** (temperatura e umidade) e **LDR** (luminosidade).  
O sistema aplica **regras de automação locais** (direto no dispositivo) e **regras em nuvem** (obtidas de uma API), com suporte a **fail-safe**.  
As leituras são armazenadas em **CSV** e visualizadas em um **mini-dashboard Python**.  

---

## 🛠️ Componentes
- ESP32-C3  
- Sensor **DHT11** (temperatura e umidade)  
- Sensor **LDR** (luminosidade)  
- LED/Relé para atuação  
- Conexão Wi-Fi  
- API REST (para thresholds dinâmicos e envio de dados)  
- Dashboard em Python (matplotlib/pandas)  

---

## ⚙️ Fluxo do Sistema
1. **ESP32-C3** lê os sensores (DHT11 + LDR).  
2. **Decisão local**: se ultrapassar os thresholds definidos no código, aciona LED/relé.  
3. **Integração com API**:  
   - Envia leituras (POST) para armazenamento.  
   - Busca thresholds atualizados (GET).  
   - Caso a API falhe, aplica **valores padrão locais** (fail-safe).  
4. Os dados recebidos pela API são armazenados em um arquivo **CSV**.  
5. O **dashboard em Python** lê o CSV e exibe gráficos de temperatura, umidade e luminosidade.  

---

## 📊 Dashboard Python
O dashboard lê os dados do CSV e gera visualizações:  

- Histórico de **temperatura**  
- Histórico de **umidade**  
- Histórico de **luminosidade**  
- Comparativo entre sensores  

