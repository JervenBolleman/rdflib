"""

A simple example showing how to process RDFa from the web

"""

from rdflib import Graph

if __name__ == '__main__':
    g = Graph()

    g.parse('sample.ttl', format='turtle')

    print("Books found:")

    res = g.query("SELECT ?s1 WHERE{<<<<?s1 ?p1 ?o1>> ?p2 ?o2>> ?p3 ?o3.}")
    print(list(res))


