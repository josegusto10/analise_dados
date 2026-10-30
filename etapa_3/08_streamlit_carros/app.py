import pandas as pd
import streamlit as st

st.set_page_config(page_title="Vendas de carros", page_icon="🚗", layout="wide")

# Preços didáticos, só para a aula. Não são cotações e o pagamento não é real.
CATALOGO = {
    "Compacto A1": {"categoria": "Hatch", "preco": 42000.00},
    "Sedan B2": {"categoria": "Sedan", "preco": 68000.00},
    "SUV C3": {"categoria": "SUV", "preco": 95000.00},
    "Picape D4": {"categoria": "Picape", "preco": 120000.00},
    "Eletrico E5": {"categoria": "Elétrico", "preco": 150000.00},
}

if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

st.title("Vendas de carros — ponto de venda didático")
st.caption(
    "O carrinho fica em st.session_state. O Streamlit guarda essa lista enquanto "
    "esta sessão do navegador estiver aberta e o script for reexecutado. "
    "Isso não grava a venda em disco e não conserva o carrinho para sempre."
)
st.markdown("---")

tabela_catalogo = pd.DataFrame(
    [
        {"Modelo": nome, "Categoria": dados["categoria"], "Preço (R$)": dados["preco"]}
        for nome, dados in CATALOGO.items()
    ]
)

col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Catálogo")
    st.dataframe(
        tabela_catalogo,
        hide_index=True,
        use_container_width=True,
        column_config={
            "Preço (R$)": st.column_config.NumberColumn("Preço (R$)", format="R$ %.2f")
        },
    )
    st.caption("Os preços acima são de exemplo. Não representam valores de mercado.")

    st.subheader("Adicionar ao carrinho")
    with st.form("form_carro", clear_on_submit=False):
        modelo = st.selectbox("Escolha o modelo", list(CATALOGO.keys()))
        preco_unit = CATALOGO[modelo]["preco"]
        st.caption(
            f"Preço deste modelo no envio do formulário: **R$ {preco_unit:.2f}**. "
            "O formulário só reexecuta o script ao clicar em adicionar, então o "
            "preço exibido acompanha o modelo escolhido nesse momento."
        )
        quantidade = st.number_input("Quantidade", min_value=1, value=1, step=1)
        adicionar = st.form_submit_button("Adicionar ao carrinho", use_container_width=True)

        if adicionar:
            subtotal = preco_unit * quantidade
            st.session_state.carrinho.append(
                {
                    "Modelo": modelo,
                    "Categoria": CATALOGO[modelo]["categoria"],
                    "Preço unit. (R$)": preco_unit,
                    "Qtd": int(quantidade),
                    "Subtotal (R$)": subtotal,
                }
            )
            st.success(f"**{modelo}** adicionado. Preço usado: R$ {preco_unit:.2f}.")

    st.subheader("Carrinho")
    if st.session_state.carrinho:
        df_carrinho = pd.DataFrame(st.session_state.carrinho)
        st.dataframe(
            df_carrinho,
            hide_index=True,
            use_container_width=True,
            column_config={
                "Preço unit. (R$)": st.column_config.NumberColumn("Preço unit.", format="R$ %.2f"),
                "Subtotal (R$)": st.column_config.NumberColumn("Subtotal", format="R$ %.2f"),
            },
        )
        if st.button("Limpar carrinho", use_container_width=True):
            st.session_state.carrinho = []
            st.rerun()
    else:
        st.info("O carrinho está vazio. Adicione um modelo acima.")

with col2:
    st.subheader("Pagamento simulado")
    total = sum(item["Subtotal (R$)"] for item in st.session_state.carrinho)
    st.metric("TOTAL DA COMPRA", f"R$ {total:.2f}")
    st.markdown("---")

    valor_recebido = st.number_input(
        "Dinheiro entregue pelo cliente (R$)",
        min_value=0.0,
        value=0.0,
        step=1000.0,
        format="%.2f",
    )

    if total == 0:
        st.warning("Adicione um carro ao carrinho antes de simular o pagamento.")
    else:
        troco = valor_recebido - total
        if valor_recebido == 0:
            st.info("Aguardando o valor entregue pelo cliente.")
        elif valor_recebido < total:
            falta = total - valor_recebido
            st.error(f"**Valor insuficiente.** Faltam **R$ {falta:.2f}**.")
        else:
            st.success("**Pagamento simulado concluído.** Nenhum dinheiro foi movimentado.")
            st.metric("TROCO A DEVOLVER", f"R$ {troco:.2f}")
            with st.expander("Ver resumo da venda"):
                st.write(f"**Itens:** {len(st.session_state.carrinho)}")
                st.write(f"**Total:** R$ {total:.2f}")
                st.write(f"**Valor informado:** R$ {valor_recebido:.2f}")
                st.write(f"**Troco:** R$ {troco:.2f}")
            if st.button("Finalizar e atender outro cliente", type="primary", use_container_width=True):
                st.session_state.carrinho = []
                st.rerun()
