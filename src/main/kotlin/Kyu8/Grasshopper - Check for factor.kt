package Kyu8

fun checkForFactor(base: Int, factor: Int): Boolean {
    if (base%factor==0)    return true
    else return false
}

fun main() {
    println(checkForFactor(10, 2))
    println(checkForFactor(63, 7))
    println(checkForFactor(2450, 5))
    println(checkForFactor(24612, 3))
    println(checkForFactor(9, 2))
    println(checkForFactor(653, 7))
    println(checkForFactor(2453, 5))
    println(checkForFactor(24617, 3))
}