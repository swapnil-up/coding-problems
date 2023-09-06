package Kyu8

fun repeatStr(r: Int, str: String) : String = str.repeat(r)

fun main() {
    println( repeatStr(4, "a"))
    println( repeatStr(3, "Hello"))
    println(repeatStr(5, ""))
    println(repeatStr(0, "kata"))
}
