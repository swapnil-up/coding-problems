package Kyu6

fun beggars(values: List<Int>, n: Int): List<Int> {
    if (n==0) return listOf()
    else{
        var result= (1..n).map{0}.toMutableList()
        for (i in 1..values.size){
            result[(i-1)%n]+=values[i-1]
        }
        return result
    }
}

fun main() {
    println(beggars(listOf(1,2,3,4,5), 1))
    println(beggars(listOf(1,2,3,4,5), 2))
    println(beggars(listOf(1,2,3,4,5), 3))
    println(beggars(listOf(1,2,3,4,5), 6))
    println(beggars(listOf(1,2,3,4,5), 0))
}