# Respostas para revisão — funções da API do Streamlit

Questionário: https://docs.google.com/forms/d/e/1FAIpQLScXNNws4bc1Z7URWFJcDZpIQGgISUhd2HyuWsEqmlG0cUo5Vw/viewform

Referência: https://docs.streamlit.io/develop/api-reference

Turma no formulário: 3A1, se essa for a turma confirmada na hora do envio.

Este arquivo só organiza as respostas para revisão. Salvar este Markdown não envia o Google Forms. O formulário não foi preenchido nem submetido.

1. Qual é a função principal de `st.title()`?
   - Alternativa: Exibir um título principal na página
   - `st.title` coloca o título maior no topo do conteúdo.

2. Qual função exibe texto em formato de cabeçalho de seção?
   - Alternativa: st.header()
   - `st.header` é o cabeçalho de seção. `st.caption` é um texto menor de apoio.

3. Qual função permite exibir texto com formatação Markdown?
   - Alternativa: st.markdown()
   - `st.markdown` interpreta negrito, listas e outros trechos em Markdown.

4. Qual função apresenta um botão clicável?
   - Alternativa: st.button()
   - `st.button` devolve verdadeiro no clique. As outras opções são seleção, não um botão comum.

5. Qual função permite ao usuário selecionar apenas uma opção de uma lista suspensa?
   - Alternativa: st.selectbox()
   - A lista suspensa de uma opção é `st.selectbox`. Várias opções ficam em `st.multiselect`.

6. Qual função permite selecionar várias opções de uma lista?
   - Alternativa: st.multiselect()
   - `st.multiselect` devolve a lista das opções marcadas.

7. Qual função cria opções de seleção com botões de rádio?
   - Alternativa: st.radio()
   - `st.radio` mostra as alternativas em botões de rádio e aceita uma escolha.

8. Qual função cria uma caixa de seleção marcada ou desmarcada?
   - Alternativa: st.checkbox()
   - `st.checkbox` guarda verdadeiro ou falso.

9. Qual função recebe texto digitado em uma única linha?
   - Alternativa: st.text_input()
   - Uma linha usa `st.text_input`. Várias linhas usam `st.text_area`.

10. Qual função recebe texto em várias linhas?
    - Alternativa: st.text_area()
    - `st.text_area` abre um campo alto para texto longo.

11. Qual função recebe um valor numérico do usuário?
    - Alternativa: st.number_input()
    - `st.number_input` limita a entrada a número, com mínimo, máximo e passo.

12. Qual função cria um controle deslizante para selecionar um valor ou intervalo?
    - Alternativa: st.slider()
    - `st.slider` escolhe um valor ou um intervalo arrastando o controle.

13. Qual função permite escolher uma data?
    - Alternativa: st.date_input()
    - A data fica em `st.date_input`. Horário é outra função.

14. Qual função permite escolher um horário?
    - Alternativa: st.time_input()
    - `st.time_input` recebe hora e minuto.

15. Qual função permite enviar um arquivo para o aplicativo?
    - Alternativa: st.file_uploader()
    - O envio de arquivo do usuário para o app é `st.file_uploader`.

16. Qual função permite ao usuário baixar um arquivo?
    - Alternativa: st.download_button()
    - `st.download_button` oferece um arquivo gerado pelo app para download.

17. Qual função exibe uma imagem?
    - Alternativa: st.image()
    - `st.image` mostra uma imagem na página.

18. Qual função exibe um dataframe de forma interativa?
    - Alternativa: st.dataframe()
    - `st.dataframe` permite rolar e ordenar a tabela. `st.table` é estática.

19. Qual função exibe uma tabela estática simples?
    - Alternativa: st.table()
    - `st.table` desenha a tabela inteira, sem a interação do dataframe.

20. Qual função mostra código com realce de sintaxe?
    - Alternativa: st.code()
    - `st.code` mostra um bloco de código com destaque de sintaxe.

21. Qual função cria um separador horizontal na página?
    - Alternativa: st.divider()
    - `st.divider` insere uma linha horizontal entre blocos.

22. Qual função apresenta um valor numérico em destaque, geralmente com comparação?
    - Alternativa: st.metric()
    - `st.metric` destaca um número e pode mostrar a variação.

23. Qual função organiza elementos em colunas?
    - Alternativa: st.columns()
    - `st.columns` divide a linha em colunas. Não existe `st.rows` nem `st.grid` nessa lista.

24. Qual função cria abas para organizar conteúdo em seções?
    - Alternativa: st.tabs()
    - `st.tabs` cria abas. A barra lateral é `st.sidebar`.

25. Qual função agrupa widgets para enviar seus valores juntos ao pressionar enviar?
    - Alternativa: st.form()
    - `st.form` junta os campos e só reexecuta o script no envio do formulário.

26. Qual botão deve ser usado dentro de um `st.form` para enviar os dados?
    - Alternativa: st.form_submit_button()
    - Dentro do formulário o botão de envio é `st.form_submit_button`, não `st.button`.

27. Qual função exibe conteúdo em uma área expansível?
    - Alternativa: st.expander()
    - `st.expander` esconde o conteúdo até a pessoa abrir.

28. Qual função cria um espaço reservado que pode ser atualizado posteriormente?
    - Alternativa: st.empty()
    - `st.empty` reserva um lugar que depois pode receber outro elemento.

29. Qual função mostra uma mensagem de sucesso?
    - Alternativa: st.success()
    - A caixa verde de sucesso é `st.success`.

30. Qual função mostra uma mensagem de erro?
    - Alternativa: st.error()
    - A caixa vermelha de erro é `st.error`.

31. Qual função mostra uma mensagem de aviso?
    - Alternativa: st.warning()
    - A caixa amarela de aviso é `st.warning`.

32. Qual função exibe uma mensagem informativa?
    - Alternativa: st.info()
    - A caixa azul de informação é `st.info`.

33. Qual função exibe um indicador de progresso?
    - Alternativa: st.progress()
    - `st.progress` mostra uma barra de progresso. `st.spinner` é a espera animada.

34. Qual função mostra uma animação de espera enquanto um bloco é executado?
    - Alternativa: st.spinner()
    - `st.spinner` gira enquanto o bloco `with` está executando.

35. Qual objeto permite guardar valores entre reexecuções da aplicação na mesma sessão?
    - Alternativa: st.session_state
    - `st.session_state` guarda valores entre reexecuções da mesma sessão. Não é um arquivo permanente.

36. Qual decorador é indicado para armazenar em cache resultados de funções que retornam dados?
    - Alternativa: @st.cache_data
    - `@st.cache_data` guarda o retorno de funções de dados, como uma tabela já calculada.

37. Qual decorador é indicado para armazenar em cache recursos como conexões ou modelos?
    - Alternativa: @st.cache_resource
    - `@st.cache_resource` é o cache de recursos compartilhados, não de tabelas serializáveis.

38. Qual função interrompe a execução do script naquele ponto?
    - Alternativa: st.stop()
    - `st.stop` para o script ali. O que vem depois não roda naquela execução.

39. Qual função força a aplicação Streamlit a executar novamente o script?
    - Alternativa: st.rerun()
    - `st.rerun` manda o Streamlit executar o script de novo imediatamente.

40. Qual função permite acessar e definir parâmetros de consulta na URL?
    - Alternativa: st.query_params
    - `st.query_params` lê e define os parâmetros depois da interrogação na URL.

Antes de enviar, confira no formulário se o enunciado de alguma questão mudou. Este texto não substitui o envio.
