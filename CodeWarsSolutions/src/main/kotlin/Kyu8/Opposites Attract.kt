package Kyu8

fun loveFun(flowerA: Int, flowerB: Int): Boolean= flowerA%2!=flowerB%2

fun main() {
    println(loveFun(1, 4))
    println(loveFun(2, 2))
    println(loveFun(0, 1))
    println(loveFun(0, 0))
}