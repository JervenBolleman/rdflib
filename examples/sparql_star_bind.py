"""

A simple example showing how to process Bind over Sparql Star format query

"""

from rdflib import Graph

if __name__ == '__main__':
    g = Graph()

    g.parse('sample.ttl', format='turtle')

    for row in g.query('''
                        SELECT ?x WHERE{ <<?s ?p ?o>> ?p1 ?o1 .
                        BIND(<<?s ?p ?o>> AS ?x)
                        }'''):
        print(row)



