import base64
from urllib.request import urlretrieve

INPUT_FILE = "graph.md"

with open(INPUT_FILE, "r") as graph_file:
    graph_code = graph_file.read().replace('"', '\\"')
    g_code = '{"code":"%s","mermaid":{"theme":"default"}}' % (graph_code,)
    base64_graph = base64.urlsafe_b64encode(
        g_code.replace("\n", "\\n").encode("utf-8")
    )
    link = "https://mermaid.ink/img/%s" % base64_graph.decode("utf-8")
    print(link)
    urlretrieve(link, "output.jpeg")
