from pathlib import Path
import base64, gzip, json, mimetypes, shutil

root=Path(__file__).resolve().parent.parent
assets={}
for path in sorted((root/'public').rglob('*')):
    if not path.is_file():
        continue
    mime=mimetypes.guess_type(path.name)[0] or 'application/octet-stream'
    if mime.startswith('text/') or mime in ('application/javascript','application/json'):
        mime+='; charset=utf-8'
    assets['/'+path.relative_to(root/'public').as_posix()]={
        'type':mime,
        'data':base64.b64encode(path.read_bytes()).decode('ascii')
    }
output=root/'dist'
if output.exists():
    shutil.rmtree(output)
(output/'server').mkdir(parents=True)
(output/'.openai').mkdir()
source='const ASSETS='+json.dumps(assets,separators=(',',':'))+';\n'+(root/'worker/index.js').read_text()
(output/'server/index.js').write_text(source)
shutil.copyfile(root/'.openai/hosting.json',output/'.openai/hosting.json')
print(f'Embedded {len(assets)} assets; Worker size {len(source):,} bytes.')
