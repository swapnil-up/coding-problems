package Kyu8

fun maps(x: IntArray): IntArray {
    return x.map { it*2 }.toIntArray()
}

fun main() {
    println(maps(intArrayOf(1, 2, 3)))
    println(maps(intArrayOf(4, 1, 1, 1, 4)))
    println(maps(intArrayOf(2, 2, 2, 2, 2, 2)))
}