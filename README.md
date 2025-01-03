
# 🌾 Texas Farm 🌾

Bem-vindo ao **Texas Farm**, um jogo de simulação agrícola onde você administra sua própria fazenda! Plante sementes, colha seus produtos, compre novos insumos e ganhe dinheiro para expandir sua fazenda. Tudo isso enquanto avança pelos dias e enfrenta desafios para se tornar o maior fazendeiro do Texas!

## 🎮 Como Jogar

1. **Início**: Ao iniciar o jogo, você escolherá o nome da sua fazenda.
2. **Plantio**: Compre sementes e plante na sua fazenda. Cada tipo de semente tem um tempo diferente para crescer.
3. **Colheita**: Quando suas plantações estiverem prontas, é hora de colher! Envie para o silo ou venda para obter lucro.
4. **Loja**: Compre novas sementes para diversificar suas plantações.
5. **Mercado**: Venda seus grãos para ganhar dinheiro e investir em novos recursos para sua fazenda.
6. **Silo**: Gerencie seus grãos armazenados no silo.
7. **Avance os Dias**: A cada dia, as plantações crescem, os preços mudam e novos desafios surgem!

## 🛠 Tecnologias Usadas

- **Python**: A base do jogo foi construída utilizando Python.
- **JSON**: O progresso do jogo é salvo em um arquivo JSON, para que você possa continuar jogando de onde parou.

## 📂 Estrutura do Projeto

```plaintext
.
├── texas.py  # Arquivo principal do jogo
└── APPDATA/ROAMING/texasfarm.json  # Salva o progresso do jogo
```

## 💾 Salvando o Progresso

O jogo permite salvar seu progresso automaticamente. Ao iniciar ou sair, suas informações são armazenadas em um arquivo de progresso que pode ser carregado novamente quando você voltar para o jogo. Isso inclui:

- Nome da fazenda
- Dinheiro
- Sementes e quantidades
- Plantações e dias restantes
- Preços de mercado
- Itens no silo

## 🎨 Melhorias Futuras

- Implementar novas funcionalidades de cultivo e agricultura.
- Melhorar a interface com mais gráficos e interatividade.
- Adicionar novos tipos de sementes e plantas.
- Expandir o sistema de economia do jogo.

## 🔧 Como Rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/FabricioFacco/TexasFarm.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd TexasFarm
   ```

3. Execute o jogo:
   ```bash
   python texas.py
   ```

## 🎉 Contribuindo

Se você deseja contribuir para o projeto, fique à vontade para enviar Pull Requests com melhorias ou correções de bugs.

---

Obrigado por jogar **Texas Farm**! Esperamos que você aproveite a experiência de se tornar o maior fazendeiro do Texas!
