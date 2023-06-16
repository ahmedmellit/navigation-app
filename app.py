import streamlit as st
from heapq import heappop, heappush
import pandas as pd
import numpy as np

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}  # Initialisation des distances à l'infini pour chaque nœud
    distances[start] = 0  # La distance du nœud de départ est définie à 0
    visited = set()  # Ensemble des nœuds visités

    pq = [(0, start)]  # Initialisation de la file de priorité avec le nœud de départ

    while pq:
        current_distance, current_node = heappop(pq)  # Retirer le nœud avec la plus petite distance actuelle de la file de priorité
        visited.add(current_node)  # Ajouter le nœud visité à l'ensemble des nœuds visités

        if current_node == end:  # Si le nœud actuel est le nœud d'arrivée, on a trouvé le chemin optimal
            break

        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:  # Vérifier si le voisin n'a pas été visité
                distance = current_distance + weight

                if distance < distances[neighbor]:  # Vérifier si la nouvelle distance est plus courte que la distance précédemment enregistrée
                    distances[neighbor] = distance  # Mettre à jour la distance du voisin
                    heappush(pq, (distance, neighbor))  # Ajouter le voisin à la file de priorité avec sa nouvelle distance

    return distances

def main():
    st.title("Application de navigation accessible aux fauteuils roulants")

    min_lat, max_lat = 34.00, 34.10
    min_lon, max_lon = -5.05, -4.95

    num_points = 200
    latitudes = np.random.uniform(min_lat, max_lat, size=num_points)
    longitudes = np.random.uniform(min_lon, max_lon, size=num_points)

    df = pd.DataFrame({'lat': latitudes, 'lon': longitudes})

    st.map(df)

    st.write("Entrez les nœuds de départ et d'arrivée pour trouver le chemin optimal accessible aux fauteuils roulants.")

    graph = {
    'Ain Nokbi Park': {'Al-Qarawiyyin Mosque': 2, 'Jardin Jnan Sbil': 3, 'Batha Museum': 4},
    'Al-Attarine Madrasa': {'Bou Inania Madrasa': 1, 'Nejjarine Museum': 3, 'Bab Bou Jeloud': 4},
    'Al-Qarawiyyin Mosque': {'Ain Nokbi Park': 2, 'Bou Inania Madrasa': 3, 'Batha Museum': 1},
    'Bab Bou Jeloud': {'Al-Attarine Madrasa': 4, 'Nejjarine Museum': 2, 'Jardin Jnan Sbil': 1},
    'Batha Museum': {'Ain Nokbi Park': 4, 'Al-Qarawiyyin Mosque': 1, 'Bou Inania Madrasa': 3},
    'Bou Inania Madrasa': {'Al-Attarine Madrasa': 1, 'Al-Qarawiyyin Mosque': 3, 'Batha Museum': 3},
    'Dar Batha Museum': {'Nejjarine Museum': 2, 'Jardin Jnan Sbil': 4, 'Bab Bou Jeloud': 3},
    'Fez Mellah': {'Nejjarine Museum': 4, 'Dar Batha Museum': 2, 'Bab Bou Jeloud': 1},
    'Ibn Danan Synagogue': {'Fez Mellah': 3, 'Dar Batha Museum': 2, 'Jardin Jnan Sbil': 4},
    'Jardin Jnan Sbil': {'Ain Nokbi Park': 3, 'Bab Bou Jeloud': 1, 'Dar Batha Museum': 4},
    'Kairaouine Mosque': {'Jardin Jnan Sbil': 3, 'Bou Inania Madrasa': 2, 'Bab Bou Jeloud': 4},
    'Madrasa Bou Inania': {'Al-Qarawiyyin Mosque': 3, 'Kairaouine Mosque': 2, 'Jardin Jnan Sbil': 1},
    'Moulay Idriss II Mausoleum': {'Fez Mellah': 2, 'Dar Batha Museum': 4, 'Bab Bou Jeloud': 3},
    'Nejjarine Museum': {'Al-Attarine Madrasa': 3, 'Bab Bou Jeloud': 2, 'Dar Batha Museum': 2},
    'Royal Palace of Fes': {'Fez Mellah': 4, 'Ibn Danan Synagogue': 3, 'Bab Bou Jeloud': 2},
    'University of Al Quaraouiyine': {'Bou Inania Madrasa': 2, 'Jardin Jnan Sbil': 4, 'Batha Museum': 3},
    'Dar el-Makhzen': {'Fez Mellah': 3, 'Jardin Jnan Sbil': 2, 'Bab Bou Jeloud': 1},
    'Boulevard Hassan II': {'Ain Nokbi Park': 4, 'Dar Batha Museum': 2, 'Jardin Jnan Sbil': 3},
    'Royal Golf de Fes': {'Ain Nokbi Park': 3, 'Batha Museum': 4, 'Bab Bou Jeloud': 1},
    'Borj Nord': {'Al-Qarawiyyin Mosque': 4, 'Bou Inania Madrasa': 1, 'Jardin Jnan Sbil': 2},
    'Borj Sud': {'Al-Attarine Madrasa': 1, 'Jardin Jnan Sbil': 4, 'Batha Museum': 3},
    'Medersa Es-Sahrij': {'Al-Qarawiyyin Mosque': 2, 'Bou Inania Madrasa': 4, 'Jardin Jnan Sbil': 1},
    'Dar Adiyel': {'Ain Nokbi Park': 3, 'Al-Attarine Madrasa': 2, 'Bab Bou Jeloud': 1},
    'Riad Fes': {'Bou Inania Madrasa': 4, 'Jardin Jnan Sbil': 2, 'Batha Museum': 3},
    'Dar Seffarine': {'Fez Mellah': 1, 'Dar Batha Museum': 3, 'Bab Bou Jeloud': 2},
    'Karaouiyne University Hospital': {'Ain Nokbi Park': 2, 'Al-Qarawiyyin Mosque': 4, 'Batha Museum': 3},
    'Al-Saffarin Madrasa': {'Al-Attarine Madrasa': 1, 'Jardin Jnan Sbil': 4, 'Bab Bou Jeloud': 2},
    'Chouara Tannery': {'Fez Mellah': 3, 'Dar Batha Museum': 2, 'Jardin Jnan Sbil': 4},
    'Bab Boujloud': {'Jardin Jnan Sbil': 1, 'Bou Inania Madrasa': 3, 'Batha Museum': 4},
    'Andalusian Mosque': {'Ain Nokbi Park': 4, 'Al-Qarawiyyin Mosque': 2, 'Bab Bou Jeloud': 3},
    'Royal Palace': {'Fez Mellah': 3, 'Dar Batha Museum': 2, 'Jardin Jnan Sbil': 4}
    }

    nodes = list(graph.keys())

    start_node = st.selectbox("Sélectionnez le nœud de départ :", nodes)
    end_node = st.selectbox("Sélectionnez le nœud de destination :", nodes)

    distances = dijkstra(graph, start_node, end_node)
    optimal_path = []

    current_node = end_node
    while current_node != start_node:
        optimal_path.append(current_node)
        current_node = min(graph[current_node], key=lambda node: distances[node] + graph[current_node][node])
    optimal_path.append(start_node)
    optimal_path.reverse()

    st.write("Chemin optimal :")
    st.write(optimal_path)

    st.write("Distance totale :", distances[end_node])

if __name__ == "__main__":
    main()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
