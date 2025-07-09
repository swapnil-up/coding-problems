package Kyu8

fun simpleMultiplication(n: Int): Int {
    if (n%2==0) return n*8 else return n*9
}


fun main() {
    println(simpleMultiplication(1))
    println(simpleMultiplication(3))
    println(simpleMultiplication(2))
    println(simpleMultiplication(4))
}