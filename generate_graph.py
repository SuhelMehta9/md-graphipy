import base64
import urllib.request

INPUT_FILE = "graph.md"

with open(INPUT_FILE, "r") as graph_file:
    graph_code = graph_file.read().replace('"', '\\"')
    g_code = '{"code":"%s","mermaid":{"theme":"default"}}' % (graph_code,)
    base64_graph = base64.urlsafe_b64encode(
        g_code.replace("\n", "\\n").encode("utf-8")
    )
    link = "https://mermaid.ink/img/%s" % base64_graph.decode("utf-8")
    print("Image_link: " + link)
    hdrs = {
        "User-Agent": "Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari / 537.36"
    }
    opener = urllib.request.build_opener()
    opener.addheaders = [
        (
            "User-Agent",
            "Mozilla / 5.0 (X11 Linux x86_64) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 52.0.2743.116 Safari 537.36",
        )
    ]
    urllib.request.install_opener(opener)
    urllib.request.urlretrieve(link, "output.jpeg")
    print("\nFind downloaded image output.jpeg in current directory")
