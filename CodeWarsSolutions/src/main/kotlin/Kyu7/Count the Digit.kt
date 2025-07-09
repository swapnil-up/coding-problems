package Kyu7

fun nbDig(n:Int, d:Int):Int {
    var s=0
    for (i in 0..n){
        if((i*i).toString().contains(d.toString())) s+=(i*i).toString().split(d.toString()).count()-1
    }
    return s
}

fun main() {
    println("Fixed Tests nbDig")
    println(nbDig(5750, 0))
    println(nbDig(11011, 2))
    println(nbDig(25, 1))


}