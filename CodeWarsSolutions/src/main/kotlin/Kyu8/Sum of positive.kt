package Kyu8

fun sum(numbers: IntArray): Int {
    var sum = 0
    numbers.forEach { if (it>0) sum+=it}
    return sum
}

fun main() {
    println(sum(intArrayOf(1, 2, 3, 4, 5)))
    println(sum(intArrayOf(1, -2, 3, 4, 5)))
    println(sum(intArrayOf()))
    println(sum(intArrayOf(-1, -2, -3, -4, -5)))
    println(sum(intArrayOf(-1, 2, 3, 4, -5)))
}