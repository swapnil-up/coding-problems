package Kyu8

class Kata {

    fun makeNegative(x: Int): Int {
        if (x>=0) return(-x)
        else return x
    }
}

fun main() {
    println(Kata().makeNegative(42).toLong())
}