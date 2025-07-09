package Kyu8

fun past(h: Int, m: Int, s: Int): Int {
    return (h*3600+m*60+s)*1000
}

fun main() {
    println(past(0, 1, 1))
    println(past(1, 1, 1))
    println(past(0, 0, 0))
    println(past(1, 0, 1))
    println(past(1, 0, 0))
}