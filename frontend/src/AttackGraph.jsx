import ForceGraph2D from "react-force-graph-2d"
import {useEffect,useState} from "react"

export default function AttackGraph(){
 const [g,setG]=useState({nodes:[],links:[]})

 useEffect(()=>{
  fetch("http://localhost:8000/attack/graph",{
   method:"POST",
   headers:{"Content-Type":"application/json"},
   body:JSON.stringify([
    {source:"web",target:"sql"},
    {source:"sql",target:"db"},
    {source:"db",target:"root"}
   ])
  }).then(r=>r.json()).then(d=>{
   setG({
    nodes:d.nodes.map(n=>({id:n})),
    links:d.edges.map(e=>({source:e[0],target:e[1]}))
   })
  })
 },[])

 return <ForceGraph2D graphData={g}/>
}
