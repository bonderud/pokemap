import heapq
from collections import defaultdict
from fuzzywuzzy import process  # Or import from rapidfuzz

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance=1):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph, start, end):
    queue = [(0, start)]
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    previous_nodes = {node: None for node in graph.nodes}
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.edges[current_node]:
            distance = current_distance + graph.distances[(current_node, neighbor)]
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path, current_node = [], end
    while previous_nodes[current_node] is not None:
        path.append(current_node)
        current_node = previous_nodes[current_node]
    if path:
        path.append(start)
        path.reverse()
    
    return path, distances[end]

def get_start_and_end_locations(graph):
    locations = list(graph.nodes)
    
    print("Enter the starting location name or abbreviation:")
    start_location = input().strip()
    best_start_match = process.extractOne(start_location, locations)[0]

    if best_start_match not in locations:
        print(f"Location '{start_location}' does not exist in the graph. Please try again.")
        return get_start_and_end_locations(graph)

    print(f"Best match for starting location '{start_location}' is '{best_start_match}'")
    
    print("Enter the ending location name or abbreviation:")
    end_location = input().strip()
    best_end_match = process.extractOne(end_location, locations)[0]

    if best_end_match not in locations:
        print(f"Location '{end_location}' does not exist in the graph. Please try again.")
        return get_start_and_end_locations(graph)

    print(f"Best match for ending location '{end_location}' is '{best_end_match}'")

    return best_start_match, best_end_match

def find_and_print_optimal_path(graph):
    start_location, end_location = get_start_and_end_locations(graph)
    
    path, distance = dijkstra(graph, start_location, end_location)
    
    if path:
        print(f"Optimal path from {start_location} to {end_location}: {' -> '.join(path)}")
        print(f"Total distance: {distance}")
    else:
        print(f"No path found from {start_location} to {end_location}.")

# Example graph setup
graph = Graph()

# Add locations (as nodes)
graph.add_node('Vanalue Town')  # The starting point for the map
graph.add_node('Vanlue Countryside')
graph.add_node('Alatur Mine')
graph.add_node('Forest Path')
graph.add_node('Maris Crossing')
graph.add_node('Ragmeer Volcano')
graph.add_node('Trodga Town')
graph.add_node('Archaic Chamber')
graph.add_node('Golt Prairie')
graph.add_node('Floret Spring')
graph.add_node('Mirage Path')
graph.add_node('Ragnel Tunnel')
graph.add_node('Colbathar Snowfield') 
graph.add_node('Ragnel Crater')
graph.add_node('Trogda Town')
graph.add_node('Waterfall Cave')
graph.add_node('Celosia Square')
graph.add_node('Haunted Manor')
graph.add_node('Moonlight Grove')
graph.add_node('Ravaged Canyon')
graph.add_node('Wevas City')
graph.add_node('Celosia City')
graph.add_node('Hudai Lake')
graph.add_node('Mowe Village')
graph.add_node('Safari Zone')
graph.add_node('Whirl Cenote')
graph.add_node('Colbalthar Snowfield')
graph.add_node('Icicle Ridge')
graph.add_node('Mushroom Grotto')
graph.add_node('Shadowcrept Hollow')
graph.add_node('Wrecked Ship')
graph.add_node('Cold Shelter')
graph.add_node('Ivy Ampitheater')
graph.add_node('Nola Pier')
graph.add_node('Shattershock Silo')
graph.add_node('Entoria Forest')
graph.add_node('Kaya Peak')
graph.add_node('Nola Seaview')
graph.add_node('Shimmering Oasis')
graph.add_node('Eoni City')
graph.add_node('Kuldova Town')
graph.add_node('Perimos Bazaar')
graph.add_node('Slowpoke Well')
graph.add_node('Excavation Site')
graph.add_node('Lilox Village')
graph.add_node('Perimos Desert')
graph.add_node('Solex Stronghold')
graph.add_node('Finoth Woods')
graph.add_node('Loret Jungle')
graph.add_node('Priman Town')
graph.add_node('Typhler Bridge')
graph.add_node('Fishing Hole')
graph.add_node('Magnified Shrine')
graph.add_node('Psyfactory')
graph.add_node('The Moon')
graph.add_node('Route 1')
graph.add_node('Route 12')
graph.add_node('Route 23')
graph.add_node('Route 2')
graph.add_node('Route 13')
graph.add_node('Route 24')
graph.add_node('Route 3')
graph.add_node('Route 14')
graph.add_node('Route 25')
graph.add_node('Route 4')
graph.add_node('Route 15')
graph.add_node('Route 26')
graph.add_node('Route 5')
graph.add_node('Route 16')
graph.add_node('Route 6')
graph.add_node('Route 17')
graph.add_node('Route 7')
graph.add_node('Route 18')
graph.add_node('Route 8')
graph.add_node('Route 19')
graph.add_node('Route 9')
graph.add_node('Route 20')
graph.add_node('Route 10')
graph.add_node('Route 21')
graph.add_node('Route 11')
graph.add_node('Route 22')

