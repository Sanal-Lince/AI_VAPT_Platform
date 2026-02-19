import {useState} from "react"

export default function ReportViewer(){
 const [r,setR]=useState("")

 const gen=async()=>{
  const res=await fetch("http://localhost:8000/report/generate",{
   method:"POST",
   headers:{"Content-Type":"application/json"},
   body:JSON.stringify(["SQL injection","Weak password"])
  })
  const d=await res.json()
  setR(d.report)
 }

 return(
  <div>
   <button onClick={gen}>Generate Report</button>
   <pre>{r}</pre>
  </div>
 )
}
