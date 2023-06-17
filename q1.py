import streamlit as st
from collections import deque


class GraphSearch:
    def __init__(self, graph):
        self.graph = graph

    def breadth_first_search(self, initial_state, goal_state):
        return convert_graph_to_queue(self.graph, initial_state, goal_state)

    def depth_first_search(self, initial_state, goal_state):
        return convert_graph_to_stack(self.graph, initial_state, goal_state)


def convert_graph_to_queue(graph, initial_state, goal_state):
    queue = deque()
    visited = set()
    queue.append((initial_state, []))  # Initial state and an empty path
    visited.add(initial_state)

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]

        for neighbor in graph[state]:
            if neighbor not in visited:
                queue.append((neighbor, path + [state]))
                visited.add(neighbor)

    return []


def convert_graph_to_stack(graph, initial_state, goal_state):
    stack = []
    visited = set()
    stack.append((initial_state, []))  # Initial state and an empty path

    while stack:
        state, path = stack.pop()

        if state == goal_state:
            return path + [state]

        if state not in visited:
            visited.add(state)
            for neighbor in graph[state]:
                stack.append((neighbor, path + [state]))

    return []


def main():
   # State space graph
    graph = {
             'Addis Ababa': {'Adama', 'Ambo', 'Debre Berhan'},
             'Adama': {'Matahara', 'Asella', 'Batu', 'Addis Ababa'}, 
             'Ambo': {'Wolkite', 'Addis Ababa', 'Nekemte'}, 
             'Debre Berhan': {'Addis Ababa', 'Debre Sina'}, 
             'Matahara': {'Adama', 'Awash'}, 
             'Asella': {'Adama', 'Assasa'}, 
             'Batu': {'Adama', 'Buta Jirra', 'Shashamene'}, 
             'Wolkite': {'Ambo', 'Worabe', 'Jimma'}, 
             'Nekemte': {'Ambo', 'Bedelle', 'Gimbi'}, 
             'Debre Sina': {'Debre Berhan', 'Kemise', 'Debre Markos'}, 
             'Awash': {'Chiro', 'Gobi Rasu', 'Matahara'}, 
             'Assasa': {'Asella', 'Dodolla'}, 
             'Buta Jirra': {'Batu', 'Worabe'}, 
             'Shashamene': {'Batu', 'Hawassa', 'Dodolla', 'Hossana'}, 
             'Worabe': {'Wolkite', 'Hossana', 'Buta Jirra'}, 
             'Jimma': {'Wolkite', 'Bonga', 'Bedelle'}, 
            'Bedelle': {'Nekemte', 'Gore', 'Jimma'}, 
             'Gimbi': {'Nekemte', 'Dambidollo'}, 
             'Kemise': {'Debre Sina', 'Dessie'}, 
             'Debre Markos': {'Debre Sina', 'Finote Selam'},
             'Chiro': {'Awash', 'Dire Dawa'}, 
             'Gobi Rasu': {'Awash', 'Samara'}, 
             'Dodolla': {'Assasa', 'Shashamene', 'Bale'}, 
             'Hawassa': {'Shashamene', 'Dilla'}, 
             'Hossana': {'Shashamene', 'Worabe', 'Wolaita Sodo'}, 
             'Bonga': {'Jimma', 'Dawro', 'Tepi', 'Mizan Teferi'}, 
             'Gore': {'Tepi', 'Gambella', 'Bedelle'}, 
             'Dambidollo': {'Gimbi', 'Assosa', 'Gambella'}, 
            'Dessie': {'Kemise', 'Woldia'}, 
            'Finote Selam': {'Debre Markos', 'Bahirdar', 'Injibara'}, 
             'Dire Dawa': { 'Chiro', 'Harar'}, 
             'Samara': { 'Gobi Rasu', 'Fanti Rasu', 'Alamata', 'Woldia'},
            'Bale': {'Liben', 'Dodolla', 'Goba', 'Sof Oumer'}, 
             'Dilla': {'Hawassa', 'Bulehora'}, 
             'Wolaita Sodo': {'Arba Minchi', 'Dawro', 'Hossana'}, 
             'Dawro': { 'Bonga', 'Basketo', 'Wolaita Sodo'}, 
             'Tepi': {'Gore', 'Bonga', 'Mizan Teferi'}, 
            'Mizan Teferi': {'Tepi', 'Bonga', 'Basketo'}, 
             'Gambella': {'Gore', 'Dambidollo'}, 
             'Assosa': {'Dambidollo', 'Metekel'}, 
            'Woldia': {'Dessie', 'Lalibella', 'Samara', 'Alamata'},
             'Bahirdar': {'Finote Selam', 'Injibara', 'Metekel', 'Azezo', 'Debre Tabor'}, 
             'Injibara': {'Bahirdar', 'Finote Selam'}, 
             'Harar': { 'Dire Dawa', 'Babile'}, 
             'Fanti Rasu': {'Samara', 'Kilbet Rasu'}, 
             'Alamata': {'Samara', 'Woldia', 'Mekelle', 'Sekota'}, 
             'Liben': {'Bale'}, 
             'Goba': {'Bale', 'Sof Oumer', 'Dega Habur'}, 
             'Sof Oumer': {'Goba', 'Bale', 'Kebri Dehar'}, 
            'Bulehora': { 'Dilla', 'Yabello'}, 
            'Arba Minchi': {'Wolaita Sodo', 'Konso', 'Basketo'}, 
             'Basketo': { 'Arba Minchi', 'Dawro', 'Mizan Teferi', 'Benchi Maji'}, 
             'Metekel': { 'Assosa', 'Bahirdar'},
             'Lalibella': {'Woldia', 'Debre Tabor', 'Sekota'},
             'Debre Tabor': {'Lalibella', 'Bahirdar'}, 
             'Azezo': {'Gondar', 'Bahirdar', 'Metema'}, 
             'Babile': { 'Harar', 'Jigjiga'}, 
             'Kilbet Rasu': {'Fanti Rasu' }, 
             'Mekelle': {'Alamata', 'Adwa', 'Adigrat', 'Sekota'}, 
             'Sekota': {'Alamata', 'Mekelle', 'Lalibella'}, 
            'Dega Habur': {'Goba', 'Jigjiga', 'Kebri Dehar'}, 
            'Kebri Dehar': {'Gode', 'Sof Oumer', 'Dega Habur', 'Werdez'}, 
            'Yabello': { 'Bulehora', 'Konso', 'Moyale'}, 
            'Konso': {'Arba Minchi', 'Yabello'}, 
            'Benchi Maji': { 'Basketo'}, 
            'Gondar': { 'Azezo', 'Metema', 'Debarke'},
            'Metema': { 'Azezo', 'Gondar'},  
            'Jigjiga': { 'Babile', 'Dega Habur'}, 
            'Adwa': { 'Mekelle', 'Axum', 'Adigrat'},
            'Adigrat': { 'Mekelle', 'Adwa'}, 
            'Gode': { 'Dollo', 'Kebri Dehar' }, 
            'Werdez': { 'Kebri Dehar'}, 
            'Moyale': { 'Yabello'}, 
            'Debarke': { 'Gondar', 'Shire'}, 
            'Axum': {'Shire', 'Adwa'}, 
            'Dollo': { 'Gode'}, 
            'Shire': { 'Axum', 'Humera', 'Debarke'},
            'Humera': { 'Shire', 'Gondar'}
            }


    # Create an instance of GraphSearcha
    search = GraphSearch(graph)

    # Get all nodes from the graph
    nodes = list(graph.keys())

    # Streamlit app title and description
    st.title("Ethiopian Traveling Search Problem")
    st.write("Enter the initial state, goal state, and search strategy.")

    # Get user inputs
    initial_state = st.selectbox("Initial State", nodes)
    goal_state = st.selectbox("Goal State", nodes)
    search_strategy = st.selectbox("Search Strategy", ["BFS", "DFS"])

    # Perform graph search based on the selected strategy
    if st.button("Find Path"):
        path = []
        if search_strategy == "BFS":
            path = search.breadth_first_search(initial_state, goal_state)
        elif search_strategy == "DFS":
            path = search.depth_first_search(initial_state, goal_state)

        # Display the result
        if path:
            st.success(f"Path found: {path}")
        else:
            st.error("No path found.")


if __name__ == "__main__":
    main()
