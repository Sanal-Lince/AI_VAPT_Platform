export async function scan(target){
 const r=await fetch(`http://localhost:8000/scan/port?target=${target}`)
 return r.json()
}
