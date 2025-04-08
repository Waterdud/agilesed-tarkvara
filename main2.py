tasks = []

def lisa_ülesanne(task):
    tasks.append(task)

def kustuta_ülesanne(task_to_delete):
    if task_to_delete in tasks:
        tasks.remove(task_to_delete)
        print(f"Ülesanne '{task_to_delete}' on kustutatud.")
    else:
        print(f"Ülesannet '{task_to_delete}' ei leitud.")

def vaata_ülesandeid():
    if tasks:
        print("Ülesanded:")
        for task in tasks:
            print(f"- {task}")
    else:
        print("Ülesandeid ei ole.")

def main():
    while True:
        print('1 - Lisa ülesanne \n2 - Kustuta ülesanne \n3 - Vaata ülesandeid \n4 - Välju')
        userInput = input("Mida sa tahad teha? ")
        
        if userInput == '1':
            task = input("Sisesta ülesanne: ")
            lisa_ülesanne(task)
        elif userInput == '2':
            task_to_delete = input("Sisesta ülesanne, mida tahad kustutada: ")
            kustuta_ülesanne(task_to_delete)
        elif userInput == '3':
            vaata_ülesandeid()
        elif userInput == '4':
            print("Väljumine...")
            break
        else:
            print("Sa sisestasid midagi vale!")

main()
import streamlist as streamlist

if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("Todo List")