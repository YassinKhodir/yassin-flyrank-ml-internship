// ASSETS is embedded by scripts/build_worker.py; no runtime file-system access.
const pages = {"/":"home", "/work":"work", "/about":"about"};
const aliases = {"/index.html":"/", "/work.html":"/work", "/about.html":"/about", "/analytics.html":"/analytics"};
const json = (value, status=200) => new Response(JSON.stringify(value), {status, headers:{"Content-Type":"application/json; charset=utf-8", "Cache-Control":"no-store"}});

async function counts(bucket) {
  const days=[];
  for (let n=0;n<7;n++) days.push(new Date(Date.now()-n*86400000).toISOString().slice(0,10));
  const totals={home:0,work:0,about:0};
  let limited=false;
  for (const day of days) {
    let cursor;
    for (let batch=0;batch<5;batch++) {
      const result=await bucket.list({prefix:`views/${day}/`, limit:1000, ...(cursor?{cursor}:{})});
      for (const object of result.objects) {
        const page=object.key.split('/')[2];
        if (Object.hasOwn(totals,page)) totals[page]++;
      }
      if (!result.truncated) break;
      if (batch===4) limited=true;
      cursor=result.cursor;
    }
  }
  return {from:days.at(-1), through:days[0], totals, limited, unit:"page requests", includes_tests:true};
}

export default {
  async fetch(request, env, ctx) {
    const url=new URL(request.url);
    if (!['GET','HEAD'].includes(request.method)) return new Response('Method not allowed',{status:405,headers:{Allow:'GET, HEAD'}});
    if (url.pathname==='/api/analytics') {
      if (!env.BUCKET) return json({error:'Analytics storage is unavailable.'},503);
      try { return json(await counts(env.BUCKET)); }
      catch { return json({error:'Analytics could not be read. Try again later.'},503); }
    }
    const path=aliases[url.pathname] || url.pathname;
    const assetPath=path==='/'?'/index.html':path==='/work'?'/work.html':path==='/about'?'/about.html':path==='/analytics'?'/analytics.html':path;
    const asset=ASSETS[assetPath];
    if (!asset) return new Response('Page not found',{status:404});
    // Only these three page requests are counted. No IP, user agent, referrer,
    // query string, cookie or reusable visitor identifier is stored.
    if (request.method==='GET' && pages[path] && env.BUCKET && request.headers.get('DNT')!=='1' && request.headers.get('Sec-GPC')!=='1' && url.searchParams.get('no_count')!=='1') {
      const day=new Date().toISOString().slice(0,10);
      const key=`views/${day}/${pages[path]}/${crypto.randomUUID()}.json`;
      ctx.waitUntil(env.BUCKET.put(key,'{}',{httpMetadata:{contentType:'application/json'}}).catch(()=>{}));
    }
    const bytes=Uint8Array.from(atob(asset.data), c=>c.charCodeAt(0));
    return new Response(request.method==='HEAD'?null:bytes,{headers:{'Content-Type':asset.type,'Cache-Control':asset.type.startsWith('text/html')?'no-store':'public, max-age=3600','X-Content-Type-Options':'nosniff'}});
  }
};
