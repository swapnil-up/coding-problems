package Kyu8

fun invert(arr: IntArray): IntArray {
    return arr.map { it*-1 }.toIntArray()
}

fun main() {
    println(invert(intArrayOf(1,2,3,4,5)))
    println(invert(intArrayOf(1,-2,3,-4,5)))
    println(invert(intArrayOf()))
    println(invert(intArrayOf(0)))
}