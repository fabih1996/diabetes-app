import warnings
import streamlit as st
# Disattiva tutti i warning
warnings.filterwarnings("ignore")


from joblib import load
model=load("ultimate_model.joblib")

def insert_data(): 
	genere = st.selectbox('Genere: ',('Maschio', 'Femmina')) #SESSO
	if genere=='Maschio':
		sesso=1
	else:
		sesso=0

	age = st.slider('Quanti anni hai?', 0, 130, 25) #ETA'
    
	press = st.selectbox('Soffri di ipertensione?',('Sì', 'No')) #PRESSIONE
	if press=='Sì':
		ipertensione=1
	else:
		ipertensione=0

	cuore = st.selectbox('Hai problemi di cuore?',('Sì', 'No')) #CUORE
	if cuore=='Sì':
		problemi_di_cuore=1
	else:
		problemi_di_cuore=0

	peso = st.slider('Quanti pesi [kg]?', 0, 130, 50) #PESO

	altezza = st.slider('Quanti sei alto [cm]?', 0, 220, 165) #ALTEZZA

	altezza=altezza/100
	altezza_quadra=altezza**2
	bmi=peso/altezza_quadra

	glicata = st.slider('Inserisci glicata [%]: ', 0, 15, 5) #GLICATA

	glicemia = st.slider('Inserisci glicemia: ', 0, 500, 90) #GLICEMIA

	return [[sesso,age,ipertensione,problemi_di_cuore,bmi,glicata,glicemia]]

def calcola_prob(dati):
	if st.button('Calcola probabilità'):
		st.write(f"Hai una probabilità del {round(model.predict_proba(dati)[0][1],2)*100}% di avere il diabete")

	else:
	    st.write('Perfavore, inserisci i tuoi dati.')
		
def test():
	dati=insert_data()
	calcola_prob(dati)
	
st.write('Calcola la probabilità di avere il diabete con un algoritmo di machine learning sviluppato da FC')
test()
