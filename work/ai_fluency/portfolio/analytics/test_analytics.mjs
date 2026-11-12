import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {gunzipSync} from 'node:zlib';
const code=await readFile('dist/server/index.js','utf8');
const app=(await import('data:text/javascript;base64,'+Buffer.from(code).toString('base64'))).default;
const objects=new Map();
const bucket={
 async put(key,body){objects.set(key,body);},
 async list({prefix}){return {objects:[...objects.keys()].filter(k=>k.startsWith(prefix)).map(key=>({key})),truncated:false};}
};
const pending=[];
const ctx={waitUntil:p=>pending.push(p)};
const run=(path,options={},env={BUCKET:bucket})=>app.fetch(new Request('https://portfolio.example'+path,options),env,ctx);
for(const path of ['/','/work.html','/about']){
 const response=await run(path);assert.equal(response.status,200);
 const html=Buffer.from(await response.arrayBuffer()).toString();
 assert.ok(html.includes('FR-D11-46B4B-A9584'));
}
await Promise.all(pending);assert.equal(objects.size,3);
assert.equal(new Set(objects.keys()).size,3);
assert.ok([...objects.values()].every(value=>value==='{}'));
await run('/work?private_query=not_saved',{headers:{DNT:'1'}});
await run('/about',{headers:{'Sec-GPC':'1'}});
await run('/?no_count=1');
await run('/work',{method:'HEAD'});
await Promise.all(pending);assert.equal(objects.size,3);
assert.equal((await run('/missing')).status,404);
assert.equal((await run('/work',{method:'POST'})).status,405);
const result=await (await run('/api/analytics')).json();
assert.deepEqual(result.totals,{home:1,work:1,about:1});
assert.equal(result.limited,false);
assert.equal((await run('/api/analytics',{},{})).status,503);
assert.equal((await run('/api/analytics',{},{BUCKET:{async list(){throw Error('storage down');}}})).status,503);
const capped=await (await run('/api/analytics',{},{BUCKET:{async list(){return {objects:[],truncated:true,cursor:'more'};}}})).json();
assert.equal(capped.limited,true);
assert.equal((await run('/analytics')).status,200);
console.log('Analytics checks passed: page serving, event privacy, independent event keys, opt-outs, aliases, methods, totals, storage failures and truncation. Storage is mocked; not production traffic.');
