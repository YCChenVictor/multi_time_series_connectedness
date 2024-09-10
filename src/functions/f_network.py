import networkx as nx
from fa2 import ForceAtlas2
import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt


class Create_Network:

    def __init__(self, connectedness_table):
        self.Connectedness_table = connectedness_table
        self.Names = None
        self.From_other = None
        self.To_other = None
        self.Graph = None
        self.Plot = None

    def change_names(self, names):

        self.Names = names

    def create_network(self):

        graph = nx.Graph()

        connectedness_table = self.Connectedness_table

        self.From_other = connectedness_table.iloc[:, -1]
        self.To_other = connectedness_table.iloc[-1, :]

        connectedness_table = connectedness_table[:-1]
        connectedness_table = connectedness_table.iloc[:, :-1]

        connectedness = connectedness_table.values

        for i in range(len(connectedness)):
            for j in range(len(connectedness[i])):
                """
                Use average of to and from connectedness to represent the
                degree of bondness, however, causing we can't tell the to and
                from degree, needs more modification

                connectedness[i][j] means
                """
                if i == j:
                    break
                else:
                    if self.Names is None:
                        graph.add_edge(i, j, weight=(connectedness[i][j] +
                                                     connectedness[j][i]) / 2)
                    else:
                        graph.add_edge(self.Names[i], self.Names[j],
                                       weight=(connectedness[i][j] +
                                               connectedness[j][i]) / 2)

        self.Graph = graph

    def plot(self):

        forceatlas2 = ForceAtlas2(

            # Behavior alternatives
            outboundAttractionDistribution=False,  # Dissuade hubs
            linLogMode=False,  # NOT IMPLEMENTED
            adjustSizes=False,  # Prevent overlap (NOT IMPLEMENTED)
            edgeWeightInfluence=1.0,

            # Performance
            jitterTolerance=1.0,  # Tolerance
            barnesHutOptimize=True,
            barnesHutTheta=1.2,
            multiThreaded=False,  # NOT IMPLEMENTED

            # Tuning
            scalingRatio=2.0,
            strongGravityMode=False,
            gravity=1.0,

            # Log
            verbose=True)

        positions = (forceatlas2.
                     forceatlas2_networkx_layout(self.Graph,
                                                 pos=None,
                                                 iterations=2000))
        self.Plot = nx.draw_networkx(self.Graph, positions,
                                     cmap=plt.get_cmap('jet'),
                                     node_size=50, with_labels=True)

    def show_draw(self):

        plt.show(self.Plot)

    def close_draw(self):

        plt.close(self.Plot)
