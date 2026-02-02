function parseCSV(text){
  if(!text) return []
  const rows = text.trim().split('\n').map(r=>r.split(','))
  const headers = rows.shift().map(h=>h.trim())
  return rows.map(r=> Object.fromEntries(r.map((v,i)=>[headers[i]||i, (v||'').trim()])))
}

function renderTable(container, data){
  if(!data || data.length===0){ container.innerHTML = '<p>No data</p>'; return }
  const headers = Object.keys(data[0])
  let html = '<table><thead><tr>' + headers.map(h=>`<th>${h}</th>`).join('') + '</tr></thead><tbody>'
  html += data.map(row => '<tr>' + headers.map(h=>`<td>${row[h]||''}</td>`).join('') + '</tr>').join('')
  html += '</tbody></table>'
  container.innerHTML = html
}

async function fetchAndRender(){
  const status = document.getElementById('status')
  status.textContent = 'Refreshing data...'
  try{
    const gTxt = await (await fetch('http://localhost:5000/data/gainers')).text()
    const lTxt = await (await fetch('http://localhost:5000/data/losers')).text()
    renderTable(document.getElementById('gainers'), parseCSV(gTxt))
    renderTable(document.getElementById('losers'), parseCSV(lTxt))
    status.textContent = ''
  }catch(e){
    status.textContent = 'Error loading data. Is the backend running?'
  }
}

document.getElementById('sync').addEventListener('click', async ()=>{
  const status = document.getElementById('status')
  status.textContent = 'Syncing...'
  try{
    const res = await fetch('http://localhost:5000/sync', { method: 'POST' })
    if(res.ok){
      status.textContent = 'Sync complete. Refreshing...'
      await fetchAndRender()
    }else{
      const err = await res.json().catch(()=>null)
      status.textContent = 'Sync failed: ' + (err?.error || 'server error')
    }
  }catch(e){
    status.textContent = 'Sync request failed. Is the backend running?'
  }
})

fetchAndRender()
