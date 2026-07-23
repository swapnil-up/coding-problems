package Kyu8

fun squareSum(n: Array<Int>): Int {
    return n.sumOf { it*it }
}

fun main() {
    println(squareSum(arrayOf(1, 2)))
    println(squareSum(arrayOf(0, 3, 4, 5)))
    println(squareSum(arrayOf()))
}