# Add special locations (as nodes)
graph.add_node('Phase Stones')
graph.add_node('Elemental Stones')
graph.add_node('Natural Stones')
graph.add_node('Flavorful Apple')
graph.add_node("Tiger's Eye")
graph.add_node("Dragon's Eye")
graph.add_node("Snake's Eye")
graph.add_node("Storm's Eye")

# Add directional edges to 'Vanalue Town'
for location in graph.nodes:
    if location != 'Vanalue Town' and location not in {'Vanlue Countryside', 'Route 8', 'Route 1', 'Route 22'}:
        graph.add_edge(location, 'Vanalue Town')

# Add two-way edges for specific locations
two_way_locations = ['Vanlue Countryside', 'Route 8', 'Route 1', 'Route 22']
for location in two_way_locations:
    graph.add_edge(location, 'Vanalue Town')
    graph.add_edge('Vanalue Town', location)

# List of edges to be reversed
edges = [
('Route 1', 'Mowe Village')
,('Mowe Village', 'Route 2')
,('Mowe Village', 'Route 13')
,('Route 13', 'Finoth Woods')
,('Route 2', 'Psyfactory')
,('Route 13', 'Excavation Site')
,('Excavation Site', 'Route 12')
,('Psyfactory', 'Route 3')
,('Route 3', 'Trogda Town')
,('Route 3', 'Entoria Forest')
,('Trogda Town', 'Route 9')
,('Entoria Forest', 'Ivy Ampitheater')
,('Entoria Forest', 'Route 4')
,('Route 9', 'Eoni City')
,('Route 4', 'Lilox Village')
,('Route 12', 'Mushroom Grotto')
,('Route 12', 'Wevas City')
,('Mushroom Grotto', 'Route 14')
,('Wevas City', 'Route 10')
,('Wevas City', 'Shadowcrept Hollow')
,('Shadowcrept Hollow', 'Haunted Manor')
,('Route 10', 'Safari Zone')
,('Eoni City', 'Maris Crossing')
,('Maris Crossing', 'Safari Zone')
,('Safari Zone', 'Route 11')
,('Route 11', 'Solex Stronghold')
,('Route 11', 'Wrecked Ship')
,('Route 11', 'Forest Path')
,('Forest Path', 'Moonlight Grove')
,('Lilox Village', 'Ragnel Tunnel')
,('Lilox Village', 'Route 5')
,('Ragnel Tunnel', 'Ragnel Crater')
,('Route 5', 'Typhler Bridge')
,('Typhler Bridge', 'Celosia Square')
,('Typhler Bridge', 'Route 6')
,('Celosia Square', 'Celosia City')
,('Celosia Square', 'Nola Pier')
,('Celosia City', 'The Moon')
,('Nola Pier', 'Nola Seaview')
,('Route 6', 'Slowpoke Well')
,('Route 6', 'Route 7')
,('Route 8', 'Hudai Lake')
,('Hudai Lake', 'Whirl Cenote')
,('Hudai Lake', 'Waterfall Cave')
,('Route 22', 'Floret Spring')
,('Vanlue Countryside', 'Priman Town')
,('Priman Town', 'Alatur Mine')
,('Route 7', 'Waterfall Cave')
,('Route 7', 'Route 15')
,('Route 15', 'Archaic Chamber')
,('Route 15', 'Perimos Bazaar')
,('Perimos Bazaar', 'Mirage Path')
,('Mirage Path', 'Shimmering Oasis')
,('Archaic Chamber', 'Route 16')
,('Route 16', 'Perimos Desert')
,('Perimos Desert', 'Route 18')
,('Route 18', 'Ravaged Canyon')
,('Route 18', 'Kuldova Town')
,('Kuldova Town', 'Route 19')
,('Route 19', 'Ragmeer Volcano')
,('Route 19', 'Loret Jungle')
,('Route 19', 'Route 20')
,('Route 20', 'Golt Prairie')
,('Golt Prairie', 'Route 21')
,('Route 21', 'Floret Spring')
,('Route 21', 'Cold Shelter')
,('Cold Shelter', 'Route 23')
,('Cold Shelter', 'Route 24')
,('Route 23', 'Fishing Hole')
,('Route 24', 'Colbathar Snowfield')
,('Fishing Hole', 'Route 25')
,('Route 25', 'Magnified Shrine')
,('Colbathar Snowfield', 'Route 26')
,('Colbathar Snowfield', 'Icicle Ridge')
,('Icicle Ridge', 'Kaya Peak')
,('Route 26', 'Shattershock Silo')
]

# Add the original edges
for from_node, to_node in edges:
    graph.add_edge(from_node, to_node)
    graph.add_edge(to_node, from_node)

# Find and print the optimal path
find_and_print_optimal_path(graph)