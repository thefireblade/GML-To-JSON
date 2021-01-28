from networkx.readwrite import json_graph
import networkx as nx

import json
import os, fnmatch
if __name__ == "__main__":
    listOfFiles = os.listdir('.')
    pattern = "*.gml"
    for entry in listOfFiles:
        if fnmatch.fnmatch(entry, pattern):
            graph_to_convert = nx.read_gml(entry)
            data = json_graph.node_link_data(
                graph_to_convert, {"link": "links", "source": "from", "target": "to"}
            )
            with open(entry.split('.')[0] + '.json', 'w') as outfile:
                json.dump(data, outfile, default={
                    "link": "links", "source": "from", "target": "to"
                    })


