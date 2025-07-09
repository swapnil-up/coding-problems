package Kyu7

fun maxMultiple(d: Int, b: Int): Int {
    var n=0
    for (i in d..b)
        if (i%d==0) n=i
    return n
}

fun main() {
    println(maxMultiple(2, 7))
    println(maxMultiple(3, 10))
    println(maxMultiple(7, 17))
    println(maxMultiple(10, 50))
    println(maxMultiple(37, 200))
    println(maxMultiple(7, 100))
}