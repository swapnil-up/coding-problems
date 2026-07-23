package Kyu8

object GrassHopper {
    fun summation(n:Int):Int {
        var sum=0
        for (i in 1..n) sum+=i
        return(sum)
    }
}

fun main(){
    println(GrassHopper.summation(1))
    println(GrassHopper.summation(8))
}