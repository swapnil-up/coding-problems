package Kyu8

fun stringToNumber(str: String): Int {
    return str.toInt()
}

fun main() {
    println(stringToNumber("1234"))
    println(stringToNumber("605"))
    println(stringToNumber("1405"))
    println(stringToNumber("-7"))
}