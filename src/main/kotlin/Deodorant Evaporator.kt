fun evaporator(content: Double, evap_per_day: Double, threshold: Double): Int {
    var decreaseContent=content
    var days=0
    while(decreaseContent>threshold/100*content){
        decreaseContent-=(evap_per_day/100*decreaseContent)
        days+=1
    }
    return(days)
}
fun main() {
    println(evaporator(10.0,10.0,10.0))
    println(evaporator(10.0,10.0,5.0))
    println(evaporator(100.0,5.0,5.0))

    }