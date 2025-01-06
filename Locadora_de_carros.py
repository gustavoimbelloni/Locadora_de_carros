import streamlit as st

# Lista de carros disponíveis para aluguel
carros = [
    ("Fiat Mobi", 50),
    ("Renault Kwid", 60),
    ("Citroen C3", 70),
    ("Fiat Argo", 80),
    ("Hyundai HB20", 90),
    ("Renault Stepway", 100),
    ("Chevrolet Onix", 110),
    ("Volkswagen Polo", 120),
]

# Lista de carros alugados
alugados = []

# Mostrar a lista de carros
def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        st.write(f"[{i}] {car[0]} -- R$ {car[1]} /dia.")

# Título do aplicativo
st.title("Locadora de Carros")

# Menu principal
menu = st.sidebar.selectbox(
    "Escolha uma opção",
    ["Mostrar Portfólio", "Alugar um Carro", "Devolver um Carro"]
)

# Mostrar portfólio de carros
if menu == "Mostrar Portfólio":
    st.header("Portfólio de Carros")
    if carros:
        mostrar_lista_de_carros(carros)
    else:
        st.write("Todos os carros estão alugados no momento.")

# Alugar um carro
elif menu == "Alugar um Carro":
    st.header("Alugar um Carro")
    if carros:
        mostrar_lista_de_carros(carros)
        cod_car = st.number_input("Escolha o código do carro:", min_value=0, max_value=len(carros) - 1, step=1)
        dias = st.number_input("Por quantos dias deseja alugar?", min_value=1, step=1)

        if st.button("Confirmar Aluguel"):
            carro_escolhido = carros.pop(cod_car)
            alugados.append(carro_escolhido)
            st.success(f"Você alugou {carro_escolhido[0]} por {dias} dias. Total: R$ {carro_escolhido[1] * dias}")
    else:
        st.write("Não há carros disponíveis para aluguel no momento.")

# Devolver um carro
elif menu == "Devolver um Carro":
    st.header("Devolver um Carro")
    if alugados:
        mostrar_lista_de_carros(alugados)
        cod = st.number_input("Escolha o código do carro a ser devolvido:", min_value=0, max_value=len(alugados) - 1, step=1)

        if st.button("Confirmar Devolução"):
            carro_devolvido = alugados.pop(cod)
            carros.append(carro_devolvido)
            st.success(f"Você devolveu o carro {carro_devolvido[0]}. Obrigado!")
    else:
        st.write("Não há carros para devolver no momento.")

# Nota final
st.sidebar.write("Obrigado por usar a Locadora de Carros!")
