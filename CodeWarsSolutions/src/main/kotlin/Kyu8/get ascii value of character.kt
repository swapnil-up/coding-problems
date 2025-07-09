package Kyu8

fun getAscii(c: Char): Int {
    return c.code
}

fun main() {
    println(getAscii('A'))
    println(getAscii(' '))
    println(getAscii('!'))
}