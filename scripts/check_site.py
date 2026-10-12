from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
ROOT=Path(__file__).resolve().parents[1]/'dist'
class Check(HTMLParser):
    def __init__(self,path):super().__init__();self.path=path;self.headings=0
    def handle_starttag(self,tag,attributes):
        attrs=dict(attributes)
        if tag=='h1':self.headings+=1
        for key in ('href','src'):
            value=attrs.get(key,'');url=urlsplit(value)
            if not value or url.scheme or value.startswith('#'):continue
            target=(ROOT/unquote(url.path).lstrip('/')) if value.startswith('/') else (self.path.parent/unquote(url.path))
            if target.is_dir():target=target/'index.html'
            assert target.is_file(),(self.path,value)
for path in ROOT.rglob('*.html'):
    parser=Check(path);parser.feed(path.read_text());assert parser.headings==1,path
assert (ROOT/'CNAME').read_text().strip()=='emet.clavesol.com.br'
print('Páginas, recursos e links locais verificados.')
