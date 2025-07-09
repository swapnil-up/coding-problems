package Kyu8

fun century(number: Int): Int {
    if (number/100==0) return 1
    else if (number%100==0)return number/100
    else return number/100+1
}

fun main() {
    println(century(1705))
    println(century(1900))
    println(century(1601))
    println(century(2000))
    println(century(89))
}