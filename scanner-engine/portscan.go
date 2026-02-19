package main
import ("fmt";"net")

func main(){
 host:="scanme.nmap.org"
 for p:=1;p<=1024;p++{
  addr:=fmt.Sprintf("%s:%d",host,p)
  conn,err:=net.Dial("tcp",addr)
  if err==nil{
   fmt.Println("OPEN",p)
   conn.Close()
  }
 }
}
