import datetime

#lista para almacenar los experimentos
listaDeExperimentos = [
    ["Experimento 1", "26/11/2024", "fisica", [5, 6, 2, 7, 8, 9]],
]

#crear todas las funciones que se necesitan
#funcion para agregar experimentos
def agregar_experimento(lista):
    pass

#funcion para eliminar un experimento
def eliminar_experimento(lista):
    pass

#funcion para visualizar los experimentos
def visualizar_experimentos(lista):
    pass

#Funcion para calcular estadisticas
def calcular_estadisticas(lista):
    pass

#funcion de comparar experimentos
def comparar_experimentos(lista):
    pass

#funcion para generar un informe
def generar_informe(lista):
    pass

#funcion para mostrar el menu
def mostrar_menu():
    print("=== Menu Principal ===")
    print("1. Agregar experimento")
    print("2. Visualizar experimentos")
    print("3. Eliminar experimento")
    print("4. Calcular estadisticas")
    print("5. Comparar experimentos")
    print("6. Generar informe")
    print("7. Salir")

#funcion principal
def main():
    while True: 
        mostrar_menu()
        try:
            opcion = int(input("Ingrese una opcion: "))
            if opcion == 1:
                agregar_experimento(listaDeExperimentos)
            elif opcion == 2:
                visualizar_experimentos(listaDeExperimentos)
            elif opcion == 3:
                eliminar_experimento(listaDeExperimentos)
            elif opcion == 4:
                calcular_estadisticas(listaDeExperimentos)
            elif opcion == 5:
                comparar_experimentos(listaDeExperimentos)
            elif opcion == 6:
                generar_informe(listaDeExperimentos)
            elif opcion == 7:
                print("Gracias por usar el programa")
                break 
        except:
            print("Error: Entrada no valida. Intenta de nuevo")


main()
