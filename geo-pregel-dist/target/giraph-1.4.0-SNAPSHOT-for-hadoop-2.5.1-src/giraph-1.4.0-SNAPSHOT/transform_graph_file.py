graph_file_name="/home/cluster_share/graph/soc-LiveJournal1_notmap.txt"
out_put_file_name='/home/amax/Graph_json/livejournal_not_mapped_json'

graph_file = open(graph_file_name)
output_file = open(out_put_file_name, 'w')

edge = dict()

for line in graph_file:
    #line = line[:-2]
    res = line.split()
    #print(res)
    source = int(res[0])
    dest = int(res[1])
    if edge.has_key(source):
        edge[source].append(dest)
    else:
        edge[source] = [dest]

for source in edge:
    edges = edge[source]
    output_file.write("["+str(source)+",0,[")
    output_file.write(",".join("["+str(i)+",0]" for i in edges))
    output_file.write("]]\n")

graph_file.close()
output_file.close()

