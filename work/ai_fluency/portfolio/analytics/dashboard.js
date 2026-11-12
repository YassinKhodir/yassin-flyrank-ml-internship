const refresh=document.getElementById('refresh-counts');
async function loadCounts(){
 refresh.disabled=true;
 const status=document.getElementById('analytics-status');
 status.textContent='Loading...';
 try{
  const response=await fetch('/api/analytics',{cache:'no-store'});
  const data=await response.json();
  if(!response.ok)throw new Error(data.error||'Counts are unavailable.');
  const body=document.getElementById('counts');body.replaceChildren();
  for(const [page,count] of Object.entries(data.totals)){
   const row=document.createElement('tr');
   for(const value of [page,count]){const cell=document.createElement('td');cell.textContent=String(value);cell.style.padding='12px';row.append(cell);}
   row.lastChild.style.textAlign='right';body.append(row);
  }
  document.getElementById('range').textContent=data.from+' through '+data.through+' (UTC days).';
  status.textContent=data.limited?'High-volume limit reached. These counts are lower bounds.':'Counts loaded. Includes testing and automated requests; not unique visitors.';
 }catch(error){status.textContent=error.message;}
 finally{refresh.disabled=false;}
}
refresh.addEventListener('click',loadCounts);loadCounts();
