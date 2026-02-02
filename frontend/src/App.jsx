import React, {useState, useEffect} from 'react'

function parseCSV(text){
  if(!text) return []
  const rows = text.trim().split('\n').map(r=>r.split(','))
  const headers = rows.shift()
  return rows.map(r=> Object.fromEntries(r.map((v,i)=>[headers[i].trim(), v.trim()])))
}

function CSVTable({data}){
  if(!data || data.length===0) return <p>No data</p>
  const headers = Object.keys(data[0])
  return (
    <table>
      <thead>
        <tr>{headers.map(h=> <th key={h}>{h}</th>)}</tr>
      </thead>
      <tbody>
        {data.map((row, idx)=> (
          <tr key={idx}>{headers.map(h=> <td key={h}>{row[h]}</td>)}</tr>
        ))}
      </tbody>
    </table>
  )
}

export default function App(){
  const [gainers, setGainers] = useState([])
  const [losers, setLosers] = useState([])
  const [loading, setLoading] = useState(false)
  const [syncing, setSyncing] = useState(false)

  const fetchData = async ()=>{
    setLoading(true)
    try{
      const g = await (await fetch('http://localhost:5000/data/gainers')).text()
      setGainers(parseCSV(g))
    }catch(e){ setGainers([]) }
    try{
      const l = await (await fetch('http://localhost:5000/data/losers')).text()
      setLosers(parseCSV(l))
    }catch(e){ setLosers([]) }
    setLoading(false)
  }

  useEffect(()=>{ fetchData() }, [])

  const handleSync = async ()=>{
    setSyncing(true)
    try{
      await fetch('http://localhost:5000/sync', { method: 'POST' })
      await fetchData()
    }catch(e){ console.error(e) }
    setSyncing(false)
  }

  return (
    <div className="container">
      <header>
        <h1>Top Gainers & Losers</h1>
        <button onClick={handleSync} disabled={syncing}>{syncing? 'Syncing...':'Sync'}</button>
      </header>
      {loading? <p>Loading...</p> : (
        <div className="grids">
          <section>
            <h2>Top Gainers</h2>
            <CSVTable data={gainers} />
          </section>
          <section>
            <h2>Top Losers</h2>
            <CSVTable data={losers} />
          </section>
        </div>
      )}
    </div>
  )
}
